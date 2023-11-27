from tkinter import *
import os.path
from tkinter import filedialog
import pytesseract
from PIL import Image  
from tkinter import messagebox
window1 =Tk()
window1.geometry('560x450')
window1.title('EXTRACT TEXT FROM IMAGE AND VIDEO')
window1.resizable(False,False)
window1.configure(bg='white')

#======DEFINE=======
def imo():
    file=filedialog.askopenfile(mode='r',filetypes=[('PNG FILES','*.png')])
    if file:
        filepath=os.path.abspath(file.name)
        En1.insert(0,filepath)
    
def ORC() :
    pytesseract.pytesseract.tesseract_cmd= "C:\\Program Files (x86)\Tesseract-OCR\\tesseract.exe"
    savo= En2.get()
    file=En1.get()
    lang=En3.get()

    image=Image.open(file)
    txt=pytesseract.image_to_string(image)
    with open(savo,"w") as f :
        f.write(txt)
    messagebox.showinfo('alla','\n THE FILE SAVED') 
    

 
#======TOLES======
f1=Frame(window1,width=600,height=368,bg='white',bd=1,relief=SOLID)
f1.place(x=3,y=1)

text =Label(f1,text='program:[IMG 2 TEXT]',font=13,fg='black',bg='white')
text.place(x=1,y=4)

En1_text=Label(f1,text='Image Path :',fg='black',bg='white',font=13)
En1_text.place(x=10,y=51)
En1=Entry(f1,font=13,width=30,bd=1,relief=SOLID)
En1.place(x=130,y=50)

bt1=Button(f1,text='+',cursor='hand2',command=imo)
bt1.place(x=445,y=51)

En2_text=Label(f1,text='SAVE Path :',fg='black',bg='white',font=13)
En2_text.place(x=10,y=84)
En2=Entry(f1,font=13,width=30,bd=1,relief=SOLID)
En2.place(x=130,y=84)

En3_text=Label(f1,text='Language :',fg='black',bg='white',font=13)
En3_text.place(x=10,y=117)
En3=Entry(f1,font=13,width=30,bd=1,relief=SOLID)
En3.place(x=130,y=117)


b1=Button(f1,text='EXTRACT TEXT',width=10 ,height=6 ,fg='black',bg='#383838',cursor='hand2',command=ORC)
b1.place(x=470,y=49)

logo=PhotoImage(file='logo.png')
logo_lb1=Label(window1,image=logo)
logo_lb1.place(x=1,y=160)



#C:\Program Files (x86)\Tesseract-OCR
         



window1.mainloop()