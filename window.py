# 引入套件
import tkinter as tk
import RPi.GPIO as gpio
import time

w = tk.Tk()
t_f = tk.Frame(w)

t_f.pack()
b_f = tk.Frame(w)
b_f.pack(side=tk.BOTTOM)


gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
def forward():
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True) 
    gpio.output(24, False)
    print ("forward")
 
def reverse():
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False) 
    gpio.output(24, True)
    print ("reverse")

 
def right():
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    print ("left")
    
def left():
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    print ("right")

def stop():
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)

l_b = tk.Button(t_f, text='front', fg='blue',command=forward)
l_b.pack(side=tk.LEFT)

m_b = tk.Button(t_f, text='left', fg='blue',command=left)
m_b.pack(side=tk.LEFT)

r_b = tk.Button(t_f, text='back', fg='blue',command=reverse)
r_b.pack(side=tk.LEFT)

t_b = tk.Button(t_f, text='right', fg = 'blue',command=right)
t_b.pack(side=tk.TOP)


b_b = tk.Button(b_f, text='stop', fg='blue', command=stop)

b_b.pack(side=tk.BOTTOM)


w.mainloop()