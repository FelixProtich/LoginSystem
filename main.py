from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1200x600+100+50")
        self.root.resizable(False, False)

        # Background image
        self.bg = ImageTk.PhotoImage(file="Screen.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame_login = Frame(self.root, bg="#6867FF")
        frame_login.place(x=350, y=150, width=500, height=400)

        # title & subtitle
        title = Label(frame_login, text="WE ARE PROTECH ", font=("Impact", "25", "bold"), fg="blue", bg="#6667FF").place(
            x=80, y=10)
        title = Label(frame_login, text="Member Login", font=("Goudy old style", "20", "bold"), fg="#1d1d1d",
                      bg="#6667FF").place(x=100, y=60)

        # Username
        lbl_username = Label(frame_login, text="Username", font=("Goudy old style", "20", "bold"), fg="purple",
                             bg="#6667FF").place(x=100, y=100)
        self.username = Entry(frame_login, font=("Goudy old style", "16"), bg="#E7E6E6")
        self.username.place(x=100, y=130, height=35, width=250)

        # Password
        lbl_password = Label(frame_login, text="Password", font=("Goudy old style", "20", "bold"), fg="purple",
                             bg="#6667FF").place(x=100, y=180)
        self.password = Entry(frame_login, font=("Goudy old style", "16"), bg="#E7E6E6")
        self.password.place(x=100, y=220, height=35, width=250)

        # Button
        forget = Button(frame_login, text="Forgot Password?", bd=0, cursor="hand2", font=("Goudy old style", "12",),
                        fg="#000000", bg="#6867FF").place(x=100, y=260)
        submit = Button(frame_login, command=self.check_function, cursor="hand2", text="Login", bd=0,
                        font=("Goudy old style", "16",), bg="#9400D3", fg="white").place(x=250, y=300, width=150,
                                                                                         height=40)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Username and Password required", parent=self.root)
        elif self.username.get() != "FelixProtich" or self.password.get() != "1234":
            messagebox.showerror("Error", "Incorrect Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")


root = Tk()
obj = Login(root)
root.mainloop()
