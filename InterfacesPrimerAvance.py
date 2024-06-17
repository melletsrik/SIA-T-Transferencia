import tkinter as tk
from tkinter import messagebox
import random

def generar_numero_operacion():
    return random.randint(10000000, 99999999)

def abrir_interfaz_monto_enviado(monto, cuenta_interbancaria):
    numero_operacion = generar_numero_operacion()
    
    enviado_ventana = tk.Toplevel()
    enviado_ventana.title("Monto enviado")
    enviado_ventana.geometry("400x500")

    tk.Label(enviado_ventana, text="Monto enviado:", font=("Arial", 16)).pack(pady=10)
    tk.Label(enviado_ventana, text=f"S/ {monto:.2f}", font=("Arial", 24)).pack(pady=5)
    tk.Label(enviado_ventana, text="Martes, 11 Junio 2024 - 08:19 a.m.", font=("Arial", 10)).pack(pady=5)

    frame_botones = tk.Frame(enviado_ventana)
    frame_botones.pack(pady=10)
    tk.Button(frame_botones, text="Descargar", font=("Arial", 12)).pack(side=tk.LEFT, padx=20)
    tk.Button(frame_botones, text="Compartir", font=("Arial", 12)).pack(side=tk.LEFT, padx=20)

    tk.Label(enviado_ventana, text="Enviado a", font=("Arial", 14)).pack(pady=10)
    tk.Label(enviado_ventana, text=f"Nombre del destinatario\n{cuenta_interbancaria}\nMoneda Soles", font=("Arial", 12)).pack(pady=5)

    tk.Label(enviado_ventana, text="Desde", font=("Arial", 14)).pack(pady=10)
    tk.Label(enviado_ventana, text="Cuenta Digital Soles\n**1086", font=("Arial", 12)).pack(pady=5)

    tk.Label(enviado_ventana, text=f"Número de operación\n{numero_operacion}", font=("Arial", 12)).pack(pady=10)

def abrir_interfaz_confirmacion(monto, cuenta_interbancaria):
    confirmacion_ventana = tk.Toplevel()
    confirmacion_ventana.title("Confirmación")
    confirmacion_ventana.geometry("400x400")

    tk.Label(confirmacion_ventana, text=f"S/ {monto:.2f}", font=("Arial", 24)).pack(pady=10)
    tk.Label(confirmacion_ventana, text="Monto total", font=("Arial", 10)).pack(pady=5)

    tk.Label(confirmacion_ventana, text="Enviar a", font=("Arial", 14)).pack(pady=10)
    tk.Label(confirmacion_ventana, text=f"Nombre del destinatario\n{cuenta_interbancaria}\nMoneda Soles", font=("Arial", 12)).pack(pady=5)
    tk.Label(confirmacion_ventana, text="Agregar a favoritos", font=("Arial", 12), fg="orange").pack(pady=5)

    tk.Label(confirmacion_ventana, text="Desde", font=("Arial", 14)).pack(pady=10)
    tk.Label(confirmacion_ventana, text="Cuenta Digital Soles\n**5013", font=("Arial", 12)).pack(pady=5)

    tk.Label(confirmacion_ventana, text="Enviar mensaje (Opcional)", font=("Arial", 10)).pack(pady=5)
    tk.Entry(confirmacion_ventana, width=50).pack(pady=5)

    tk.Label(confirmacion_ventana, text="Esta operación se confirmará con tu Token Digital.", font=("Arial", 10), fg="blue").pack(pady=10)

    def confirmar():
        abrir_interfaz_monto_enviado(monto, cuenta_interbancaria)

    tk.Button(confirmacion_ventana, text="Confirmar", command=confirmar, font=("Arial", 14), bg="orange", fg="white").pack(pady=20)

def abrir_otra_interfaz(cuenta_interbancaria):
    otra_ventana = tk.Toplevel()
    otra_ventana.title("Enviar a")
    otra_ventana.geometry("400x400")

    tk.Label(otra_ventana, text="Nombre del destinatario", font=("Arial", 12)).pack(pady=10)
    tk.Label(otra_ventana, text=cuenta_interbancaria, font=("Arial", 12)).pack()
    tk.Label(otra_ventana, text="Moneda Soles", font=("Arial", 10)).pack(pady=5)

    tk.Label(otra_ventana, text="Moneda y monto", font=("Arial", 14)).pack(pady=10)
    
    frame_moneda = tk.Frame(otra_ventana)
    frame_moneda.pack(pady=5)
    tk.Label(frame_moneda, text="S/", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
    monto_entry = tk.Entry(frame_moneda, width=20, font=("Arial", 14))
    monto_entry.pack(side=tk.LEFT, padx=5)
    
    tk.Label(otra_ventana, text="Desde", font=("Arial", 14)).pack(pady=10)
    frame_cuentas = tk.Frame(otra_ventana)
    frame_cuentas.pack(pady=5)
    tk.Label(frame_cuentas, text="Cuentas De Ahorro", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
    tk.Label(frame_cuentas, text="S/ Saldo", font=("Arial", 12)).pack(side=tk.RIGHT, padx=5)
    tk.Label(frame_cuentas, text="**5013", font=("Arial", 12)).pack(side=tk.RIGHT, padx=5)

    def continuar():
        monto = monto_entry.get()
        if monto:
            abrir_interfaz_confirmacion(float(monto), cuenta_interbancaria)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un monto.")

    tk.Button(otra_ventana, text="Continuar", command=continuar, font=("Arial", 14)).pack(pady=20)

def abrir_interfaz_final():
    final_ventana = tk.Toplevel()
    final_ventana.title("Interfaz Final")
    final_ventana.geometry("300x200")
    tk.Label(final_ventana, text="Esta es la interfaz final").pack(pady=20)
    tk.Button(final_ventana, text="Cerrar", command=final_ventana.destroy).pack(pady=10)

def entre_mis_cuentas():
    cuentas_ventana = tk.Toplevel()
    cuentas_ventana.title("Entre mis cuentas BCP")
    cuentas_ventana.geometry("300x200")
    tk.Label(cuentas_ventana, text="Cuentas BCP").pack(pady=20)
    tk.Button(cuentas_ventana, text="Cerrar", command=cuentas_ventana.destroy).pack(pady=10)

def transferir():
    numero_cuenta = cuenta_entry.get()
    if numero_cuenta:
        abrir_otra_interfaz(numero_cuenta)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un número de cuenta.")

app = tk.Tk()
app.title("Transferir dinero")
app.geometry("400x300")

tk.Label(app, text="Ingresa cuenta BCP o interbancaria").pack(pady=10)
cuenta_entry = tk.Entry(app, width=40)
cuenta_entry.pack(pady=10)

tk.Button(app, text="Confirmar", command=transferir).pack(pady=10)

tk.Button(app, text="Entre mis cuentas BCP", command=entre_mis_cuentas).pack(pady=10)

favoritos_frame = tk.Frame(app)
favoritos_frame.pack(pady=20)
tk.Label(favoritos_frame, text="Favoritos", font=("Arial", 14)).pack()
tk.Label(favoritos_frame, text="Aquí podrás ver Favoritos\nAgrégalos en el último paso de la operación\ncon la opción Agregar a favoritos").pack(pady=10)

app.mainloop()
