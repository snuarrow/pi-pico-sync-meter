from i2c_lcd import I2cLcd
from characters import empty, line0, line1, line2, line3, line4

lastIndex = 0

def initChars(lcd: I2cLcd):
    lcd.custom_char(0, line0)
    lcd.custom_char(1, line1)
    lcd.custom_char(2, line2)
    lcd.custom_char(3, line3)
    lcd.custom_char(4, line4)
    lcd.custom_char(5, empty)
    return lcd

def clearChar(lcd: I2cLcd, line: int, index: int):
    
    charIndex = int(index * (16 / 80))
    #print("clearing:", charIndex)
    #lineIndex = (index % 5)
    lcd.move_to(charIndex, line)
    lcd.putchar(chr(5))

def drawLine(lcd: I2cLcd, line: int, index: int, previousIndex: int):

    clearChar(lcd, line, previousIndex)
    charIndex = int(index * (16 / 80))
    lineIndex = (index % 5)

    #print("index:", index, "charIndex:", charIndex, "lineIndex:", lineIndex)

    lcd.move_to(charIndex, line)
    #lcd.putchar(chr(1))
    #return

    if lineIndex == 0:
        #print('line0')
        lcd.putchar(chr(0))
        return

    if lineIndex == 1:
        #print('line1')
        lcd.putchar(chr(1))
        return

    if lineIndex == 2:
        #print('line2')
        lcd.putchar(chr(2))
        return

    if lineIndex == 3:
        #print('line3')
        lcd.putchar(chr(3))
        return

    if lineIndex == 4:
        #print('line4')
        lcd.putchar(chr(4))
        return