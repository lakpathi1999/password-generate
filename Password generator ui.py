#Importing tkinter for the graphical user interface
#Filedialog to allow browsing the file and getting the directory
#Random to randomly select the list of characters in an array
#Array import to store letters
from tkinter import *
from tkinter import filedialog
import random

import array
#Button "Click here to copy password" Calls this function
#Clears the current clipboard and then adds the password to clipboard
def copytoclip():
    root.clipboard_clear()
    root.clipboard_append(T1.get(1.0, "end-1c"))
#Button "Generate password" calls this function which then clears the textbox and pastes the newly generated password
#this generates a password depending on the values in the slider
#and then the check boxes
def Passwordgen():
    T1.delete("1.0",END)
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
 
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
 
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
              '*', '(', ')', '<']
    if((i.get()+j.get()+k.get()+l.get())==0):
        T1.insert(END,"Please select any of the checkboxes from above and click generate password ")
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    
    #Conditions for the check boxes where i,j,k,l are uppercase ,lowercase,symbols and digits respectively
    #1 means the checkboxes have been ticked and 0 means that the checkboxes is empty
    #The following condition is to ensure the random letters are from the particular array
    #And to ensure that none of the other alphabet gets into the combined list from where the final list
    #We will use the final list to randomly pick a character from it and make a password from it
    if(i.get()==1 and j.get()==1 and k.get()==1 and l.get()==1):#1111
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    elif(i.get()==1 and j.get()==1 and k.get()==1 and l.get()==0):#1110
        COMBINED_LIST =UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        temp_pass = rand_upper + rand_lower + rand_symbol
    elif(i.get()==1 and j.get()==1 and k.get()==0 and l.get()==1):#1101
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS
        temp_pass = rand_digit + rand_upper + rand_lower
    elif(i.get()==1 and j.get()==1 and k.get()==0 and l.get()==0):#1100
        COMBINED_LIST =UPCASE_CHARACTERS + LOCASE_CHARACTERS
        temp_pass = rand_upper + rand_lower
    elif(i.get()==1 and j.get()==0 and k.get()==1 and l.get()==1):#1011
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + SYMBOLS
        temp_pass = rand_digit + rand_upper +rand_symbol
    elif(i.get()==1 and j.get()==0 and k.get()==1 and l.get()==0):#1010
        COMBINED_LIST = UPCASE_CHARACTERS+ SYMBOLS
        temp_pass = rand_upper +rand_symbol
    elif(i.get()==1 and j.get()==0 and k.get()==0 and l.get()==1):#1001
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS
        temp_pass = rand_digit + rand_upper 
    elif(i.get()==1 and j.get()==0 and k.get()==0 and l.get()==0):#1000
        COMBINED_LIST =UPCASE_CHARACTERS
        temp_pass = rand_upper    
    elif(i.get()==0 and j.get()==1 and k.get()==1 and l.get()==1):#0111
        COMBINED_LIST = DIGITS +LOCASE_CHARACTERS + SYMBOLS
        temp_pass = rand_digit + rand_lower + rand_symbol
    elif(i.get()==0 and j.get()==1 and k.get()==1 and l.get()==0):#0110
        COMBINED_LIST = LOCASE_CHARACTERS + SYMBOLS
        temp_pass = rand_lower + rand_symbol
    elif(i.get()==0 and j.get()==1 and k.get()==0 and l.get()==1):#0101
        COMBINED_LIST = DIGITS + LOCASE_CHARACTERS
        temp_pass = rand_digit + rand_lower
    elif(i.get()==0 and j.get()==1 and k.get()==0 and l.get()==0):#0100
        COMBINED_LIST = LOCASE_CHARACTERS
        temp_pass = rand_lower 
    elif(i.get()==0 and j.get()==0 and k.get()==1 and l.get()==1):#0011
        COMBINED_LIST = DIGITS + SYMBOLS
        temp_pass = rand_digit + rand_symbol
    elif(i.get()==0 and j.get()==0 and k.get()==1 and l.get()==0):#0010
        COMBINED_LIST = SYMBOLS
        temp_pass = rand_symbol
    elif(i.get()==0 and j.get()==0 and k.get()==0 and l.get()==1):#0001
        COMBINED_LIST = DIGITS
        temp_pass = rand_digit

    #the condition for eliminating the extra random characters only will work if v1.get>(i.get()+j.get()+k.get()+l.get())
    #Assuming that a person presses all the check boxes and ask for a 4 letter password we will put only the temppass 
    #so that all the characters from each class appears once as the password

    if(v1.get()-(i.get()+j.get()+k.get()+l.get())==0):
        temp_pass_list=array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
        
    else:
        #For this condition we take the temp pass from each of the characters made using the rand
        #and then select more characters from the combined list
        for x in range(v1.get()-(i.get()+j.get()+k.get()+l.get())):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            #This 
            random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
    print(password)
     
    T1.insert(END,password)
