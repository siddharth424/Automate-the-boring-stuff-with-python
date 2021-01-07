tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
for i in range(len(tableData[1])):
    for j in tableData:
        print(j[i],end=' ')
    print('')
