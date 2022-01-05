import datetime as dt
import locale
import tkinter as tk

from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font

#==========#
# 関数定義 #
#==========#
def copyMessage():
    # Get Strings
    txt2 = txt.get('1.0', tk.END+'-1c')

    # Clipboard
    root.clipboard_clear()     # Clear
    root.clipboard_append(txt2) # Copy

    # Message Dialog
    if txt2 != '':
        messagebox.showinfo('Copy Message', 'クリップボードにコピーしました')

#=========#
# GUI定義 #
#=========#
root = tk.Tk()
root.title('Copy Message')
root.minsize(300, 200)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry('320x160')

### Frame ###
#frame1 = ttk.Frame(root, padding=1)
#frame1.rowconfigure(1, weight=1)
#frame1.columnconfigure(0, weight=1)
#frame1.grid(sticky=(N, W, S, E))

# ------------------------------------------------------------------------------
### Text ###
f = Font(family='Meiryo UI', size=12)
#txt = Text(frame1, height=15, width=70)

locale.setlocale(locale.LC_ALL, '') # 文字化け対策
dte = dt.datetime.now().strftime('%Y/%m/%d (%a)')
tim = dt.datetime.now().strftime('%H:%M')
txt = tk.Text(font=('Meiryo UI',12), width=30, height=3)
txt.configure(font=f)
txt.insert(1.0, "@here " + dte + "\nおはようございます。\n9:00より業務を開始致します。")
##txt.grid(row=1, column=0, sticky=(N, W, S, E))
txt.pack(expand=1)

### ###
button = tk.Button(
	root,
	text='コピー',
	font=('Meiryo UI',12),
	command=copyMessage)
#button1 = ttk.Button(
#    frame1, text='OK',
#    command=lambda: print('%s' % txt.get(1.0, END)))
#button1.grid(
#    row=0, column=0, columnspan=2, sticky=(N, E))
button.pack(expand=1)

root.mainloop()
