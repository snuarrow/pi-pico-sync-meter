import machine
from machine import I2C
import math
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from graphics import drawLine, initChars
from characters import line0, line1, line2, line3, line4
from sync_meter import PressureSensor
I2C_ADDR = 0x38
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=500000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.move_to(1,0)
lcd.putstr('yolo')
lcd.clear()
import machine
import utime
 
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

ra = [0,0,0,0,0,0,0]
ri = 0
rsum = 0

lcd = initChars(lcd=lcd)

def next_index(i):
    if i == 6:
        return 0
    else:
        return i + 1

def filter_value(value):
    global ra, ri, rsum
    oldest = ra[ri]
    rsum -= oldest
    ra[ri] = value
    rsum += value
    ri = next_index(ri)
    return rsum / 7

index = 0
previousIndex = 0
pressureSensor0 = PressureSensor(0)
pressureSensor0.setBand(15000, 25000)

while True:
    #reading = sensor_temp.read_u16() * conversion_factor 
    #temperature = 27 - (reading - 0.706)/0.001721
    previousRead0 = pressureSensor0.getPreviousRead()
    read0 = pressureSensor0.read80()
    lcd.clear()
    #clearChar(lcd, 0, index-1)
    sine_index = math.sin(index/math.pi/4)
    sine_index *= 0.97
    sine_index += 1
    sine_index = int(sine_index * 80 / 2)

    drawLine(lcd, 0, int(read0), 70)
    drawLine(lcd, 1, sine_index, previousIndex)
    previousIndex = sine_index
    index += 1

    if index == 80:
        index = 0

    #lcd.backlight_off()

    #pressure_0 = machine.ADC(0).read_u16()
    #max = 5000
    #min = 2500
    #lcd.custom_char(0, line0)
    #pressure_0 = filter_value(pressure_0)
    #lcd.putstr(str(chr(0)))
    utime.sleep(0.05)