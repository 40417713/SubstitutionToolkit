from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class Window():
    def __init__(self, master):
        self.master = master
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.substitution = []

        self.substitution_entry = []

        self.init_var()
        self.draw_widgets()

    def init_var(self):
        for letter in self.alpha:
            self.substitution.append([letter, letter])

    def draw_widgets(self):
        padding = 5

        BOX_A = LabelFrame(self.master, text=" Current Substitution: ") # Current Substitution
        BOX_A.grid(row=0, column=0, sticky=W, pady=padding, padx=padding, ipady=padding, ipadx=padding, rowspan=2)
        
        BOX_B = LabelFrame(self.master, text=" Input Text: ")           # Input Text
        BOX_B.grid(row=0, column=1, sticky=W, pady=padding, padx=padding, ipady=padding, ipadx=padding)

        BOX_C = LabelFrame(self.master, text=" Output Text: ")          # Output Text
        BOX_C.grid(row=0, column=2, sticky=W, pady=padding, padx=padding, ipady=padding, ipadx=padding)
        
        BOX_D = LabelFrame(self.master, text=" Letter Frequency: ")     # Graph
        BOX_D.grid(row=1, column=1, sticky=W, pady=padding, padx=padding, ipady=padding, ipadx=padding)
        
        BOX_E = LabelFrame(self.master, text=" Suggestions: ")          # Notes and Suggestions
        BOX_E.grid(row=1, column=2, sticky=W, pady=padding, padx=padding, ipady=padding, ipadx=padding)

        # --- Draw Widgets --- #

        # Current Substitution
        self.draw_substitution(BOX_A)

        # Input Text
        # Output Text
        # Graph
        # Notes and Suggestions

    def draw_substitution(self, frame):
        subframe = Canvas(frame)
        subframe.pack(padx=10, pady=10, anchor=W)
        rows = len(self.alpha)/2

        pos = [0, 0]
        for letter in self.alpha:
            if pos[0] >= rows:
                pos[0] = 0
                pos[1] += 2
            
            Label(subframe, text=letter).grid(row=pos[0], column=pos[1])

            e = Entry(subframe, width=3)
            e.grid(row=pos[0], column=pos[1]+1)
            self.substitution_entry.append(e)
            
            pos[0] += 1

            
root = Tk()
root.title("Substitution Tool")

x = Window(root)












##from tkinter import *
##import matplotlib.pyplot as plt
##import numpy as np
##
##
##msg = "The future of the Internet, especially in expanding the range of applications, involves a much deeper degree of privacy, and authentication. Without these the Internet cannot be properly used to replace existing applications such as in voting, finance, and so on. The future is thus towards data encryption which is the science of cryptographics , and provides a mechanism for two entities to communicate without any other entity being able to read their messages. In a secret communications system, Bob and Alice should be able to communicate securely, without Eve finding out the contents of their messages, or in keeping other details secure, such as their location, or the date that their messages are sent. The two main methods used are to either use a unique algorithm which both Bob and Alice know, and do not tell Eve, or they use a well-known algorithm, which Eve also knows, and use some special electronic key to uniquely define how the message is converted into Ciphertext, and back again. A particular problem in any type of encryption is the passing of the secret algorithm or the key in a secure way, as Bob or Alice does not know if Eve is listening to their communications. If Eve finds-out the algorithm or the key, neither Bob nor Alice is able to detect this. This chapter looks at some of the basic principles of encryption, including the usage of private-key and public-key methods. As we will find public and private key methods work together in perfect harmony, with, typically, private key methods providing in the actual core encryption, and public key methods providing ways to authenticate, and pass keys."
##
##FREQ = [["a", 8.167], ["b", 1.492], ["c", 2.782], ["d", 4.253], ["e", 12.702], ["f", 2.228], ["g", 2.015], ["h", 6.094], ["i", 6.966], ["j", 0.153], ["k", 0.772], ["l", 4.025], ["m", 2.406], ["n", 6.749], ["o", 7.507], ["p", 1.929], ["q", 0.095], ["r", 5.987], ["s", 6.327], ["t", 9.056], ["u", 2.758], ["v", 0.978], ["w", 2.360], ["x", 0.150], ["y", 1.974], ["z", 0.074]]
##alpha = "abcdefghijklmnopqrstuvwxyz"
##
##bar_width = 0.35
##opacity = 0.8
##
##TRUE_FREQ = []
##for letter in alpha:
##    TRUE_FREQ.append([letter, 0])
##for letter in msg:
##    try:
##        TRUE_FREQ[alpha.index(letter)][1] += 1
##    except:
##        pass
##
##x1, y1, y2 = [], [], []
##for i in range(0, len(alpha)):
##    x1.append(FREQ[i][0])                           ## Letter
##    y1.append(float(TRUE_FREQ[i][1]/len(msg)*100))  ## Frequency in text
##    y2.append(float(FREQ[i][1]))                    ## Frequency in english language
##
##
##fig, ax = plt.subplots()
##index = np.arange(len(alpha))
##
##rect1 = plt.bar(index, y1, bar_width, alpha=opacity, color='g', label="Input Text")
##rect2 = plt.bar(index + bar_width, y2, bar_width, alpha=opacity, color='b', label="English Language")
##
##plt.xlabel("Letter")
##plt.ylabel("Frequency")
##
##plt.xticks(index + bar_width, x1)
##plt.legend()
##plt.tight_layout()
##plt.show()
