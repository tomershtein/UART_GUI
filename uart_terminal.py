import tkinter as tk
from tkinter import *
import serial
from tkinter import messagebox
from time import sleep

#GUI Application 
root = tk.Tk()
tkvar = StringVar()                                  #create a Tkinter variable for popup menu
tkvar2 = StringVar()                                 #create 2nd Tkinter variable for input
userInput = None                                     #create user input variable

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9,relx=0.1, rely=0.1)

choices = {'4800','9600','144000','19200','28800'}
tkvar.set('9600')                                    #set the default option
popupMenu = OptionMenu(root, tkvar, *choices)

def saveBaud():
#    global baud_rate
    baud_rate = tkvar.get()
    print('The baud rate is ' + baud_rate)
    return baud_rate

tk.Label(root, text="Choose baud rate:").grid(row=0)
tk.Label(root, text="Input:").grid(row=3)
tk.Label(root, text="Output:").grid(row=4)

e1 = tk.Entry(root,textvariable = tkvar2)            #input
e2 = tk.Entry(root)                                  #output

popupMenu.grid(row=0, column=1)
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)

def saveInput():
    global userInput
    userInput = tkvar2.get()
    print('The input is ' + userInput)
    return userInput

def uart_init(userInput,baud_rate):
    ser = serial.Serial ("/dev/ttyS0", baud_rate)    #open port with baud rate
    while True:
        ser.write(str(userInput).encode())                #write to serial port
        received_data = ser.read()                   #read serial port
        sleep(0.03)
        data_left = ser.inWaiting()                  #check for remaining byte
        received_data += ser.read(data_left)
        print(received_data)                         #print received data
        ser.write(received_data)
        return received_data
    messagebox.showinfo(title='Application', message='UART connection established!') #comment when clicked
    
tk.Button(root, text='Connect', command = uart_init ).grid(row=0, column=2, sticky=tk.W, pady=4)
tk.Button(root, text='Send', command = saveInput ).grid(row=3, column=2, sticky=tk.W, pady=4)

root.mainloop()


#need to find a way to print all inputs by the user
#need to understand how does UART functions --done
#create another text box to show all user inputs 
#solve the serial libary problem
#output to the GUI the process