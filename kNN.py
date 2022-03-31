import numpy as np
bonus = [[95,95], [96,90], [92,98], [85,88], [87,86], [92,80], [75,85], [75,80], [88, 65], [82, 85]]
nobonus = [[20,30], [35,40], [50,45], [20,75], [45,55], [60,60], [70,50], [50,70], [30,75], [55,45]]
data = []

for i in bonus:
    i.append(True)
    data.append(i)
for i in nobonus:
    i.append(False)
    data.append(i)
# ----------------------------------------
a = int(input( "Please type your this year performance score " ))
b = int(input ("Please type your this year work time score "))
n = len(data) # length : 20
distance = []



for i in range (n) :
    distance.append( [ ((a-data[i][0])**2+(b-data[i][1])**2), data[i][2] ])

for i in range(n-1):
    for j in range(0,n-i-1):
        if distance[j][0]>distance[j+1][0]:
            distance[j+1], distance[j] = distance[j], distance[j+1]

# ----------
truee, falsee = 0,0
for i in range(3):
    if distance[i][1]:
        truee+=1
    else:
        falsee+=1
if truee>2:
    print("We predict that you can get bonus this year :D ")
else:
    print("We predict that you cannot get bonus this year :(")



