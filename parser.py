import xml.etree.ElementTree as ET

def printElem(elem):
    print("<", elem.tag,' ',sep='',end='')
    for attr in elem.attrib:
        print(attr, '="', elem.attrib[attr], '"',end='', sep='')
    print(">",sep='')
    for child in elem:
        printElem(child)
    print("</", elem.tag, ">", sep='')


inFile = input("Введите имя xml-файла: ")
try:
    tree = ET.parse(inFile)
except FileNotFoundError:
    print("Файл",inFile,"не найден")
    exit(-1)

root = tree.getroot()

if root.tag == "CarList":
    outFile = root.attrib.get('outFile')
    if outFile:
        tree.write(outFile + '.xml', 'utf-8')
        print("Записано в файл", outFile + '.xml')
    else:
        for car in root:
            print("Модель:", car.attrib['model'])
            print("Цена:", car.attrib['price'])
            print("Пробег:", car.attrib['probeg'])
            print("=========")
else:
    printElem(root)
