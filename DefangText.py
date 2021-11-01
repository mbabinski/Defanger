# -*- coding: cp1252 -*-
# Title: DefangText.py
# Author: Micah Babinski, Junior Security Analyst, Mosaic451 MDR Team
# Date: 3/24/2021
# Description: Text entry widget capable of defanging IP addresses and URLs. Reduces the risk of accidentally
# connecting to a malicious host or website.

# import tkinter module, should work with either Python 2.x or 3.x
try:
    from Tkinter import *
except:
    from tkinter import *

# regex import
import re, ipaddress

# function to defang input text
def Defang(inputText, ignorePrivate=True):
    url_candidates = [x[0] for x in re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", inputText)]
    if len(url_candidates) > 0:
        for url in url_candidates:
            inputText = inputText.replace(url, url.replace(".", "[.]"))
        inputText = inputText.replace("http:", "hxxp:").replace("https:", "hxxps:")

    ftp_candidates = [x[0] for x in re.findall(r"(?i)\b((?:ftp?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", inputText)]
    if len(ftp_candidates) > 0:
        for ftp in ftp_candidates:
            inputText = inputText.replace(ftp, ftp.replace(".", "[.]"))
        inputText = inputText.replace("ftp:", "fxp:")

    ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", inputText)
    if len(ip_candidates) > 0:
        for ip in ip_candidates:
            if ignorePrivate == False:
                inputText = inputText.replace(ip, ip.replace(".", "[.]"))
            else:
                if not ipaddress.ip_address(ip).is_private:
                    inputText = inputText.replace(ip, ip.replace(".", "[.]"))

    return inputText

# functions to define button press actions
def DefangPress():
    inputTxt = text.get("1.0","end-1c")
    text.delete("1.0", END)
    if cb.get() == 1:
        ignorePrivate = True
    else:
        ignorePrivate = False
    text.insert(END, Defang(inputTxt, ignorePrivate))

def CopyPress():
    copyTxt = text.get("1.0","end-1c")
    screen.clipboard_clear()
    screen.clipboard_append(copyTxt)

def ClearPress():
    text.delete("1.0", END)

def Close():
    screen.destroy()

# widget construction and configuration
screen = Tk()
screen.title("Defanger")
scroll = Scrollbar(screen)
scroll.pack(side=RIGHT, fill=Y)
text = Text(screen, yscrollcommand=scroll.set)
text.pack(expand=1,fill='both')
text.insert(END, "Paste or enter text here.")
cb = IntVar()
cb.set(1)
checkBox = Checkbutton(screen, text = "Ignore private IP addresses.", variable=cb, onvalue=1, offvalue=0)
checkBox.pack()
btn = Button(screen, text = "Defang text", width = 10, command = DefangPress) 
btn.pack(fill=X)
btn2 = Button(screen, text = "Copy to clipboard", command = CopyPress)
btn2.pack(fill=X)
btn4 = Button(screen, text = "Clear", command = ClearPress)
btn4.pack(fill=X)
btn3 = Button(screen, text = "Close", command = Close)
btn3.pack(fill=X)
scroll.config(command=text.yview)


# start app
mainloop()
