# тут будет построение пользовательского интерфейс
from msilib.schema import ListBox
import tkinter as tk
from tkinter import LEFT, ttk
import sys
from turtle import width


class Application(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("INJMold_cycle_time_calc")
        self.set_ui()
    
    def set_ui(self):
        material_label = ttk.Label(self, text="Choose material")
        material_label.pack()

        combo_materials = ttk.Combobox(self, values=["PC/ABS", "PP", "PC"])
        combo_materials.pack()

        thickness_label = ttk.Label(self, text="Choose thickness")
        thickness_label.pack()

        combo_thickness = ttk.Combobox(self, values=[1.5, 2, 2.5, 3, 3.5, 4, 5, 6])
        combo_thickness.pack()

        calc_but = ttk.Button(self, text="Calculate", command="")
        calc_but.pack()

        result_lable = ttk.Label(self, text="result:")
        result_lable.pack()

        result_text = tk.Text(self, width=20, height=10)
        result_text.pack()

        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_but.pack(pady=30)
        

    def app_exit(self):
        self.destroy()
        sys.exit()
