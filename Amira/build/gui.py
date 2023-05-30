from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox ,Frame
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3
import time
from PIL import Image, ImageTk
import customtkinter

#cunters
qty1=0
qty2=0
qty3=0
qty4=0
qty5=0
qty6=0
qty7=0
qty8=0


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Amira\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#new_invice()
def new_invoice():
    tree.delete(*tree.get_children())
    
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = "amira"
    phone = "666-666"
    subtotal = sum(item[3] for item in invoice_list) 
    salestax = 0.1
    total = subtotal*(1-salestax)
    
    doc.render({"name":name, 
            "phone":phone,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "salestax":str(salestax*100)+"%",
            "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
   
    new_invoice()    


def enter_data(qt,descz,pricez,totalz):
    
    # Create Table
    conn = sqlite3.connect('data1.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS travel_data 
            (qt INT, descz TEXT, pricez FLOAT, totalz FLOAT )
    '''
    conn.execute(table_create_query)
    
    # Insert Data
    data_insert_query = '''INSERT INTO travel_data (qt, descz, pricez, 
    totalz) VALUES 
    (?, ?, ?,?)'''
    data_insert_tuple = (qt,
                          descz, pricez, totalz)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()


window = Tk()

window.geometry("1280x832")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

#create  a tree 
columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text="Total")
tree.place(x=261,
    y=616,
    width=757,
    height=204)
# i1

invoice_list = []
#cinters defs
def itemplus():
    global qty1
    qty1+=1
    my_label1.config(text = qty1)

def itemmins():
    global qty1
    if(qty1>0):
         qty-=1
    my_label1.config(text = qty1)
#adding iteam in tree 
def add_item1():
    global qty1
    if(qty1>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty1*price
         invoice_item = [qty1, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty1,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label1= Label(window,text = qty1)
my_label1.place(x=135,
    y=266,
    width=44,
    height=47)
#-------------------------------------------------
#2
def item2plus():
    global qty2
    qty2+=1
    my_label2.config(text = qty2)

def item2mins():
    global qty2
    if(qty2>0):
         qty2-=1
    my_label2.config(text = qty2)
#adding iteam in tree 
def add_item2():
    global qty2
    if(qty2>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty2*price
         invoice_item = [qty2, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty2,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label2= Label(window,text = qty2)
my_label2.place(x=463,
    y=267,
    width=44,
    height=47)
#-------------------------------------------------
#3
def item3plus():
    global qty3
    qty3+=1
    my_label3.config(text = qty3)

def item3mins():
    global qty3
    if(qty3>0):
         qty3-=1
    my_label3.config(text = qty3)
#adding iteam in tree 
def add_item3():
    global qty3
    if(qty3>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty3*price
         invoice_item = [qty3, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty3,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label3= Label(window,text = qty3)
my_label3.place(x=787,
    y=267,
    width=44,
    height=47)
#-------------------------------------------------
#4
def item4plus():
    global qty4
    qty4+=1
    my_label4.config(text = qty4)

def item4mins():
    global qty4
    if(qty4>0):
         qty4-=1
    my_label4.config(text = qty4)
#adding iteam in tree 
def add_item4():
    global qty4
    if(qty4>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty4*price
         invoice_item = [qty4, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty4,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label4= Label(window,text = qty4)
my_label4.place(x=1100,
    y=267,
    width=44,
    height=47)
#-------------------------------------------------
#5
def item5plus():
    global qty5
    qty5+=1
    my_label5.config(text = qty5)

def item5mins():
    global qty5
    if(qty5>0):
         qty5-=1
    my_label5.config(text = qty5)
#adding iteam in tree 
def add_item5():
    global qty5
    if(qty5>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty5*price
         invoice_item = [qty5, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty5,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label5= Label(window,text = qty5)
my_label5.place(x=137,
    y=555,
    width=44,
    height=47)
#-------------------------------------------------
#6
def item6plus():
    global qty6
    qty6+=1
    my_label6.config(text = qty6)

def item6mins():
    global qty6
    if(qty6>0):
         qty6-=1
    my_label6.config(text = qty6)
#adding iteam in tree 
def add_item6():
    global qty6
    if(qty6>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty6*price
         invoice_item = [qty6, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty6,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label6= Label(window,text = qty6)
my_label6.place(x=463,
    y=555,
    width=44,
    height=47)
#-------------------------------------------------
#7
def item7plus():
    global qty7
    qty7+=1
    my_label7.config(text = qty7)

def item7mins():
    global qty7
    if(qty7>0):
         qty7-=1
    my_label7.config(text = qty7)
#adding iteam in tree 
def add_item7():
    global qty7
    if(qty7>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty7*price
         invoice_item = [qty7, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty7,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label7= Label(window,text = qty7)
my_label7.place(x=787,
    y=553,
    width=44,
    height=47)
#-------------------------------------------------
#8
def item8plus():
    global qty8
    qty8+=1
    my_label8.config(text = qty8)

def item8mins():
    global qty8
    if(qty8>0):
         qty8-=1
    my_label8.config(text = qty8)
#adding iteam in tree 
def add_item8():
    global qty8
    if(qty8>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty8*price
         invoice_item = [qty8, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty8,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label8= Label(window,text = qty8)
my_label8.place(x=1106,
    y=555,
    width=44,
    height=47)
#-------------------------------------------------

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    416.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item1(),
    relief="flat"
)
button_1.place(
    x=28.0,
    y=35.0,
    width=257.198486328125,
    height=212.85394287109375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item5(),
    relief="flat"
)
button_2.place(
    x=29.77374267578125,
    y=321.4659118652344,
    width=257.19854736328125,
    height=212.85394287109375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item8(),
    relief="flat"
)
button_3.place(
    x=992.937744140625,
    y=321.4659118652344,
    width=257.198486328125,
    height=212.85394287109375
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item4(),
    relief="flat"
)
button_4.place(
    x=994.7115478515625,
    y=35.0,
    width=257.198486328125,
    height=212.85394287109375
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item6(),
    relief="flat"
)
button_5.place(
    x=350.8284912109375,
    y=321.4659118652344,
    width=257.198486328125,
    height=212.85394287109375
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item7(),
    relief="flat"
)
button_6.place(
    x=671.8831787109375,
    y=321.4659118652344,
    width=257.198486328125,
    height=212.85394287109375
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item2(),
    relief="flat"
)
button_7.place(
    x=356.14990234375,
    y=35.0,
    width=257.198486328125,
    height=212.85394287109375
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item3(),
    relief="flat"
)
button_8.place(
    x=684.2998046875,
    y=35.0,
    width=257.198486328125,
    height=212.85394287109375
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemplus(),
    relief="flat"
)
button_9.place(
    x=65.0,
    y=267.0,
    width=44.0,
    height=47.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5plus(),
    relief="flat"
)
button_10.place(
    x=66.76239013671875,
    y=554.7183837890625,
    width=44.82086181640625,
    height=45.698272705078125
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2plus(),
    relief="flat"
)
button_11.place(
    x=391.0,
    y=267.0,
    width=45.0,
    height=47.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6plus(),
    relief="flat"
)
button_12.place(
    x=391.44970703125,
    y=554.7183837890625,
    width=44.82080078125,
    height=45.698272705078125
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8plus(),
    relief="flat"
)
button_13.place(
    x=1028.1832275390625,
    y=554.7183837890625,
    width=44.82080078125,
    height=45.698272705078125
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3plus(),
    relief="flat"
)
button_14.place(
    x=718.0,
    y=267.0,
    width=44.0,
    height=47.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7plus(),
    relief="flat"
)
button_15.place(
    x=717.807373046875,
    y=554.7183837890625,
    width=44.82080078125,
    height=45.698272705078125
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4plus(),
    relief="flat"
)
button_16.place(
    x=1029.0,
    y=267.0,
    width=44.0,
    height=47.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemmins(),
    relief="flat"
)
button_17.place(
    x=208.0,
    y=267.0,
    width=44.0,
    height=47.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5mins(),
    relief="flat"
)
button_18.place(
    x=208.656982421875,
    y=554.7183837890625,
    width=44.82086181640625,
    height=45.698272705078125
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2mins(),
    relief="flat"
)
button_19.place(
    x=533.0,
    y=267.0,
    width=45.0,
    height=47.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6mins(),
    relief="flat"
)
button_20.place(
    x=533.344482421875,
    y=554.7183837890625,
    width=44.82080078125,
    height=45.698272705078125
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8mins(),
    relief="flat"
)
button_21.place(
    x=1171.0,
    y=555.0,
    width=44.0,
    height=45.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3mins(),
    relief="flat"
)
button_22.place(
    x=860.0,
    y=267.0,
    width=44.0,
    height=47.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7mins(),
    relief="flat"
)
button_23.place(
    x=859.7020263671875,
    y=554.7183837890625,
    width=44.82080078125,
    height=45.698272705078125
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4mins(),
    relief="flat"
)
button_24.place(
    x=1171.0,
    y=267.0,
    width=44.0,
    height=47.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: new_invoice(),
    relief="flat"
)
button_25.place(
    x=1037.0,
    y=647.0,
    width=173.0,
    height=143.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_invoice(),
    relief="flat"
)
button_26.place(
    x=75.0,
    y=647.0,
    width=173.0,
    height=143.0
)
def check():
    if entry_user.get()=="amira" and entry_pass.get()=="123":
        LOGIN.destroy()
        
LOGIN = Frame( window)

# Create a photoimage object of the image in the path
# 1440x950
LOGIN.place(x=0,y=0,width=1512,height=982)
LOGIN.configure(background="white")
LOGIN_IM = Image.open(r"D:\Amira\build\assets\frame0\login.png")
test_LOGIN = ImageTk.PhotoImage(LOGIN_IM)
LOGOIN = Label(LOGIN,background="white",image=test_LOGIN).place(
    x=0,
    y=0,
    
)






entry_user = customtkinter.CTkEntry(master=LOGIN,
                               
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               
                               width=433,
                               height=45,
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=12)
entry_user.place(x=410,y=410)

entry_pass = customtkinter.CTkEntry(master=LOGIN,
                               
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               width=434,
                               height=46,
                               show="*",
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=12)
entry_pass.place(x=410,y=515)

button_login = customtkinter.CTkButton(master=LOGIN,
                                 
                                 width=425,
                                 height=58,
                                 fg_color=("#1E1E1E","#1E1E1E"),
                                 border_width=0,
                                 corner_radius=37,
                                 text="LOGIN",
                                 command=check)
button_login.place(x=426,y=586)



#LOGO.image = test

w = Frame( window)
# Create a photoimage object of the image in the path
w.place(x=0,y=0,width=1512,height=982)
image1 = Image.open(r"D:\Amira\build\assets\frame0\start.png")
test = ImageTk.PhotoImage(image1)
LOGO = Label(w,image=test).pack()
#LOGO.image = test

window.after(2000,lambda:w.destroy())

window.resizable(False, False)
window.mainloop()
