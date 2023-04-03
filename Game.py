from tkinter import *
import random
import keyboard
import time
from PIL import Image, ImageTk


root = Tk()
root.geometry("1250x700")
canvas = Canvas(root,width=1250,height=700, bg='#6a788f')
canvas.pack()
x_mouse = random.randrange(0,1000,50)
y_mouse = random.randrange(0,650,50)
mouse=canvas.create_rectangle(x_mouse,y_mouse,x_mouse+50,y_mouse+50)
x_snake = random.randrange(0,1100,50)
y_snake = random.randrange(0,650,50)
direction='right'
listsq = []
listpos = []
listpos.append([x_snake,y_snake])
play = True


def make_mouse():
    global x_mouse,y_mouse,mouse

    x_mouse = random.randrange(50,1200,50)
    y_mouse = random.randrange(50,650,50)
    canvas.delete(mouse)  
    mouse = canvas.create_rectangle(x_mouse,y_mouse,x_mouse+50,y_mouse+50,fill='red')

def make_snake():
    global x_snake

    for i in range(3):
        x_snake+=50
        listsq.append(canvas.create_rectangle(x_snake,y_snake,x_snake+50,y_snake+50,fill='black'))

def crash():
    global x_snake,y_snake,play

    for i in range(0,len(listpos)-1):
        if (x_snake+25) in range(listpos[i][0],listpos[i][0]+51) and (y_snake+25) in range(listpos[i][1],listpos[i][1]+51):
            canvas.delete("all")
            img = ImageTk.PhotoImage(Image.open("GameOver.png").resize((1350,700)))  
            canvas.create_image(575, 350, image=img)
            canvas.update()
            time.sleep(2)
            root.destroy()
            play = False 
            break

            
def screenEnd():
    global mouse,x_snake,y_snake

    x_snake = 1200 if x_snake<0 else x_snake
    x_snake = 0 if x_snake>1200 else x_snake
    y_snake = 650 if y_snake<0 else y_snake
    y_snake = 0 if y_snake>650 else y_snake

    update(x_snake,y_snake)

def update(x1,y1):
    global x_mouse,y_mouse,x_snake,y_snake

    listpos.append([x_snake,y_snake])

    if (x1+25) in range(x_mouse,x_mouse+51) and (y1+25) in range(y_mouse,y_mouse+51):        
            listsq.append(canvas.create_rectangle(x1,y1,x1+50,y1+50,fill='black'))
            make_mouse()
    else:
        canvas.delete(listsq[0])
        listsq.pop(0)
        listsq.append(canvas.create_rectangle(x1,y1,x1+50,y1+50,fill='black'))
        listpos.pop(0)

    crash()

def leftcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('left'):
        x_snake-=50
        direction='left'

    elif direction=='left':
        x_snake-=50
        direction='left'

def rightcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('right'):
        x_snake+=50
        direction='right'
    
    elif direction=='right':
        x_snake+=50
        direction='right'

def upcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('up'):
        y_snake-=50
        direction='up'

    elif direction=='up':
        y_snake-=50
        direction='up'

def downcheck():
    global x_snake,y_snake,direction

    if keyboard.is_pressed('down'):
        y_snake+=50
        direction='down'

    elif direction=='down':
        y_snake+=50
        direction='down'


def structure():
    global direction

    if direction=='up':
        leftcheck()
        rightcheck()
        upcheck()

    elif direction=='down':
        leftcheck()
        rightcheck()
        downcheck()

    elif direction=='left':
        upcheck()
        downcheck()
        leftcheck()

    elif direction=='right':
        upcheck()
        downcheck()
        rightcheck()
    
    screenEnd()

def Gamestart():
    global direction,listsq,mouse

    canvas = Canvas(root,width=1250,height=700)
    canvas.pack()
    x_mouse = random.randrange(1,1100,50)
    y_mouse = random.randrange(1,660,50)
    mouse=canvas.create_rectangle(x_mouse,y_mouse,x_mouse+50,y_mouse+50)
    x_mouse = random.randrange(1,1200,50)
    y_mouse = random.randrange(1,660,50)
    direction='right'
    listsq = []
    listpos = []
    listpos.append([x_snake,y_snake])
    make_mouse()
    make_snake()
    while(play):    
        structure()
        canvas.update()
        time.sleep(0.05)
            
    root.mainloop()




Gamestart()