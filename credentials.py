import tkinter as tk
from tkinter import *


class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enter your LinkedIn login")
        self.root.geometry('600x300')
        self.root.configure(background='black')

        self.frame_1 = Frame(self.root, bg="white")
        self.frame_1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

        # Campos de entrada
        Label(self.frame_1, text="E-mail:").place(relx=0.1, rely=0.2)
        self.entry_email = Entry(self.frame_1)
        self.entry_email.place(relx=0.25, rely=0.2, relwidth=0.7, relheight=0.15)

        Label(self.frame_1, text="Password:").place(relx=0.1, rely=0.4)
        self.entry_pass = Entry(self.frame_1, show="*")
        self.entry_pass.place(relx=0.25, rely=0.4, relwidth=0.7, relheight=0.15)

        Button(self.frame_1, text="Ok", command=self.save_login).place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.15)

        # Variáveis de retorno
        self.email = None
        self.password = None

    def save_login(self):
        """Salva e fecha a janela"""
        self.email = self.entry_email.get()
        self.password = self.entry_pass.get()
        self.root.destroy()

    def get_login(self):
        """Executa a janela e retorna login e senha"""
        self.root.mainloop()
        return self.email, self.password