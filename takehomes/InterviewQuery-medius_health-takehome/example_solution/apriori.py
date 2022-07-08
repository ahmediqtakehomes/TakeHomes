#
# Native implementation for Apriori Algorithm
#
# This script assumes the input TSV file come from clean.py.
# 
# Run with python3 apriori.py data.tsv 10 where 10 is the support threshold
#

import sys
import itertools
from queue import Queue

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(('\nRun with python3 apriori.py data.tsv 10 where 10 is the support threshold'))
    else:
        # Support threshold (no type checking assuming it's an integer)
        thre = int(sys.argv[2])

        def readTSV(name):
            r = open(name, 'r')
            for line in r:
                strs = line.split('\t')
                assert(len(strs) == 2)
                yield (strs[0], strs[1].strip())

        #
        # Native implementation for candidate generation (simply join the items)
        #

        def candidate(items, k1):
            return (([i + ' ' + j for i in items for j in k1]))

        #
        # Native implementation for counting input items and return a dictionary with the counts
        #

        def count(items, trans, k):
            x = {i:0 for i in items}
            for tran in trans:
                for item in items:
                    c1 = tran.count(' ' + item + ' ')
                    c2 = 1 if tran.endswith(item) else 0
                    c3 = 1 if tran.startswith(item) else 0
                    x[item] += (c1 + c2 + c3)
            return x
    
        # Transactions (e.g. medical records)
        trans = []

        # Data structure for breadth-first search
        q = Queue()

        for (x, y) in readTSV(sys.argv[1]):
            trans.append(y)
    
            # Our cleanup script guarantees no English stopwords, no tabs etc. We just need to break the text by space to get individual words.
            for i in y.split(' '):
                q.put(i)

        # Candidate item sets of length 
        k = 2

        # Frequent items
        fi = {}
        
        # Counts for the frequent items
        fc = {}

        #
        # Apply breadth-first search with pruning
        #

        while not q.empty():
            items = set()
    
            # Get all items from the queue, more effiicient for counting the items
            while not q.empty():
                items.add(q.get())

            # Count the items
            freq = count(items, trans, k) 

            # Prunce away all items that are smaller than the support threshold. We can do this because of the apriori property.
            items = [i for i in items if freq[i] >= thre]

            if len(items) > 0:
                fi[k-1] = items
                fc[k-1] = freq
                
                # Compute candidate sets at k
                for j in candidate(items, fi[1]):
                    q.put(j)
            
                k += 1

        for i in fi:
            for j in fi[i]:
                print(str(j) + '\t' + str(fc[i][j]))
