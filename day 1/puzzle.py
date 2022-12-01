f = open('day 1/values.txt','r')
file = f.read()
values = file.split('\n')
most = 0
sum = 0

for i in range (len(values)):
    if values[i] == '':
        if sum > most:
            most = sum
        sum = 0
    else:
        sum += int(values[i])

print (most)