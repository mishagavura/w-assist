import time
import pyautogui as pg
time.sleep(5)
screenSize = open('db/resolution.txt', 'w', encoding='utf-8')
screenSize.write('{}'.format(pg.size()))
screenSize.close()
mousePos = []
for i in range(50):
    #print(1)
    time.sleep(0.05)
    x, y = pg.position()
    wtr = []
    if len(mousePos) != 0:
        print(len(mousePos))
        print(mousePos[len(mousePos)-1][0])
        print(str(x))
        print('---------')
        if mousePos[len(mousePos)-1][0] == str(x) and mousePos[len(mousePos)-1][1] == str(y) and len(mousePos) > 15 and mousePos[len(mousePos)-2][0] == str(x) and mousePos[len(mousePos)-2][1] == str(y) and mousePos[len(mousePos)-3][0] == str(x) and mousePos[len(mousePos)-3][1] == str(y):
            break
            print('finish')
        else:
            wtr.append(str(x))
            wtr.append(str(y))
            mousePos.append(wtr)
            #print(mousePos)
    else:
        wtr.append(str(x))
        wtr.append(str(y))
        mousePos.append(wtr)
        print(mousePos)
caligraphyFile = open('db/caligraphy.txt', 'w', encoding='utf-8')
for item in mousePos:
    caligraphyFile.write('{}\n'.format(item))
caligraphyFile.close()


caligraphyRead = open('db/caligraphy.txt', 'r', encoding='utf-8')
masToMove = caligraphyRead.read()

masToMove = masToMove.split('\n')
#print(masToMove)
useMouseMas = []
for item in masToMove:
    if item != '':
        item = item.replace("'", "")
        item = item.replace("[", '')
        item = item.replace("]", '')
        item = item.split(', ')
        useMouseMas.append(item)
    print(item)

for item in useMouseMas:
    if item != useMouseMas[0]:
        pg.dragTo(int(item[0]), int(item[1]))
    else:
        pg.moveTo(int(item[0]), int(item[1]))
