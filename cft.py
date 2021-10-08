# CFT Calculation with Length, width, height
import math


def length():
    length = input("Length :")
    if(len(length) >= 5):
        lengthInc = length[3:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:2]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    elif(len(length) == 4):
        lengthInc = length[3:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:1]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    elif(len(length) == 1):
        finalInt = int(length)
    elif(len(length) == 3):
        lengthInc = length[2:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:1]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    return float(finalInt)


def height():
    length = input("Height :")
    if(len(length) >= 5):
        lengthInc = length[3:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:2]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    elif(len(length) == 4):
        lengthInc = length[3:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:1]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    elif(len(length) == 1):
        finalInt = int(length)
    elif(len(length) == 3):
        lengthInc = length[2:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:1]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    return float(finalInt)


def width():
    length = input("Width :")
    if(len(length) >= 5):
        lengthInc = length[3:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:2]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    elif(len(length) == 4):
        lengthInc = length[3:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:1]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    elif(len(length) == 1):
        finalInt = int(length)
    elif(len(length) == 3):
        lengthInc = length[2:]
        lengthIncConvert = int(lengthInc)/12
        lengthAcerateValue = '%.2f' % lengthIncConvert
        lengthStrConvert = str(lengthAcerateValue[2:])
        lengthFoot = length[:1]
        finalInt = f"{lengthFoot}.{lengthStrConvert}"
    return float(finalInt)


def measurement():
    Math_operation = length() * height() * width()
    total = '%.2f' % Math_operation
    return f"The Measurement of Stone is : {total} SFT"


print(measurement())

