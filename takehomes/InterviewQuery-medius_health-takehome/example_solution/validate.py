lines = []
with open('data.tsv', 'r') as r:
    for line in r:
        lines.append(line.split('\t')[1])

with open('A.txt', 'r') as r:
    for line in r:
        key = line.split('\t')[0]
        n = 0
        for line in lines:
            line = line.strip()            
            c1 = line.count(' ' + key + ' ')
            c2 = 1 if line.startswith(key) else 0
            c3 = 1 if line.endswith(key) else 0                                    
            n += (c1 + c2 + c3)
        print(str(key) + '\t' + str(n))