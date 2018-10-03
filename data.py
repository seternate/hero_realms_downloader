PATH = 'Cards/' + 'data.txt'
FILE = open(PATH, 'r', encoding='utf-8')
data = FILE.read()
data = data.rsplit('\n', 1)[0]
FILE.close()


matrix = []
for entry in data.split('\n'):
    items = entry.split(';')
    card = {'image': items[0]}
    items[0] = items[0].split(',')
    items[2] = items[2].split('◆')
    for index in range(len(items[2])):
        items[2][index] = items[2][index].strip()
    card = {'image': items[0],
            'name': items[1],
            'type': items[2],
            'text': items[3],
            'faction': items[4],
            'cost': items[5],
            'defense': items[6],
            'level': items[7],
            'role': items[8],
            'setname': items[9],
            'setqty': items[10]}
    matrix.append(items)


print(matrix)
