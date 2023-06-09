import pytube
from tkinter import*
from tkinter import messagebox


window = Tk()
window.geometry("700x500+350+100")
window.title("YOUTUBE DOWLANDER")
window.configure(bg="black")

def dowlander():
    try:
        url = (my_entry.get())
        path = "Desktop"
        pytube.YouTube(url).streams.get_highest_resolution().download(path)
        messagebox.showinfo(title="dowlander",message="dowland")


    except:
        messagebox.showerror(title="error",message="uygulamayı yeniden başlatın")




def bosluk(x):
    cerceve = Frame()
    cerceve.pack(pady=x)
bosluk(50)

my_label = Label(text="PLEASE YOUTUBE URL",font="Kablammo",fg="red",bg="black")
my_label.pack()

bosluk(10)

my_entry = Entry(width=50)
my_entry.pack()

bosluk(20)
my_button = Button(text="Dowland",width=20,height=2,fg="red",bg="black",command=dowlander)
my_button.pack()



window.mainloop()


