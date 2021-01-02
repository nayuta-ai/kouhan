import serial, time
import numpy as np

def arudino(left,top,right,bottom):
    print("Open Port")
    ser =serial.Serial("COM4", 9600)
    time.sleep(2)
    while True:
        x=(left+right)/2
        y=(top+bottom)/2
        angle=np.degrees(np.arctan(y/x))
        print(angle)
        angle=int(angle)
        send_data=angle.to_bytes(1,"big")
        ser.write(send_data)
        time.sleep(5)
        print("Close Port")
        ser.close()
        break;

def re(deg):
    print("Open Port")
    ser =serial.Serial("COM4", 9600)
    time.sleep(2)
    while True:
        deg=int(deg)
        data=deg.to_bytes(1,"big")
        ser.write(data)
        time.sleep(3)
        print("Close Port")
        ser.close()
        break;

def push():
    print("Open Port")
    ser =serial.Serial("COM4", 9600)
    time.sleep(2)
    while True:
        deg=0
        data=deg.to_bytes(1,"big")
        ser.write(data)
        time.sleep(3)
        print("Close Port")
        ser.close()
        break;

def data(left,top,right,bottom):
    ser=serial.Serial("COM4",9600)
    time.sleep(2)
    while True:
        x=int((left+right)/2)
        y=int((top+bottom)/2)
        data_x=x.to_bytes(1,"big")
        data_y=y.to_bytes(1,"big")
        ser.write(data_x)
        ser.write(data_y)
        time.sleep(1)
        ser.close()
        break
    
"""
print("Open Port")
ser =serial.Serial("COM3", 9600)
time.sleep(3)
while True:
    print("input")
    deg=input()
    if(deg=="e"):
        print("Close Port")
        ser.close()
        break;
    deg=int(deg)
    data=deg.to_bytes(1,"big")
    ser.write(data)
    time.sleep(3)
    
print("Open Port")
ser =serial.Serial("COM3", 9600)
while True:
    deg=input()
    deg=int(deg)
    data=deg.to_bytes(1,"big")
    ser.write(data)
    print("Close Port")
    ser.close()
    break;
"""

data(120,230,123,234)