from tkinter import *
import time
from tkinter import messagebox

finproj = Tk()
finproj.geometry("1400x720")
finproj.config(background="sky blue")
finproj.title("Refreshments")

textin=StringVar()
operator=""
enter=IntVar()
totalbill = 0.0


def stp():
    exit(1)

def billbutton():

    name = username.get()
    phone_no = phno.get()

    def prnt():
        pass
    
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="prashant")
    myCursor = mydb.cursor()
    sql = "INSERT INTO `customer_info`(`user_name`, `contact_no`) VALUES ('" + name + "'," + phone_no + ")"
    myCursor.execute(sql)
    mydb.commit()
    id_no = myCursor.lastrowid
    sql1 = "SELECT * FROM `customer_info` WHERE `order_id`=" + str(id_no)
    myCursor.execute(sql1)
    record = myCursor.fetchall()
    billwin = Toplevel(finproj)
    billwin.geometry("520x450")
    billwin.config(background="white")
    billwin.title("BILL")
    lbl = Label(billwin,text="CAFE HOME",bg="white",font="algerian 17")
    lbl.pack()
    l1 = Label(billwin,text="Order no. :",bg="white",font="arial 12")
    l1.place(x=20,y=40)
    l01 = Label(billwin,bg="white",font="arial 12")
    l01.place(x=100,y=40)
    orderid = str(id_no)
    l01.config(text=""+orderid)
    l2 = Label(billwin,bg="white",font="arial 12")
    l2.place(x=130,y=70)
    l2.config(text=""+name)
    l3 = Label(billwin,bg="white",font="arial 12")
    l3.place(x=335,y=70)
    l3.config(text=""+phone_no)
    qty1 = int(cap.get("0.0",END))
    qty2 = int(bcoff.get("0.0",END))
    qty3 = int(flatw.get("0.0",END))
    qty4 = int(mocha.get("0.0",END))
    qty5 = int(irishc.get("0.0",END))
    qty6 = int(macch.get("0.0",END))
    qty7 = int(aulait.get("0.0",END))
    qty8 = int(affo.get("0.0", END))
    c1,c2,c3,c4,c5,c6,c7,c8 = 50,60,80,100,80,90,110,120
    tot1 = qty1 * c1
    tot2 = qty2 * c2
    tot3 = qty3 * c3
    tot4 = qty4 * c4
    tot5 = qty5 * c5
    tot6 = qty6 * c6
    tot7 = qty7 * c7
    tot8 = qty8 * c8

    total_cost = tot1+ tot2 + tot3 + tot4 + tot5 + tot6 + tot7 + tot8
    a = total_cost
    b = (a*5)/100
    total_bill = total_cost + b
    listbox = Listbox(billwin,font="arial 10",height = 17,width = 66,relief = "flat")
    listbox.place(x=30,y=100)
    listbox.delete(0,END)
    listbox.insert("end", "                                                 ")
    listbox.insert("end", "                                                 ")
    listbox.insert("end", "              MENU                      QUANTITY                 COST     ")
    listbox.insert("end", "                                                 ")
    listbox.insert("end", "           Cappuccino                              " + str(qty1) + "                    " + str(qty1 * 50) + " Rs")
    listbox.insert("end", "          Black Coffee                              " + str(qty2) + "                    " + str(qty2 * 60) + " Rs")
    listbox.insert("end", "           Flat White                                " + str(qty3) + "                    " + str(qty3 * 80) + " Rs")
    listbox.insert("end", "             Mocha                                   " + str(qty4) + "                    " + str(qty4 * 100) + " Rs")
    listbox.insert("end", "          Irish Coffee                                " + str(qty5) + "                    " + str(qty5 * 80) + " Rs")
    listbox.insert("end", "            Macchiato                               " + str(qty6) + "                    " + str(qty6 * 90) + " Rs")
    listbox.insert("end", "          Latte Au Lait                             " + str(qty7) + "                    " + str(qty7 * 110) + " Rs")
    listbox.insert("end", "            Affogato                                  " + str(qty8) + "                    " + str(qty8 * 120) + " Rs")
    listbox.insert("end", "                                                 ")
    listbox.insert("end", "                                                                          TOTAL   " +str(total_bill)+ "")
    listbox.selection_set(first=0, last=None)
    listbox.configure(exportselection=False)
    listbox.configure(state=DISABLED)
    exitbut = Button(billwin,text="PRINT",font="arial 10",width="10",fg="white",bg="brown",activebackground="brown",relief="raised",command=prnt)
    exitbut.place(x=215,y=400)

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     global operator
     operator=""
     textin.set("")

