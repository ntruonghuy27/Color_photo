import tkinter as tk
from tkinter import filedialog
from tkinter import *
import numpy
import tensorflow as tf
from keras.models import load_model
import cv2
import os
from PIL import ImageTk, Image

model=load_model(r'unet11.h5')

window=Tk()
window.geometry('800x600')
window.title('Coloring grayscale image') 
window.configure(background='#CDCDCD')
gray_label=Label(window,background='#CDCDCD', font=('arial',15,'bold'))
gray_label.configure(text='Ảnh gốc')
gray_image = Label(window)
color_label=Label(window,background='#CDCDCD', font=('arial',15,'bold'))
color_label.configure(text='Ảnh dự đoán')
color_image = Label(window)
def upload_image():
    global w,h
    try:
        color_image.configure(image='')
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        w,h=uploaded.size
        uploaded.thumbnail((256,256))
        im=ImageTk.PhotoImage(uploaded)
        gray_image.configure(image=im)
        gray_image.image=im
        show_color_button(file_path)
    except:
        pass

def pred_img(file_path):
    gray=cv2.imread(file_path)
    gray= cv2.resize(gray,(128,128))
    if gray.shape[2]>=3: 
        gray = gray.mean(axis=-1)
    gray = gray/255
    gray_reshape = gray.reshape((1,128,128,1))
    color=model.predict(gray_reshape)[0]

    color= cv2.cvtColor(color*255, cv2.COLOR_BGR2RGB)
    color= cv2.resize(color,(w,h))
    colored_path= file_path.replace('gray_imgs','color_imgs')+".jpg"
    cv2.imwrite(colored_path,color)
    uploaded=Image.open(colored_path)
    uploaded.thumbnail((256,256))
    im=ImageTk.PhotoImage(uploaded)
    color_image.configure(image=im)
    color_image.image=im


def show_color_button(file_path):
    btColor=Button(window,text="Tô màu",command=lambda: pred_img(file_path),padx=10,pady=5)
    btColor.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    btColor.grid(row=2,column=1)

upload=Button(window,text="Tải ảnh lên",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.grid(row=2,column=0)

gray_label.grid(row=0,column=0,padx=10,pady=10)
gray_image.grid(row=1,column=0,padx=10,pady=10)
color_label.grid(row=0,column=1,padx=10,pady=10)
color_image.grid(row=1,column=1,padx=10,pady=10)

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.mainloop()
