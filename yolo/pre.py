import numpy as np
import pyfirmata
import time

def arudino(left,top,right,bottom):
    print("Open Port")
    board = pyfirmata.Arduino('COM4')
    it = pyfirmata.util.Iterator(board)
    it.start()

    time.sleep(1)
    x=(left+right)/2
    y=(top+bottom)/2
    angle=np.degrees(np.arctan(y/x))
    angle=int(angle)

def pre():
    print("Open Port")
    board = pyfirmata.Arduino('COM4')
    it = pyfirmata.util.Iterator(board)
    it.start()
    pin1 = board.get_pin('d:4:s') 
    pin1.write(100)
    time.sleep(0.5)
    pin1.write(0)
    print("Close Port")
"""
def board():
    board=pyfirmata.Arduino('COM4')
    it=pyfirmata.util.Iterator(board)
    it.start()
    pin=board.get_pin('d:4:s')
    pinIN1=board.get_pin('d:7:o')
    pinIN2=board.get_pin('d:8:o')
    pinIN3=board.get_pin('d:9:o')
    pinIN4=board.get_pin('d:10:o')
"""
def motor():
    board=pyfirmata.Arduino('COM4')
    it=pyfirmata.util.Iterator(board)
    it.start()
    pin=board.get_pin('d:4:s')
    """
    pinIN1=board.get_pin('d:7:o')
    pinIN2=board.get_pin('d:8:o')
    pinIN3=board.get_pin('d:9:o')
    pinIN4=board.get_pin('d:10:o')
    pinENA=board.get_pin('a:5:o')
    pinENB=board.get_pin('a:6:o')
    pinENA.write(255)
    pinENB.write(255)
    pinIN3.write(1)
    pinIN4.write(0)
    time.sleep(3)
    """
    board.analog[5].write(255)
    board.analog[3].write(255)
    board.digital[7].write(1)
    board.digital[8].write(0)
    board.digital[9].write(1)
    board.digital[10].write(0)
    pin.write(100)
    time.sleep(0.1)
    pin.write(0)    
motor()