def blackcoffee():
     k = bcoff.get("1.0",END)
     bcoff.delete("1.0",END)
     bcoff.insert(END,int(k) + 1)

def sub2():
     k = bcoff.get("1.0",END)
     bcoff.delete("1.0",END)
     if(int(k)) == 0:
          bcoff1.insert(END,0)
     else:
          bcoff.insert(END,int(k)-1)

def capuchino():
     k = cap.get("1.0",END)
     cap.delete("1.0",END)
     cap.insert(END,int(k) + 1)

def sub1():
     k = cap.get("1.0",END)
     cap.delete("1.0",END)
     if(int(k)) == 0:
          cap.insert(END,0)
     else:
          cap.insert(END,int(k)-1)
def flatwhite():
     k = flatw.get("1.0",END)
     flatw.delete("1.0",END)
     flatw.insert(END,int(k) + 1)

def sub3():
     k = flatw.get("1.0",END)
     flatw.delete("1.0",END)
     if(int(k)) == 0:
          flatw1.insert(END,0)
     else:
          flatw.insert(END,int(k)-1)

def mocha():
     k = mocha.get("1.0",END)
     mocha.delete("1.0",END)
     mocha.insert(END,int(k) + 1)

def sub4():
     k = mocha.get("1.0",END)
     mocha.delete("1.0",END)
     if(int(k)) == 0:
          mocha1.insert(END,0)
     else:
          mocha.insert(END,int(k)-1)

def irishcoffee():
    k = irishc.get("1.0",END)
    irishc.delete("1.0",END)
    irishc.insert(END,int(k) + 1)

def sub5():
     k = irishc.get("1.0",END)
     irishc.delete("1.0",END)
     if(int(k)) == 0:
          irishc1.insert(END,0)
     else:
          irishc.insert(END,int(k)-1)

def macchiano():
     k = macch.get("1.0",END)
     macch.delete("1.0",END)
     macch.insert(END,int(k) + 1)

def sub6():
     k = macch.get("1.0",END)
     macch.delete("1.0",END)
     if(int(k)) == 0:
          macch1.insert(END,0)
     else:
          macch.insert(END,int(k)-1)

def latteaulait():
     k = aulait.get("1.0",END)
     aulait.delete("1.0",END)
     aulait.insert(END,int(k) + 1)

def sub7():
     k = aulait.get("1.0",END)
     aulait.delete("1.0",END)
     if(int(k)) == 0:
          aulait1.insert(END,0)
     else:
          aulait.insert(END,int(k)-1)

def affogato():
     k = affo.get("1.0",END)
     affo.delete("1.0",END)
     affo.insert(END,int(k) + 1)

def sub8():
     k = affo.get("1.0",END)
     affo.delete("1.0",END)
     if(int(k)) == 0:
          affo1.insert(END,0)
     else:
          affo.insert(END,int(k)-1)

def total():
    qty1 = int(cap.get("0.0", END))
    qty2 = int(bcoff.get("0.0", END))
    qty3 = int(flatw.get("0.0", END))
    qty4 = int(mocha.get("0.0", END))
    qty5 = int(irishc.get("0.0", END))
    qty6 = int(macch.get("0.0", END))
    qty7 = int(aulait.get("0.0", END))
    qty8 = int(affo.get("0.0", END))
    c1, c2, c3, c4, c5, c6, c7, c8 = 50, 60, 80, 100, 80, 90, 110, 120
    tot1 = qty1 * c1
    tot2 = qty2 * c2
    tot3 = qty3 * c3
    tot4 = qty4 * c4
    tot5 = qty5 * c5
    tot6 = qty6 * c6
    tot7 = qty7 * c7
    tot8 = qty8 * c8

    total_cost = tot1 + tot2 + tot3 + tot4 + tot5 + tot6 + tot7 + tot8
    a = total_cost
    b = (a * 5) / 100
    total_bill = total_cost + b
    totalis.delete("1.0",END)
    totalis.insert(END,str(total_bill))

