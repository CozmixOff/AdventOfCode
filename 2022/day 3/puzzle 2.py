f = open('2022/day 3/values.txt','r')
file = f.read()
values = file.split('\n')
dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
badges = []
score = 0

for i in range (int(len(values)/3)):
    group1 = values[3*i]
    group2 = values[3*i+1]
    group3 = values[3*i+2]
    for i in range (len(dict)):
        if dict[i] in group1 and dict[i] in group2 and dict[i] in group3:
            badges.append(dict[i])

for i in range (len(badges)):
    score += dict.index(badges[i]) + 1

print (score)