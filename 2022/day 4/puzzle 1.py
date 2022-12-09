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
    if int(toanalyze[0]) in ensemble2 and int(toanalyze[1]) in ensemble2:
        score += 1
    elif int(toanalyze[2]) in ensemble1 and int(toanalyze[3]) in ensemble1:
        score += 1
    print (toanalyze)
    print (ensemble1)
    print (ensemble2)
    print ('')
print(score)