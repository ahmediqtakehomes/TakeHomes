package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"regexp"
	"sort"
	"strconv"
)

// solves highest scores problem
// - blank lines in the input are ignored.
// - lines where there are no score are ignored.
//
const (
	usage = "usage:$ go run main.go filename count"

	// readBufferSize is for handling lines where the JSON input is potentially
	// longer than the standard buffer allocation size of 4kb.
	readBufferSize = 4096 * 50
)

// matches 102381098:
var scoreRegexp = regexp.MustCompile(`[0-9]*:`)

// data - holder for ID and score
// params:
// ID    string - the id of the element
// Score int64  - the parsed score
type data struct {
	Score int64  `json:"score"`
	ID    string `json:"id"`
}

// Scores - helper data type to implement the sort.Sort interface
type scores []*data

func (s scores) Len() int           { return len(s) }
func (s scores) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s scores) Less(i, j int) bool { return s[i].Score > s[j].Score }

// set - private helper type to map scores to an ID
type set map[int64]string

// Slice emits a slice of scores from the set
func (s set) Slice() scores {
	slice := scores{}
	for score, id := range s {
		slice = append(slice, &data{ID: id, Score: score})
	}
	return slice
}

// algorithm:
// open the file
// get the count of how many highest scores to return
// create a map of score to ID
// for each line in the file:
//   try to find a "score"
//      fail if you can't
//   try to find a json string
//      fail if you can't
//   parse the json, extract the ID
//     if no id exists in json at top level, error
// transform the set of scores into an array
// sort that array descending based on score
// slice the arry by the count from the beginning
// return json of the slice

func main() {
	filename, count := processInput()
	f := getFile(filename)
	defer f.Close()
	// we create a set to satisfy the requirement:
	// Scores can repeat, but you should only count the `id` of the _last_ line processed as the "winning" `id`.
	scoreToId := set{}
	bufferedReader := bufio.NewReaderSize(f, readBufferSize)
	for {
		line, _, err := bufferedReader.ReadLine()
		if err != nil {
			if err == io.EOF {
				break
			} else {
				printErrorAndExit("failed to read line", err)
			}
		}

		// as per the instructions:
		//
		// If the line has a score that would make it part of the highest scores,
		// then the remainder of the line _must_ be parsable as JSON,
		// and there must be an "id" key at the top level of this JSON doc.
		//
		// this would seem to imply that lines can be invalid? if they are, we just skip'em.
		// alternatively, this could be a fatal error.
		potentialScore := scoreRegexp.Find(line)
		if len(potentialScore) == 0 {
			continue
		}

		// get everything from the line after the `:` of the score
		potentialJson := line[len(potentialScore):]

		// parse the json; if it's nested, we don't care since we're really only looking for the ID
		d := &data{}
		if err := json.Unmarshal(potentialJson, &d); err != nil {
			printErrorAndExit("failed to unmarshal json", err)
		}

		// make sure ID was valid at the top level of JSON
		if d.ID == "" {
			printErrorAndExit("`id` must be specified in top level of JSON", nil)
		}

		// 12310989082: minus the `:`
		potentialScoreString := string(potentialScore[:len(potentialScore)-1])
		score, err := strconv.ParseInt(potentialScoreString, 10, 64)
		if err != nil {
			printErrorAndExit(fmt.Sprintf("somehow failed to parse '%s'", potentialScoreString), err)
			continue
		}
		scoreToId[score] = d.ID
	}
	// create an array and sort it
	finalScores := scoreToId.Slice()
	sort.Sort(finalScores)
	// write output
	// undefined case: what happens when N > input file
	// defensive, but optimistic
	finalScoresLength := int64(len(finalScores))
	if count > finalScoresLength {
		count = finalScoresLength
	}
	writeOutput(finalScores[:count])
}

// printErrorAndExit - print an error and exit with status code 1
func printErrorAndExit(msg string, err error) {
	if err != nil {
		fmt.Printf("%s: %s\n", msg, err.Error())
	} else {
		fmt.Printf("%s\n", msg)
	}
	os.Exit(1)
}

// procsssInput
// returns the filename to open and the N that we should process
// invalid params are fatal errors
func processInput() (string, int64) {
	if len(os.Args) < 3 {
		printErrorAndExit(usage, nil)
	}

	filename, countStr := os.Args[1], os.Args[2]

	count, err := strconv.ParseInt(countStr, 10, 64)
	if err != nil {
		msg := fmt.Sprintf("invalid input '%s'; must be integer", count)
		printErrorAndExit(msg, err)
	}
	return filename, count
}

// getFile gets returns a reference to a file for a given filename
func getFile(filename string) io.ReadCloser {
	f, err := os.Open(filename)
	if err != nil {
		printErrorAndExit("error opening file", err)
	}
	return f
}

// WriteOutput takes whatever and writes it to JSON
func writeOutput(output interface{}) {
	result, err := json.MarshalIndent(output, "", "  ")
	if err != nil {
		printErrorAndExit("error marshalling result", err)
	}
	fmt.Println(string(result))
}
