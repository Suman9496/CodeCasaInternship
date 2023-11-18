from tkinter import *

root = Tk()


def send():
    send = "You:" + e.get()
    text.insert(END, "\n" + send)
    if e.get() == 'hi':
        text.insert(END, "\n" + "Bot: hello")
    elif e.get() == 'hello':
        text.insert(END, "\n" + "Bot: hi")
    elif e.get() == 'how are you?':
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif e.get() == "i'm fine too":
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif e.get() == "what is the day today?":
        text.insert(END, "\n" + "Bot: Today is wednesday.")
    elif e.get() == "Where are you right now?":
        text.insert(END, "\n" + "Bot: Inside your heart.")
    elif e.get() == "Who developed you?":
        text.insert(END, "\n" + "Bot: My dear suman shah")
    elif e.get() == "Who is antima's besti?":
        text.insert(END, "\n" + "Bot: books")
    elif e.get() == "Who is suman's partner?":
        text.insert(END, "\n" + "Bot: Amkar Vaibhav")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")


text = Text(root, bg='blue', fg='white')
text.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=80)
Button(root, text='Send', bg='deeppink', fg='white', width=20, command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title('SKNG.com')
root.mainloop()
