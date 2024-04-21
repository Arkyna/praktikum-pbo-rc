import tkinter
from tkinter import messagebox

class LoginApp:
    USERNAME = "admin"
    PASSWORD = "12345"
    registered_accounts = {}

    def __init__(self, Winlog):
        self.Winlog = Winlog
        self.Winlog.title("Login")
        self.Winlog.minsize(250, 140)

        self.usernameLabel = tkinter.Label(Winlog, text="Username : ")
        self.usernameLabel.grid(row=0, column=0, sticky="ew")

        self.usernameEntry = tkinter.Entry(Winlog)
        self.usernameEntry.grid(row=0, column=1, sticky="ew")

        self.passwordLabel = tkinter.Label(Winlog, text="Password : ")
        self.passwordLabel.grid(row=1, column=0, sticky="ew")

        self.passwordEntry = tkinter.Entry(Winlog, show="*")
        self.passwordEntry.grid(row=1, column=1, sticky="ew")

        self.loginButton = tkinter.Button(Winlog, text="Login", command=self.checkLogin)
        self.loginButton.grid(row=2, column=1, sticky="ew", pady=5)

        self.registButton = tkinter.Button(Winlog, text="Register", command=self.openWinregis)
        self.registButton.grid(row=3, column=1, sticky="ew", pady=5)

    def showSuccessDialog(self, username):
        messagebox.showinfo("Login Ouput", f"Welcome, {username}!")

    def showErrorDialog(self):
        messagebox.showerror("Login Ouput", "Failed to Login")

    def checkLogin(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username == self.USERNAME and password == self.PASSWORD:
            self.showSuccessDialog(username)
        else:
            self.showErrorDialog()

    def openWinregis(self):
        register_window = RegistApp(self.Winlog)

    def registerAccount(self, username, password):
        if username not in self.registered_accounts:
            self.registered_accounts[username] = password
            messagebox.showinfo("Registration Ouput", "Account registered")
        else:
            messagebox.showerror("Registration Ouput", "Username already exists!")

class RegistApp:
    def __init__(self, Winlog):
        self.WinregWindow = tkinter.Toplevel(Winlog)
        self.WinregWindow.title("Register")
        self.WinregWindow.minsize(250, 140)

        self.usernameLabel = tkinter.Label(self.WinregWindow, text="Username : ")
        self.usernameLabel.grid(row=0, column=0, sticky="ew")

        self.usernameEntry = tkinter.Entry(self.WinregWindow)
        self.usernameEntry.grid(row=0, column=1, sticky="ew")

        self.passwordLabel = tkinter.Label(self.WinregWindow, text="Password : ")
        self.passwordLabel.grid(row=1, column=0, sticky="ew")

        self.passwordEntry = tkinter.Entry(self.WinregWindow, show="*")
        self.passwordEntry.grid(row=1, column=1, sticky="ew")

        self.registerButton = tkinter.Button(self.WinregWindow, text="Register", command=self.registerAccount)
        self.registerButton.grid(row=2, column=1, sticky="ew", pady=5)

    def registerAccount(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        app.registerAccount(username, password)
        self.WinregWindow.destroy()

Winlog = tkinter.Tk()
app = LoginApp(Winlog)
Winlog.mainloop()