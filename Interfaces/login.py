import tkinter as tk
from tkinter import messagebox
from db_connection import connect
from menu import Menu  # Asegúrate de importar Menu

class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="ID Cliente:").pack(pady=10)
        self.id_cliente_entry  = tk.Entry(self)
        self.id_cliente_entry.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(pady=10)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Ingresar", command=self.login).pack(pady=20)

    def login(self):
        id_cliente = self.id_cliente_entry.get()
        password = self.password_entry.get()
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mae_cliente WHERE id_cliente=%s AND contrasenia=%s", (id_cliente, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.master.switch_frame(Menu, id_cliente)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
