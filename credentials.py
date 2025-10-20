import tkinter as tk
from tkinter import *


class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enter your LinkedIn login")
        self.root.geometry('600x400')
        self.root.configure(background='black')

        self.frame_1 = Frame(self.root, bg="white")
        self.frame_1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        # Campos de entrada
        Label(self.frame_1, text="E-mail:").place(relx=0.1, rely=0.1)
        self.entry_email = Entry(self.frame_1)
        self.entry_email.place(relx=0.2, rely=0.1, relwidth=0.7, relheight=0.1)

        Label(self.frame_1, text="Password:").place(relx=0.1, rely=0.3)
        self.entry_pass = Entry(self.frame_1, show="*")
        self.entry_pass.place(relx=0.2, rely=0.3, relwidth=0.7, relheight=0.1)

        Label(self.frame_1, text="Position:").place(relx=0.1, rely=0.5)
        self.entry_position = Entry(self.frame_1)
        self.entry_position.place(relx=0.2, rely=0.5, relwidth=0.7, relheight=0.1)

        Label(self.frame_1, text="City:").place(relx=0.1, rely=0.7)
        self.entry_city = Entry(self.frame_1)
        self.entry_city.place(relx=0.2, rely=0.7, relwidth=0.7, relheight=0.1)

        Button(self.frame_1, text="Ok", command=self.save_login).place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.1)

        # Variáveis de retorno
        self.email = None
        self.password = None
        self.position = None
        self.city = None

    def save_login(self):
        """Salva e fecha a janela"""
        self.email = self.entry_email.get()
        self.password = self.entry_pass.get()
        self.position = self.entry_position.get()
        self.city = self.entry_city.get()
        self.root.destroy()

    def get_login(self):
        """Executa a janela e retorna login e senha"""
        self.root.mainloop()
        return self.email, self.password, self.position, self.city