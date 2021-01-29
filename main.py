from tkinter import filedialog as fd
from tkinter import *
import os
import csv
import smtplib
import time

global e
global w
e = ""
w = ""
SENDER = 'warnpass@gmail.com'
PASSWRD = 'schoolproject'
server = smtplib.SMTP('smtp.gmail.com', 587)
window = Tk()
window.title("Dummy Mail")
window.configure(background='LightPink1')
wordlist_path = Label(window, text="no wordlist selected", fg="red", bg='black')
emaillist_path = Label(window, text="no emaillist selected", fg="red", bg='black')

def btn(text1, c1, r1, cmd):
    buttn = Button(window, text=text1, command=cmd)
    buttn.grid(column=c1, row=r1)

def lbl(text2, c2, r2, font):
    if "no" in font:
        label = Label(window, text=text2, fg="black", bg='LightPink1')
        label.grid(column=c2, row=r2)
    else:
        label = Label(window, text=text2, fg="black", font=font, bg='LightPink1')
        label.grid(column=c2, row=r2)


def wordlist():
   wordlist = fd.askdirectory()
   #print(wordlist)
   wordlist_path.config(text=os.path.basename(wordlist))
   wordlist_path.config(fg="green")
   wrdlstpath = os.path.split(wordlist)[0] + '/' + os.path.split(wordlist)[1]
   global w 
   w = wordlist
   print(w)

def emaillist():
    emaillist = fd.askopenfilename()
    print(emaillist)
    emaillist_path.config(text=os.path.basename(emaillist))
    emaillist_path.config(fg="green")
    global e
    e = emaillist
    print(e)

def run():
    output.config(fg="green") 
    output['text'] = "> Finding Password Breaches..."
    window.update()
    print("> Running...")
    while True:
        print(e)
        print(w)
        if not e or not w:
            print("no has value")
            output['text'] = "> Invalid Entry, going to ask for emaillist and wordlist in 2 seconds..."
            window.update()
            time.sleep(3)
            emaillist()
            wordlist()
            print(e)
            print(w)
        else:
            print("has value")
            if "BreachCompilation" in w:
                    print("BreachCompilation")
                    os.system(f'h8mail -t {e} -bc {w} -sk -o temp.csv')
                    break
            elif "Collection1" in w:
                os.system(f'h8mail -t {e} -gz {w} -sk -o temp.csv')
                break
            else:
                output['text'] = "> Invalid Entry, going to ask for wordlist in 5 seconds...(make sure wordlist is BreachCompilation or Collection#1)"
                window.update()
                time.sleep(6)
                wordlist()


    output['text'] = "> Starting email server..."
    window.update()
    print("> Starting email server...")
    server.starttls()
    print("> Server started")
    output.config(text="> Logging in...")
    window.update()
    print("> Logging in...")
    server.login(SENDER, PASSWRD)
    print("> Logged in")
    with open('temp.csv', 'r') as csvf:
        csvr = csv.reader(csvf)
        next(csvr)
        for line in csvr:
            rec = line[0]
            breach = line[2]
            message = f"""Subject: CHANGE YOUR PASSWORD NOW

            PLEASE CHANGE YOUR PASSWORD FOR ALL SITE/APPS THAT USE: {breach}
            
            """
            server.sendmail(SENDER, rec, message)
            #server.sendmail(SENDER, "footit4@gmail.com", message)
            print(f"sent: {rec}, {breach}")
            output.config(text=f"sent: {rec}, {breach}")
            window.update()
            #print(line[0])
        output.config(text="> Done :-P")
        window.update()

#Start Here
lbl(":-P Dummy Mail :-P", 2, 0, 'Helvetica 20 bold')

btn("WordList Directory", 0, 1,  wordlist)
wordlist_path.grid(column=0, row=2)

btn("EmailList Directory", 3, 1,  emaillist)
emaillist_path.grid(column=3, row=2)

btn("Run", 2, 3, run)
output = Label(window, text="When ready press run", fg="DarkGoldenrod2", bg="black")
output.grid(column=2, row=4)

#Loop finished
window.mainloop()