label1 = Label(finproj,text="Cappuccino",bg="sky blue",font="arial 8")
label1.place(x=83,y=130)
label2 = Label(finproj,text="Black Coffee",bg="sky blue",font="arial 8")
label2.place(x=80,y=230)
label3 = Label(finproj,text="Flat White",bg="sky blue",font="arial 8")
label3.place(x=87,y=330)
label4 = Label(finproj,text="Mocha",bg="sky blue",font="arial 8")
label4.place(x=107,y=430)
label5 = Label(finproj,text="Irish COffee",bg="sky blue",font="arial 8")
label5.place(x=80,y=530)
label6 = Label(finproj,text="Macchiato",bg="sky blue",font="arial 8")
label6.place(x=932,y=130)
label7 = Label(finproj,text="Latte Au Lait",bg="sky blue",font="arial 8")
label7.place(x=920,y=230)
label8 = Label(finproj,text="Affogato",bg="sky blue",font="arial 8")
label8.place(x=935,y=330)
l01 = Label(finproj,text="Cafe Home",font="algerian 35",bg="sky blue")
l01.place(x=590,y=5)
localtime=time.asctime(time.localtime(time.time()))
lblinfo = Label(font=( 'aria' ,15, ),text=localtime,fg="black",bg="sky blue",anchor=W)
lblinfo.place(x=1100,y=10)
l2 = Label(finproj,text="User Name",font="arial 15 bold",bg="sky blue")
l2.place(x=370,y=60)
username = Entry(finproj,width=30,relief="sunken")
username.place(x=520,y=60)
l3 = Label(finproj,text="Contact no.",font="arial 15 bold",bg="sky blue")
l3.place(x=720,y=60)
phno = Entry(finproj,width=25,relief=SUNKEN)
phno.place(x=870,y=60)

image1 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image1.png")
image11=image1.subsample(7,7)
imgbut1 = Button(finproj,image=image11,width=80,height=80,bg="white",activebackground="white",relief="raised",command=capuchino)
imgbut1.place(x=155,y=100)
cap = Text(finproj,width=5,font="arial",height=1,relief="sunken")
cap.insert(END,0)
cap.place(x=265,y=135)
but1 = Button(finproj,font="arial 15",text="-",width=5,bg="orange",relief="raised",activebackground="orange",command=sub1)
but1.place(x=340,y=126)

image2 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image2.png")
image12=image2.subsample(18,18)
imgbut2 = Button(finproj,image=image12,width=80,height=80,bg="white",activebackground="white",relief="raised",command=blackcoffee)
imgbut2.place(x=155,y=200)
bcoff = Text(finproj,width=5,height=1,font="arial",relief="sunken")
bcoff.insert(END,0)
bcoff.place(x=265,y=230)
but2 = Button(finproj,font="arial 15",text="-",width=5,height=1,bg="orange",relief="raised",activebackground="orange",command=sub2)
but2.place(x=340,y=220)

image3 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image3.png")
image13=image3.subsample(87,87)
imgbut3 = Button(finproj,image=image13,width=80,height=80,bg="white",activebackground="white",relief="raised",command=flatwhite)
imgbut3.place(x=155,y=300)
flatw = Text(finproj,width=5,height=1,font="arial",relief="sunken")
flatw.insert(END,0)
flatw.place(x=265,y=330)
but3 = Button(finproj,font="arial 15",text="-",width=5,height=1,bg="orange",relief="raised",activebackground="orange",command=sub3)
but3.place(x=340,y=318)

