import tkinter
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from tkinter import font
 
def coil1set():
    print("coil 1 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(0,True,unit=1)
    rq = client.write_register(0, 100)
    client.close()
def coil1reset():
    print("coil 1 reset")
    v.set("coilreset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(0,False,unit=1)
    client.close()
def coil2set():
    print("coil 2 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(1,True,unit=1)
    client.close()
def coil2reset():
    print("coil 2 reset")
    v.set("coilreset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(1,False,unit=1)
    client.close()
def coil3set():
    print("coil 3 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(2,True,unit=1)
    client.close()
def coil3reset():
    print("coil 3 reset")
    v.set("coilreset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(2,False,unit=1)
    client.close()
def coil4set():
    print("coil 4 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(3,True,unit=1)
    client.close()
def coil4reset():
    print("coil 4 reset")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(3,False,unit=1)
    client.close()
def coil5set():
    print("coil 5 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(4,True,unit=1)
    client.close()
def coil5reset():
    print("coil 5 reset")
    v.set("coilreset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(4,False,unit=1)
    client.close()
def coil6set():
    print("coil 6 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(5,True,unit=1)
    client.close()
def coil6reset():
    print("coil 6 reset")
    v.set("coilreset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(5,False,unit=1)
    client.close()
def coil7set():
    print("coil 7 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(6,True,unit=1)
    client.close()
def coil7reset():
    print("coil 7reset")
    v.set("coilreset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(6,False,unit=1)
    client.close()
def coil8set():
    print("coil 8 set")
    v.set("coilset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(7,True,unit=1)
    client.close()
def coil8reset():
    print("coil 8 reset")
    v.set("coilreset")
    client=ModbusClient('localhost',port=502)
    rq=client.write_coil(7,False,unit=1)
    client.close()

 
window=tkinter.Tk()
f=tkinter.Frame(window)
v=tkinter.StringVar(f)
helv20=font.Font(family='Heveltica',size=20)

b1=tkinter.Button(f,text="Coil 1 set",fg="red",width=10,height=1,font=helv20,command=coil1set).grid(row=0,column=0)
b2=tkinter.Button(f,text="Coil 1 reset",fg="blue",width=10,height=1,font=helv20,command=coil1reset).grid(row=0,column=1)
b3=tkinter.Button(f,text="coil 2 set",fg="red",width=10,height=1,font=helv20,command=coil2set).grid(row=1,column=0)
b4=tkinter.Button(f,text="coil 2 reset",fg="blue",width=10,height=1,font=helv20,command=coil2reset).grid(row=1,column=1)
b5=tkinter.Button(f,text="coil 3 set",fg="red",width=10,height=1,font=helv20,command=coil3set).grid(row=2,column=0)
b6=tkinter.Button(f,text="coil 3 reset",fg="blue",width=10,height=1,font=helv20,command=coil3reset).grid(row=2,column=1)
b7=tkinter.Button(f,text="coil 4 set",fg="red",width=10,height=1,font=helv20,command=coil4set).grid(row=3,column=0)
b8=tkinter.Button(f,text="coil 4 reset",fg="blue",width=10,height=1,font=helv20,command=coil4reset).grid(row=3,column=1)
b9=tkinter.Button(f,text="coil 5 set",fg="red",width=10,height=1,font=helv20,command=coil5set).grid(row=4,column=0)
b10=tkinter.Button(f,text="coil 5 reset",fg="blue",width=10,height=1,font=helv20,command=coil5reset).grid(row=4,column=1)
b11=tkinter.Button(f,text="coil 6 set",fg="red",width=10,height=1,font=helv20,command=coil6set).grid(row=5,column=0)
b12=tkinter.Button(f,text="coil 6 reset",fg="blue",width=10,height=1,font=helv20,command=coil6reset).grid(row=5,column=1)
b13=tkinter.Button(f,text="coil 7 set",fg="red",width=10,height=1,font=helv20,command=coil7set).grid(row=6,column=0)
b14=tkinter.Button(f,text="coil 7 reset",fg="blue",width=10,height=1,font=helv20,command=coil7reset).grid(row=6,column=1)
b15=tkinter.Button(f,text="coil 8 set",fg="red",width=10,height=1,font=helv20,command=coil8set).grid(row=7,column=0)
b16=tkinter.Button(f,text="coil 8 reset",fg="blue",width=10,height=1,font=helv20,command=coil8reset).grid(row=7,column=1)


f.grid()

window.mainloop()

