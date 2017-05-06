from tkinter import *   # I imported a module called Tkinter alongside all it's classes
#import csv


from GUI_Classes import *





root = Tk()
root.geometry("1000x500")



theLabel = Label(root, bg= 'white',fg= 'blue', text="Damilola Aluko GUI",font = ('Arial',25))

theLabel.grid(column=1)





label = Label(root, text = 'File name',font = ('Arial', 14),fg='green')
button = Button(root,text = 'Enter',fg='purple',command=getData)

question1 = Label(root, text = ' Question 1. The average value of the numbers in the field [height] in the range (33) and (53) inclusive')
buttonQ1 = Button(root, text = 'click', fg='green')

question2 = Label(root,text = ' Question 2. The values in the code field do not match the format X*XX[9]XXX')
buttonQ2  = Button (root, text = 'click', fg='green')

question3 = Label(root,text = ' Question 3. The numbers that lie in the field [distance] between (44.180) and (79.061) inclusive')
buttonQ3 = Button(root, text = 'click', fg='green')

question4 = Label(root,text = ' Question 4. Count the number of (Cold) in the field [val]')
buttonQ4 = Button (root, text = 'click', fg='green')

question5 = Label(root,text = 'Quesion 5.The percentage of strings have the value (Director) in the field [role]')
buttonQ5 = Button (root, text = 'click', fg= 'green')

question6 = Label (root,text = 'Question 6. The sum of the numbers in field [tonnes] between (5334) and (8233) inclusive')
buttonQ6 = Button (root,text = 'click', fg= 'green')

question7 = Label(root,text = 'Quesion 7. The lines where tonnes is less than 7780  *or* distance is more than 59.097')
buttonQ7= Button (root,text = 'click', fg='green')
        





entry_1 = Entry(root)


label.grid(row=5,sticky=E)
button.grid(row=6,column=2)

question1.grid(row=20,sticky=E)
buttonQ1.grid(row=23,column=2)


question2.grid(row=25,sticky=E)
buttonQ2.grid(row=27,column=2)

question3.grid(row=30,sticky=E)
buttonQ3.grid(row=32,column=2)

question4.grid(row=35,sticky=E)
buttonQ4.grid(row=37, column=2)

question5.grid(row=40,sticky=E)
buttonQ5.grid(row=42,column=2)

question6.grid(row=45,sticky=E)
buttonQ6.grid(row=47,column=2)

question7.grid(row=50,sticky=E)
buttonQ7.grid(row=52,column=2)








entryQ1 =Entry(root)
entryQ2=Entry(root)
entryQ3=Entry(root)
entryQ4=Entry(root)
entryQ5=Entry(root)
entryQ6=Entry(root)
entryQ7=Entry(root)





entry_1.grid(row=5,column=1)
entryQ1.grid(row=20,column=1)
entryQ2.grid(row=25,column=1)
entryQ3.grid(row=30,column=1)
entryQ4.grid(row=35,column=1)
entryQ5.grid(row=40,column=1)
entryQ6.grid(row=45,column=1)
entryQ7.grid(row=50,column=1)





        
        

    #check = Checkbutton(root, text = 'keep me signed in')
    #check.grid(columnspan=1)

 
root.mainloop()

