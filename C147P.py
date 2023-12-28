from tkinter import*
root = Tk()
root.title("Encryption with ASCII Code")
root.geometry("400x400")
root.configure(background = "Lightblue1")

ew= Entry(root)
ew.place(relx = 0.5, rely = 0.4, anchor = CENTER)

l1= Label(root, text="Name in ASCII : ", bg = "light cyan", fg = "black")
l1.place(relx = 0.5, rely= 0.6, anchor= CENTER)


l2= Label(root, text="Ebcrypted Name : ", bg = "light cyan", fg = "black")
l2.place(relx = 0.5, rely= 0.7, anchor= CENTER)

def asciiConverter():
    input_word = str(ew.get())
    l1["text"]+= str(ord(letter)) +" "
    ascii = int(ord(letter))
    encrypted = ascii - 1
    l2["text"] += str(chr(encrypted))
    
b1 = Button(root, text = "Display the ASCII code and Encrypted value", command = asciiConverter, bg = 'cornflower blue', fg = 'white')
b1.place(relx  =0.5, rely = 0.5, anchor = CENTER)

root.mainloop()