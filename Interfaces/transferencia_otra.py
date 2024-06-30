import tkinter as tk
from tkinter import messagebox
from db_connection import connect
from confirmacion import Confirmacion  

class TransferenciaOtra(tk.Frame):
    def __init__(self, master, id_cliente):
        super().__init__(master)
        self.master = master
        self.id_cliente = id_cliente
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Cuenta Destino:").pack(pady=10)
        self.cuenta_destino_entry = tk.Entry(self)
        self.cuenta_destino_entry.pack(pady=5)

        tk.Label(self, text="Monto:").pack(pady=10)
        self.monto_entry = tk.Entry(self)
        self.monto_entry.pack(pady=5)

        tk.Button(self, text="Siguiente", command=self.confirmar).pack(pady=20)

    def confirmar(self):
        cuenta_destino = self.cuenta_destino_entry.get()
        monto = self.monto_entry.get()

        if cuenta_destino and monto:
            conn = connect()
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT nro_cuenta FROM mae_cuenta WHERE id_cliente = %s", (self.id_cliente,))
                cuentas_origen = cursor.fetchall()  # Obtenemos todas las cuentas del cliente
                if cuentas_origen:
                    cuenta_origen = cuentas_origen[0][0]  # Seleccionamos la primera cuenta del cliente como ejemplo
                    cursor.execute("""
                        SELECT mae_persona.nombre, mae_persona.apellido 
                        FROM mae_persona
                        JOIN mae_cliente ON mae_persona.id_persona = mae_cliente.id_cliente
                        JOIN mae_cuenta ON mae_cliente.id_cliente = mae_cuenta.id_cliente
                        WHERE mae_cuenta.nro_cuenta = %s
                    """, (cuenta_destino,))
                    destino = cursor.fetchone()

                    if destino:
                        nombre_destino = f"{destino[0]} {destino[1]}"
                        self.master.switch_frame(Confirmacion, self.id_cliente, cuenta_origen, cuenta_destino, monto, "otra", nombre_destino)
                    else:
                        messagebox.showerror("Error", "Cuenta destino no encontrada")
                else:
                    messagebox.showerror("Error", "No se encontraron cuentas para el cliente")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")
            finally:
                conn.close()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")