image4 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image4.png")
image14=image4.subsample(10,10)
imgbut4 = Button(finproj,image=image14,width=80,height=80,bg="white",activebackground="white",relief="raised",command=mocha)
imgbut4.place(x=155,y=400)
mocha = Text(finproj,width=5,height=1,font="arial",relief="sunken")
mocha.insert(END,0)
mocha.place(x=265,y=430)
but4 = Button(finproj,font="arial 15",text="-",width=5,height=1,bg="orange",relief="raised",activebackground="orange",command=sub4)
but4.place(x=340,y=420)

image5 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image5.png")
image15=image5.subsample(5,5)
imgbut5 = Button(finproj,image=image15,width=80,height=80,bg="white",activebackground="white",relief="raised",command=irishcoffee)
imgbut5.place(x=155,y=500)
irishc = Text(finproj,width=5,height=1,font="arial",relief="sunken")
irishc.insert(END,0)
irishc.place(x=265,y=522)
but5 = Button(finproj,font="arial 15",text="-",width=5,height=1,bg="orange",relief="raised",activebackground="orange",command=sub5)
but5.place(x=340,y=512)

image6 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image6.png")
image16=image6.subsample(7,7)
imgbut6 = Button(finproj,image=image16,width=80,height=80,bg="white",activebackground="white",relief="raised",command=macchiano)
imgbut6.place(x=1000,y=100)
macch = Text(finproj,width=5,height=1,font="arial",relief="sunken")
macch.insert(END,0)
macch.place(x=1110,y=135)
but6 = Button(finproj,font="arial 15",text="-",width=5,bg="orange",relief="raised",activebackground="orange",command=sub6)
but6.place(x=1185,y=126)

image7 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image7.png")
image17=image7.subsample(9,9)
imgbut7 = Button(finproj,image=image17,width=80,height=80,bg="white",activebackground="white",relief="raised",command=latteaulait)
imgbut7.place(x=1000,y=200)
aulait = Text(finproj,width=5,height=1,font="arial",relief="sunken")
aulait.insert(END,0)
aulait.place(x=1110,y=230)
but7 = Button(finproj,font="arial 15",text="-",width=5,height=1,bg="orange",relief="raised",activebackground="orange",command=sub7)
but7.place(x=1185,y=220)

image8 = PhotoImage(file="C:/Users/DBLPC11/Desktop/Prashant/image8.png")
image18=image8.subsample(5,5)
imgbut8 = Button(finproj,image=image18,width=80,height=80,bg="white",activebackground="white",relief="raised",command=affogato)
imgbut8.place(x=1000,y=300)
affo = Text(finproj,width=5,height=1,font="arial",relief="sunken")
affo.insert(END,0)
affo.place(x=1110,y=330)
but8 = Button(finproj,font="arial 15",text="-",width=5,height=1,bg="orange",relief="raised",activebackground="orange",command=sub8)
but8.place(x=1185,y=318)

bill_but = Button(finproj,text="Bill",bg="brown",fg="white",font="arial 20",width=8,relief="raised",activebackground="brown",command=billbutton)
bill_but.place(x=645,y=600)

tot_but = Button(finproj,font="arial 17 bold",text="Total",command=total,fg="light yellow",bg="green",activebackground="green")
tot_but.place(x=625,y=672)

totalis = Text(font="arial",width=8,height=1,relief="sunken")
totalis.place(x=737,y=685)

metext=Entry(finproj,font=("Courier New",12,'bold'),textvar=textin,width=32,bd=5,bg='powder blue')
metext.place(x=540,y=110)

but1=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=540,y=140)

but2=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=540,y=210)

but3=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=540,y=280)

but4=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=605,y=140)

but5=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=605,y=210)

but6=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=605,y=280)

but7=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=670,y=140)

but8=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=670,y=210)

but9=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=670,y=280)

but0=Button(finproj,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=540,y=350)

butdot=Button(finproj,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=605,y=350)

butpl=Button(finproj,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=735,y=140)

butsub=Button(finproj,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=735,y=210)

butml=Button(finproj,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=735,y=280)

butdiv=Button(finproj,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=735,y=350)

butclear=Button(finproj,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=800,y=140)

butequal=Button(finproj,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=540,y=420)

name = username.get()
phone_no = phno.get()

finproj.mainloop()
