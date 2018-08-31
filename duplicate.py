testList = ['red1', 'blue', 'red2', 'green', 'blue', 'blue']

testListDict = {}

for item in testList:
    try:
      testListDict[item] += 1
      print("die")
    except:
      testListDict[item] = 1
      # print(item)

print (testListDict)