from tkinter import *
def red():
    Label(details, text="age",bg='red').grid(row=1,column=0, sticky=W)
def getdetail():
    
    f= open("temp.txt","w+")
    f.write(name.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write(age.get())
    f.close()
    f=open("temp.txt","a+")
    f.write("\n")
    f.close()
    f=open("temp.txt","a+")
    f.write( sex.get())
    f.close()
def green():
    Label(details, text="age",bg='white').grid(row=1,column=0, sticky=W)
    WSignUp1= Button(details, text="Save ", command=getdetail).grid(row=3, column=4, sticky=W)
    WSignUp1= Button(details, text="Done ", command=quit).grid(row=3, column=5, sticky=W)
def checkage():
    j=str(age.get())
    if(len(j)==2):
        for i in range(len(j)):
            if(j[i] not in ['1','2','3','4','5','6','7','8','9','0']):
                a=red()
                break;
            else:
                a=green()
    else:
        z=red()
details=Tk()
details.title('Details of Patient')
name =StringVar()
age=StringVar()
sex=StringVar()
Label(details, text="name").grid(row=0, sticky=W)  #label
Entry(details, textvariable =name).grid(row=0, column=1, sticky=E) #entry textbox
Label(details, text="Age").grid(row=1,column=0, sticky=W)  #label
Entry(details, textvariable = age).grid(row=1, column=1, sticky=E) #entry textbox
Label(details, text="Sex").grid(row=2,column=0, sticky=W)  #label
Entry(details, textvariable = sex).grid(row=2, column=1, sticky=E) #entry textbox
WSignUp3= Button(details, text="Check", command =checkage).grid(row=3, column=0, sticky=W)
details.mainloop()

