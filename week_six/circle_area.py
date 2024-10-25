import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
from math import pi

def main():
  root = tk.Tk()
  
  frm_main = Frame(root)
  frm_main.master.title('Circle Area')
  frm_main.pack(padx=3, pady=3, fill=tk.BOTH, expand=1)

  populate_main_window(frm_main)

  root.mainloop()

def populate_main_window(frm_main):
  lbl_title = Label(frm_main, text='Area of a circle', font=('Comic Sans MS', 16))

  lbl_sub = Label(frm_main, text='Formula:')
  lbl_form = Label(frm_main, text='a = πr²')
  
  lbl_ratio = Label(frm_main, text='r = ')
  ent_r = FloatEntry(frm_main, width=5, lower_bound=0)
  lbl_meters = Label(frm_main, text='m')

  lbl_pi = Label(frm_main, text='π =')
  lbl_value = Label(frm_main, text=f'{pi:.2f}')

  lbl_area = Label(frm_main, text='Area:')
  lbl_total = Label(frm_main, width=10)
  lbl_units = Label(frm_main, text='m²')

  btn_clear = Button(frm_main, text="Clear", width=10, font=('Comic Sans MS', 10))


  lbl_title.grid( row=0, column=0, pady=3, columnspan=8)

  lbl_sub.grid(   row=1, column=0, pady=0, columnspan=2, sticky='e')
  lbl_form.grid(  row=1, column=2, pady=0, columnspan=2, sticky='w')

  lbl_ratio.grid( row=2, column=0, pady=3, sticky='e')
  ent_r.grid(     row=2, column=1, pady=3)
  lbl_meters.grid(row=2, column=2, pady=3, sticky='w')

  lbl_pi .grid(   row=3, column=0, pady=3, sticky='e')
  lbl_value.grid( row=3, column=1, pady=3, sticky='w')

  lbl_area.grid(  row=4, column=5, pady=3, padx=(30, 0), sticky='e')
  lbl_total.grid( row=4, column=6, pady=3)
  lbl_units.grid( row=4, column=7, pady=3, sticky='w')

  btn_clear.grid( row=5, column=6, pady=3, padx=3, columnspan=2, sticky='e')

  def calculate(event):
    try:

      ratio = ent_r.get()

      area = pi * ratio ** 2
      lbl_total.config(text=f'{area:.2f}')

    except ValueError:
      lbl_total.config(text='')

  def clear():
        btn_clear.focus()
        ent_r.clear()
        lbl_total.config(text="")

  ent_r.bind("<KeyRelease>", calculate)

  btn_clear.config(command=clear)

if __name__ == '__main__':
  main()