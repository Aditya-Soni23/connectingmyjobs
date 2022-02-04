from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.geometry("900x500")


burger = ImageTk.PhotoImage(Image.open("image1.png"))
burger_image = Label(root)
burger_image["image"]=burger
burger_image.place(relx =0.7, rely = 0.5, anchor = CENTER )

label_heading = Label(root,text="JOBS", font = ("times",40,"bold"), fg = "Orange")
label_heading.place(relx = 0.12, rely = 0.1,anchor=CENTER)


entry_doctor = Entry(root)
entry_doctor.place(relx=0.25, rely=0.20,anchor=CENTER)

entry_IT = Entry(root)
entry_IT.place(relx=0.25, rely=0.45,anchor=CENTER)

entry_chemical = Entry(root)
entry_chemical.place(relx=0.25, rely=0.75,anchor=CENTER)


label_selected_doctor=Label(root)
label_selected_doctor.place(relx=0.01, rely=0.3,anchor=W)
label_selected_IT=Label(root)
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)
label_selected_chemical=Label(root)
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)


class parent():
    def __init__(self):
        print("This is parent class")
        
        
    def doctor(doctor_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor['text'] = doctor_name+" has been alloted to "+hospital_list[random_hospital]
        
        
    def softwareEngineer(it_professional_name):
        IT_company_list = ["I code", "Web Access", "Dotcom Services", "ATOS"]
        random_IT_company = random.randint(0,3) 
        label_selected_IT['text'] = it_professional_name+" has been alloted to "+IT_company_list[random_IT_company]
        
       
    def chemical_engineer(chemical_engineer_name):
        company_list = ["chemecologist","checmials","chemicobottles","chemiexperiments"]
        random_company = random.randint(0,3)
        label_selected_chemical['text'] = chemical_engineer_name+" has been alloted to "+company_list[random_company] 
        
        
class child1(parent):
    def __init__(self):
        print("This is child1 class")
    def getDoctor(self):
        name = entry_doctor.get()
        parent.doctor(name)
        
class child2(parent):
    def __init__(self):
        print("This is child2 class")
    def getIT(self):
        name = entry_IT.get()
        parent.softwareEngineer(name) 


class child3(parent):
 
    def __init__(self):
        print("This is child3 class")
  
    def getChemical(self):
        name = entry_chemical.get()
        parent.chemical_engineer(name)
        
obj1 = child1()
obj2 = child2()
obj3 = child3()
btn_doctor = Button(root, text="Show the hospital alloted", command=obj1.getDoctor)
btn_doctor.place(relx=0.1, rely=0.23,anchor=CENTER)
btn_it = Button(root, text="Show the IT company alloted", command=obj2.getIT)
btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)
btn_chemical = Button(root, text="Show the chemical company alloted", command=obj3.getChemical)
btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)
root.mainloop()