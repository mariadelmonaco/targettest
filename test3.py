import json

with open("data.json", "r") as f:
    jsonData = json.load(f)

size = 0
total = jsonData[0]['valor']
for i in range(1, len(jsonData), 1):
    fat = jsonData[i]['valor']
    if fat == 0 or fat > 0:
        total = total + fat
    if fat != 0 and fat > 0:
        size += 1


average = total/size

count = 0
for i in jsonData:
    if (i['valor'] >= average):
        count += 1
print("total days in which revenue was greater than the monthly average:", count)

low = jsonData[0]['valor']
high = jsonData[0]['valor']

for i in range(1, len(jsonData), 1):
    fat = jsonData[i]['valor']
    if (fat == 0):
        continue
    if (low == 0 or fat < low):
        low = fat
     
    if high == 0 or fat > high:
        high = fat
print("Lowest billing amount occurred in the month:", low)
print("Highest billing value occurred in the month:", high)


