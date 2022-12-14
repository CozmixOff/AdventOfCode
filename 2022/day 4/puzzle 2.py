f = open('2022/day 4/values.txt','r')
file = f.read()
values = file.split('\n')
score = 0

for i in range (len(values)):
    subvalues = values[i].split(',')
    toanalyze = []
    for j in range (2):
        toadd = subvalues[j].split('-')
        toanalyze.extend(toadd)
    ensemble1 = []
    ensemble2 = []
    for j in range (int(toanalyze[0]),int(toanalyze[1])+1):
        ensemble1.append(j)
    for j in range (int(toanalyze[2]),int(toanalyze[3])+1):
        ensemble2.append(j)
    for i in range (len(ensemble1)):
        if ensemble1[i] in ensemble2:
            score += 1
            break
print(score)