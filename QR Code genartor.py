import tkinter as tk
import pyqrcode

win=tk.Tk()
win.title("QR Code Generator")

def generator():
	url=entry.get()
	qr=pyqrcode.create(url)
	save=qr.svg("myqrcode.svg",scale=5)

label1=tk.Label(win,text="Enter URL here:            "
				,font=("arial",10,"bold"))
label1.grid(row=0,column=0)

entry=tk.Entry(win,width=50)
entry.grid(row=1,column=0)

button=tk.Button(win,text="Generate",command=generator)
button.grid(row=3,column=0)

win.mainloop()
