import tkinter as Tkinter 
from datetime import datetime
import time
counter = 66600
running = False
def counter_label(label): 
	def count(): 
		if running: 
			global counter 

 
			if counter==66600:			 
				display="Starting Stopwatch..."
			else:
				tt = datetime.fromtimestamp(counter)
				string = tt.strftime("%H:%M:%S")
				display=string 

			label['text']=display  

			
			
			label.after(1000, count) 
			counter += 1

	 
	count()	 


def Start(label): 
	global running 
	running=True
	counter_label(label) 
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'
	quit['state']='normal'


def Stop(): 
	global running 
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	quit['state']='disabled'
	running = False

 
def Reset(label): 
	global counter 
	counter=66600

	
	
root = Tkinter.Tk() 
root.title("Stopwatch app") 

# Fixing the window size. 
root.minsize(width=500, height=350) 
label = Tkinter.Label(root, text="Welcome to stopwatch", fg="black", font="aerial 40 bold") 
label.pack() 
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=10,height=9,command=lambda:Start(label)) 
stop = Tkinter.Button(f, text='Stop',width=10,height=9,state='disabled', command=Stop) 
reset = Tkinter.Button(f, text='Reset',width=10, height=9,state='disabled', command=lambda:Reset(label)) 
quit=Tkinter.Button(f,text='Quit',width=10,height=9,state='disabled',command=quit)
f.pack(anchor = 'center',pady=5)
start.pack(side="left") 
stop.pack(side ="left") 
reset.pack(side="left") 
quit.pack(side="left")
root.mainloop()
