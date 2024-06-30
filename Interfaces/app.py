import tkinter as tk
from login import Login  # Asegúrate de importar Login

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App de Transferencias")
        self.geometry("300x500")
        self.resizable(False, False)

        self.switch_frame(Login)

    def switch_frame(self, frame_class, *args):
        new_frame = frame_class(self, *args)
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
