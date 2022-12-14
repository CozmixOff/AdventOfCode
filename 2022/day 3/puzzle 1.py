f = open('2022/day 3/values.txt','r')
file = f.read()
values = file.split('\n')
dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
doubles = []
score = 0

for i in range (len(values)):
    used = []
    value = values[i]
    start = []
    for j in range (int(len(value)/2)):
        start.append(value[j])
    end = []
    for j in range (int(len(value)/2),len(value)):
        end.append(value[j])
    for j in range (len(start)):
        if end[j] in start:
            doubles.append(end[j])
            break

for i in range (len(doubles)):
    score += dict.index(doubles[i]) + 1

print (score)