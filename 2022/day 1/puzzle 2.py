f = open('2022/day 1/values.txt','r')
file = f.read()
values = file.split('\n')
most,second,third,sum = (0,0,0,0)

for i in range (len(values)):
    if values[i] == '':
        if sum > most:
            third = second
            second = most
            most = sum
        elif sum > second:
            third = second
            second = sum
        elif sum > third:
            third = sum
        sum = 0
    else:
        sum += int(values[i])

total = most + second + third
print (total)