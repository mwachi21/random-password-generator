# Password Generator

import random
# clipboard data
import pyperclip
#Tkinter
from tkinter import *


# Main Project
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&-+()*':;!?[]}{£¢~÷×."

all = lower + upper + numbers + symbols
length = 9
length < 15

# Pass Generator

password = " " . join (random.sample(all,length))
print (password)


root = Tk(password)

# code to be copied

pyperclip.copy(password)
