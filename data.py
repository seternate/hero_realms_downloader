import xml.etree.ElementTree as Et
from xml.dom import minidom


PATH = 'Cards/' + 'data.txt'
FILE = open(PATH, 'r', encoding='utf-8')
data = FILE.read()
data = data.rsplit('\n', 1)[0]
FILE.close()


matrix = []
for idx, entry in enumerate(data.split('\n')):
    items = entry.split(';')
    card = {'image': items[0]}
    items[0] = items[0].split(',')
    items[2] = items[2].split('◆')
    items[6] = items[6].split()
    for index in range(len(items[2])):
        items[2][index] = items[2][index].strip()
    for index in range(len(items[6])):
        items[6][index] = items[6][index].strip()
    card = {'id': str(idx),
            'image': items[0],
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
    matrix.append(card)


root = Et.Element('herorealms')
deck1 = Et.SubElement(root, 'deck', name='Basis Deck')
for element in matrix:
    card = Et.SubElement(deck1, 'card', id=element['id'], name=element['name'])
    images = Et.SubElement(card, 'images')
    for image in element['image']:
        imageXml = Et.SubElement(images, 'image')
        if image != 'None':
            imageXml.text = image
    types = Et.SubElement(card, 'types')
    for type in element['type']:
        typeXml = Et.SubElement(types, 'type')
        if type != 'None':
            typeXml.text = type
    text = Et.SubElement(card, 'text')
    if element['text'] != 'None':
        text.text = element['text']
    faction = Et.SubElement(card, 'faction')
    if element['faction'] != 'None':
        faction.text = element['faction']
    cost = Et.SubElement(card, 'cost')
    if element['cost'] != 'None':
        cost.text = element['cost']
    if len(element['defense']) is 1:
        defense = Et.SubElement(card, 'defense', guard='0')
    else:
        defense = Et.SubElement(card, 'defense', guard='1')
        defense.text = element['defense'][1]
    level = Et.SubElement(card, 'level')
    if element['level'] != 'None':
        level.text = element['level']
    role = Et.SubElement(card, 'role')
    if element['role'] != 'None':
        role.text = element['role']
    setqty = Et.SubElement(card, 'setqty')
    if element['setqty'] != 'None':
        setqty.text = element['setqty']


doc = minidom.parseString(Et.tostring(root, encoding='utf-8'))
tree = Et.ElementTree(Et.fromstring(doc.toprettyxml(encoding='utf-8')))
tree.write('data.xml', encoding='utf-8', xml_declaration=True)




