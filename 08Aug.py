import tkinter as tk
    
def add(a,b):
    print (a+b)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

one = tk.Button(frame, text="1")
two = tk.Button(frame, text="2")
three = tk.Button(frame, text="3")
equals = tk.Button(frame, text="=", command=add)
one.pack(side=tk.LEFT)
two.pack(side=tk.LEFT)
three.pack(side=tk.LEFT)
equals.pack(side=tk.BOTTOM)
a = one.get()
b = two.get()
root.mainloop()