#Button "Click here to save password to text file" brings up a pop up file browser
#which then asks you to select the directory of the txt file and pastes the details of the current password,username and website to the txt file

def file_input():
    filename = filedialog.asksaveasfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")),defaultextension=".txt")
    F1=open(filename,"a")
    F1.write("\n\nUSERNAME : "+T2.get(1.0, "end-1c")+"\n"+"PASSWORD : "+T1.get(1.0, "end-1c")+"\n")
    F1.close()
    L2.configure(text="The file directory is :"+filename)
    
      
 
root =Tk()
#Title of the project
root.title("Password Generator")
Label(root, text = "Password generator",font ="Times 16 bold underline",fg="red",bg="yellow").grid(row=1,column=10)
T1 = Text(root, height = 1, width = 40)#Text box for password
T2 = Text(root, height = 1, width = 40)#Text box for username

v1= IntVar()#Slider variable

Label(root, text = "Number of characters in a password",font="Times 12 bold underline").grid(row=4,column=10)
MAX_LEN = Scale( root, variable = v1, from_ = 4, to = 12, orient = HORIZONTAL)   
MAX_LEN.set(8)#Default value of the no of characters in a password is set as 8 letters
MAX_LEN.grid(row=6,column=10)#placing the slider

Label(root, text = "Variety of characters in a password",font="Times 12 bold underline").grid(row=8,column=10)#label heading for the checkboxes
i=IntVar(value=1)#By default all the checkboxes are marked as ticked
j=IntVar(value=1)
k=IntVar(value=1)
l=IntVar(value=1)
c = Checkbutton(root, text = "Uppercase letter", variable=i)
c.grid(row=10,column=10,sticky=W)#placing the Checkbox aligned from left so that all the checkboxes will be in line with each other
d = Checkbutton(root, text = "Lowercase letter", variable=j)
d.grid(row=10,column=11,sticky=W)#placing the Checkbox aligned from left so that all the checkboxes will be in line with each other
e = Checkbutton(root, text = "Symbols", variable=k)
e.grid(row=12,column=10,sticky=W)#placing the Checkbox aligned from left so that all the checkboxes will be in line with each other
f = Checkbutton(root, text = "Numbers", variable=l)
f.grid(row=12,column=11,sticky=W)#placing the Checkbox aligned from left so that all the checkboxes will be in line with each other

Label(root, text = "ENTER USERNAME HERE\n(if you want to save to text):",font="Times 12 bold underline").grid(row=18,column=10)
T2.grid(row=19,column=10) #Textbox input for username
b = Button(root,text="Click here to generate password",fg="yellow",font="Times 16",command=Passwordgen,bg="red")
b.grid(row=21,column=10)#Button for getting the generated passwords
#it calls the function passwordgen
Label(root, text = "Password is ",font ="Times 16 bold underline",bg="yellow").grid(row=23,column=10)
T1.grid(row=26,column=10)#Textbox output for password

z = Button(root,text="Click here to copy password",fg="yellow",font="Times 16",command=copytoclip,bg="Green")
z.grid(row=29,column=10)#Button to copy the password to clipboard
#it calls the function copytoclip


y = Button(root,text="Click here to save password to text file",fg="yellow",font="Times 16",command=file_input,bg="Blue")
y.grid(row=31,column=10)#Button to copy the password,username and website name to txt file

L2=Label(root, text = "The file directory is :  ",font ="Times 16 bold underline",bg="yellow")
L2.grid(row=34,column=10)
root.geometry("500x600")
root.mainloop()
