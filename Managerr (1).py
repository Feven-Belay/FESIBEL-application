#importing important built-ins in tkinter
import tkinter as tk
from tkinter import messagebox
import random
global window
from tkinter import*


class users:
    '''class to represent users'''
    #constructor
    def __init__(self,user_prof_name = '',user_birthdate="",user_location= ''):
        self.user_prof_name = user_prof_name
        self.user_birthdate = user_birthdate
        self.user_location= user_location
    #setter and getter
    def set_user_prof_name(self, name):
        self.user_prof_name = name

    def get_user_prof_name(self):
        return self.user_prof_name

    def set_user_birthdate(self, date):
        self.user_birthdate = date

    def get_user_birthdate(self):
        return self.user_birthdate

    def set_user_location(self, location):
        self.user_location = location
    def get_user_location(self):
        return self.user_location

    #display function
    def __str__(self):
        return "Name:{},\nBirthday:{},\nLocation".format(self.get_user_prof_name(),self.get_user_birthdate(),self.get_user_location())

class Manager:
    '''This class represents Manager'''
    #constructor
    def __init__(self):
        self.usersFilename=""
        self.postsFilename=""

     #setter and getter
    def setusersFilename(self,usersFilename):
        self.usersFilename=usersFilename
    def getusersFilename(self):
        return self.usersFilename

    def setpostsFilename(self,postsFilename):
        self.postsFilename=postsFilename
    def getpostsFilename(self):
        return self.postsFilename

    #function that creates main window
    def user(self):
    #creating GUI window
        window3 = Tk()
        window3.geometry("400x500")  #setting length and width of the window
        window3.configure(background='ivory') #setting the background color
        #validating if the user has entered all his information
        try:
            #designing the level user registation
            pagename = tk.Label(window3, text="USER REGISTRATION",bg='ivory',fg='Maroon', font=("bold",30))
            pagename.pack()
            #setting window title
            window3.title("User Register")
            #fullname level
            fullnametext = tk.Label(window3, text="Enter your Fullname",bg='ivory')
            #full name entry
            self.fullname = tk.Entry(window3)
            fullnametext.pack()
            self.fullname.pack()
            usertext = tk.Label(window3, text="Enter your username",bg='ivory')  #username label
            self.username = tk.Entry(window3) #username entry
            usertext.pack()
            self.username.pack()
            passwordtext = tk.Label(window3, text="Enter your password",bg='ivory') #password label
            self.password = tk.Entry(window3) #password entry
            self.password.config(show="*") #showing password in * formart
            passwordtext.pack()
            self.password.pack()
            emailtext = tk.Label(window3, text="Enter your Email",bg='ivory') #email label
            self.email = tk.Entry(window3) #email entry
            emailtext.pack()
            self.email.pack()
            teletext = tk.Label(window3, text="Enter your Telephone number",bg='ivory') #tele number label
            self.telephone = tk.Entry(window3) #number entry
            teletext.pack()
            self.telephone.pack()
            addtext = tk.Label(window3, text="Enter your Address",bg='ivory') #address label
            self.Address = tk.Entry(window3) #address entry
            addtext.pack()
            self.Address.pack()
            addtext = tk.Label(window3, text="Enter your Date of birth",bg='ivory')#DOB label
            self.DOB = tk.Entry(window3) #DOB entry
            addtext.pack()
            self.DOB.pack()
            addtext = tk.Label(window3, text="Enter your bio",bg='ivory')#bio label
            self.bio = tk.Entry(window3) #entry bio
            addtext.pack()
            self.bio.pack()

        except ValueError:
            raise ValueError("Enter a valid input")
        #regster button
        self.button = tk.Button(window3,text="register", width=5, height=2, command=self.validate)
        self.button.pack()
    #validating function if all info is filled
    def validate(self):
        if ( self.username.get() == "" or self.password.get() == "" or  self.fullname.get()== "" or  self.email.get() =="" or self.Address.get() =="" ):
            messagebox.showinfo("" ,"Blank Not Allowed ")

        else:
            self.registerfile()
    #function to register in a file
    def registerfile(self):
        #creating tkinter another window
        window3 = Tk()
        #accepting username entry
        user = self.username.get()
        #accepting password entry
        passw = self.password.get()
        #accepting fullname entry
        full = self.fullname.get()
        #accepting address entry
        addr = self.Address.get()
        #accepting email entry
        email = self.email.get()
        #accepting telephone number entry
        tele = self.telephone.get()
        #accepting DOB entry
        DOB = self.DOB.get()
        #accepting bio entry
        bio = self.bio.get()

        #opening and writing username and password into a file
        file = open("Web_user", "a")
        file.write(user)
        file.write(",")
        file.write(passw + "\n")
        #closing the file
        file.close()

        #opening and writing user sign in info into a file
        file1 = open("records", "a")
        file1.write(user)
        file1.write(",")
        file1.write(passw)
        file1.write(",")
        file1.write(full)
        file1.write(",")
        file1.write(email)
        file1.write(",")
        file1.write(addr)
        file1.write(",")
        file1.write(tele)
        file1.write(",")
        file1.write(DOB)
        file1.write(",")
        file1.write(bio)
        file1.write(",")
        file1.write("\n")
        file1.close()

        #opening the file
        file = open("Web_user", "a")

        #writing into the file
        file.write(user)
        file.write(",")
        file.write(passw + "\n")
        file.close()

        #to clear the entry in the regster file
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.fullname.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.Address.delete(0, tk.END)
        self.telephone.delete(0, tk.END)
        self.DOB.delete(0, tk.END)
        self.bio.delete(0, tk.END)

        #creating the label after succefully regstering
        self.success = tk.Label(window3, text="You have successfully registered", fg="green")
        self.success.pack()

    #function for the log in window
    def userlogin(self):
        #creating tkinter window
        window7= Tk()
        #setting length and width of the window
        window7.geometry("400x500")
        #setting title of the window
        window7.title("Fesibel")
        #setting backgroung colour of the window
        window7.configure(background='ivory')
        #label for the user name
        usertext = tk.Label(window7, text="Enter your username",bg='ivory')
        #entry for username
        self.username = tk.Entry(window7)
        #setting size of the button
        usertext.pack(ipadx=15, ipady=15)
        self.username.pack()
        passwordtext = tk.Label(window7, text="Enter your password",bg='ivory')
        self.password = tk.Entry(window7)
        self.password.config(show="*")
        #setting size of password text
        passwordtext.pack(ipadx=15, ipady=15)
        self.password.pack()
        #setting button login
        self.button = tk.Button(window7, text="login", width=5, height=2, command=self.validatelogin)
        self.button.pack(ipadx=15, ipady=4)
        self.button.pack(padx = 80, pady = 70)

    #function to validate entered info
    def validatelogin(self):
        #opening the file and reading from it
        with open('Web_user', 'r') as file:
            user = self.username.get()
            passw = self.password.get()

            #accessing and reading from each line
            if ((user + "," + passw + "\n") in file.readlines()):

                self.logedin()
            #if nothing is entered
            elif (user == "" or passw== ""):
                messagebox.showinfo("",
                                  "Log in failed ,Username or Password is empty ")
            #if wrong info is entered
            else:
                messagebox.showinfo("",
                                    "Log in failed ,Username or Password is wrong ")

    #function to display the window when user logs in
    def logedin(self):
        window9 = tk.Toplevel()
        window9.geometry("400x500")
        window9.title("Fesibel")
        window9.configure(background='ivory')
        #creating button
        userbut1= tk.Button(window9, text="User Details", width=25, height=2, command=self.detail)
        userbut1.pack(ipadx=20, ipady=4,padx=50,pady=20)

        # creating button
        userbut2 = tk.Button(window9, text="Check your followers", width=25, height=2,command=self.Followers)
        userbut2.pack(ipadx=20, ipady=4,padx=55,pady=22)

        # creating button
        userbut3 = tk.Button(window9, text="Check your posts", width=25, height=2 ,command=self.Posts)
        userbut3.pack(ipadx=20, ipady=4,padx=58,pady=24)
        userbut4 = tk.Button(window9, text="Add post", width=25, height=2, command=self.Post)
        userbut4.pack(ipadx=20, ipady=4, padx=80, pady=26)

        # creating button
        userbut5 = tk.Button(window9, text="Add Follower", width=25, height=2, command=self.follower)
        userbut5.pack(ipadx=20, ipady=4, padx=90, pady=28)

    #function to display details
    def detail(self):
        #opening in a new window
        windoww = tk.Toplevel()
        windoww.geometry("400x500")
        windoww.title("Dashboard")
        pagename = tk.Label(windoww, text="Details", bg='ivory', fg='Maroon', font=("bold",25))
        user = self.username.get()
        file = open("records", "r")
        #accesing each line
        for line in file:
            #spliting the words with string
            currentline = line.split(",")
            if user == currentline[0]:
                user = currentline[0]
                passw = currentline[1]
                Namee = currentline[2]
                email = currentline[3]
                address = currentline[4]
                Tele = currentline[5]
                DOB = currentline[6]
                Bio = currentline[7]
                #making them appear in a window
                yourinfo = tk.Label(windoww, text="Username" + "  " + user + "\n"
                                                  + "Password " + "  " + passw + "\n" + "Name "+ " " + Namee + "\n"
                                                  + "Email " + " " + email +  "\n" + "Address   " + address + "\n" + "Tele   " + Tele + "\n" + "Date of birth   " + DOB + "\n" + "Biography   " + Bio)
                yourinfo.pack()

    #function for displaying following
    def Followers(self):
        windoww = tk.Toplevel()
        windoww.geometry("400x500")
        windoww.title("Dashboard")
        user = self.username.get()
        file=open("followers.txt","r")
        for line in file:
            currentline = line.split(",")
            if user == currentline[0]:
                    user=currentline[0]
                    Fol1 = currentline[1]
                    Fol2=currentline[2]
                    Fol3 = currentline[3]
                    Fol4=currentline[4]

                    #displaing the folowers
                    yourinfo = tk.Label(windoww,text="Fol1 " + Fol1 + "\n"
                        + "Fol2" + Fol2 + "\n"+ "Fol3"+ Fol3 + "\n"
                                           + "Fol4 " + Fol4)
                    yourinfo.pack()
    #function to display from a file by readinng from the file
    def Posts(self):
        windoww = tk.Toplevel()
        windoww.geometry("400x500")
        windoww.title("Dashboard")
        user = self.username.get()
        file=open("Posts.txt","r")
        for line in file:
            currentline = line.split(",")
            if user == currentline[0]:
                    user=currentline[0]
                    date = currentline[1]
                    view=currentline[2]
                    like= currentline[3]
                    type=currentline[4]
                    #displaying post details
                    yourinfo = tk.Label(windoww,text="Post date " + date + "\n"
                        + "view" + view + "\n"+ "Like"+ like+ "\n"
                                           + "Post type" + type)
                    yourinfo.pack()



    #function to add followers
    def follower(self):
        window11 = Tk()
        window11.geometry("400x500")
        window11.configure(background='ivory')

        pagename = tk.Label(window11, text="ADD followers",bg='ivory',fg='Maroon', font=("bold",30))
        pagename.pack()
        window11.title("User Register")
        fol1text = tk.Label(window11, text="Enter Follwers",bg='ivory')
        self.fol1 = tk.Entry(window11)
        fol1text.pack()
        self.fol1.pack()

        fol2text = tk.Label(window11, text="Enter Follwers", bg='ivory')
        self.fol2 = tk.Entry(window11)
        fol1text.pack()
        self.fol2.pack()
        self.fol3 = tk.Entry(window11)
        fol1text.pack()
        self.fol3.pack()
        self.fol4 = tk.Entry(window11)
        fol1text.pack()
        self.fol4.pack()
        self.fol5 = tk.Entry(window11)
        fol1text.pack()
        self.fol5.pack()

        self.bu = tk.Button(window11, text="Add", width=5, height=2, command=self.validated)
        self.bu.pack()
        self.followerfile()

    def validated(self):
        if ( self.fol1== "" or self.fol2== "" ):
            messagebox.showinfo("" ,"Blank Not Allowed ")

        else:
            self.followerfile()

    # function that contains a file that is going to appned the followers inserted by the user there
    def followerfile(self):
        window3 = Tk()
        fol1 = self.fol1.get()
        fol2=self.fol2.get()
        fol3 = self.fol3.get()
        fol4 = self.fol4.get()
        fol5 = self.fol5.get()


        file = open("followers.txt", "a")
        file.write(fol1)
        file.write(",")
        file.write(fol2)
        file.write(",")
        file.write(fol3)
        file.write(",")
        file.write(fol4)
        file.write(",")
        file.write(fol5)
        file.write(",")


        self.fol1.delete(0, tk.END)
        self.fol2.delete(0, tk.END)

        self.success = tk.Label(window3, text="Your followers are successfully added", fg="green")
        self.success.pack()

    def Post(self):
        window12 = Tk()
        window12.geometry("400x500")
        window12.configure(background='ivory')

        pagename = tk.Label(window12, text="ADD Post", bg='ivory', fg='Maroon', font=("bold", 30))
        pagename.pack()
        window12.title("User Post")
        usertext = tk.Label(window12, text="Enter username", bg='ivory')
        self.user = tk.Entry(window12)
        usertext.pack()
        self.user.pack()
        datetext = tk.Label(window12, text="Enter date", bg='ivory')
        self.date = tk.Entry(window12)
        datetext.pack()
        self.date.pack()
        datetext = tk.Label(window12, text="Enter date", bg='ivory')
        self.date = tk.Entry(window12)
        datetext.pack()
        self.date.pack()
        typetext = tk.Label(window12, text="Enter post type", bg='ivory')
        self.type = tk.Entry(window12)
        typetext.pack()
        self.type.pack()

        self.bu = tk.Button(window12, text="Add", width=5, height=2, command=self.validateed)
        self.bu.pack()
        self.postfile()

    def validateed(self):
        if (self.date == "" or self.type == ""):
            messagebox.showinfo("", "Blank Not Allowed ")

        else:
            self.postfile()

    #function that contains a file that is going to appned the details inserted by the user there
    def postfile(self):
        window3 = Tk()
        user = self.user.get()
        date = self.date.get()
        type = self.type.get()

        file = open("posts.txt", "a")
        file.write(user)
        file.write(",")
        file.write(date)
        file.write(",")
        file.write(type)
        file.write(",")

        self.user.delete(0, tk.END)
        self.date.delete(0, tk.END)
        self.type.delete(0, tk.END)

        self.success = tk.Label(window3, text="Your post is successfully added", fg="green")
        self.success.pack()

