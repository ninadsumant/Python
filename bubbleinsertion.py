from tkinter import *

window=Tk()

def bubble():
    text.delete(1.0,END)
    a=input.get()
    arr=a.split(",")
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    text.insert(END,arr)


def insertion():
    text.delete(1.0,END)
    a=input.get()
    arr=a.split(",")
    for i in range(1, len(arr)): 
        key = arr[i]  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    text.insert(END,arr)



input=Entry(window)

text=Text(window,height=2,width=20,background="Red")

b1=Button(window,text="Bubble",command=bubble)

b2=Button(window,text="Insertion",command=insertion)

input.pack()
text.pack()
b1.pack()
b2.pack()
window.geometry("500x500")
window.mainloop()
