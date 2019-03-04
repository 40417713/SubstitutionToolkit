from tkinter import *


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.substitution = []
        self.font = ["Helvetica", 16]
        self.setup_widgets()

    def setup_widgets(self):

        # Draw alphabet
        sub = Canvas(self.master, width=200, height=200)
        sub.grid(row=0, column=0, rowspan=2)
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        spacing = 4
        rows = 13
        position = [-1, 0]
        for letter in alpha:
            position[0] += 1
            if position[0] >= rows:
                position[0] -= alpha.index(letter)
                position[1] += 3

            
            e = Entry(sub, width=2, font=self.font)
            e.grid(row=position[0], column=position[1]+1)
            self.substitution.append(e)
            l = Label(sub, text=str(letter.upper()+": "), font=self.font)
            l.grid(row=position[0], column=position[1])
            Label(sub, text=str(" "*spacing), font=self.font).grid(row=position[0], column=position[1]+2)

        # Draw substitute button and reset button
        Button(sub, text="Reset", font=(self.font[0],self.font[1]-3)).grid(row=position[0]+2, column=0, pady=10, padx=5, columnspan=3, sticky=N+S+E+W)
        Button(sub, text="Substitute", font=(self.font[0],self.font[1]-3)).grid(row=position[0]+2, column=3, pady=10, padx=5, columnspan=3, sticky=N+S+E+W)


        # Draw input and output box
        inp = Canvas(self.master, width=200, height=200)
        inp.grid(row=0, column=1)
        Label(inp, text="Input:").grid(row=0, column=0, sticky=W)
        self.input_text = Text(inp, height=12, width = 60)
        self.input_text.grid(row=1, column=0)
        
        
        out = Canvas(self.master, width=200, height=200)
        out.grid(row=1, column=1)
        Label(out, text="Output:").grid(row=0, column=0, sticky=W)
        self.output_text = Text(out, height=12, width = 60)
        self.output_text.grid(row=1, column=0)


        # 
root = Tk()
#root.geometry("400x300")

app = Window(root)
root.mainloop()
