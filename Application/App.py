#! /usr/bin/env python
# GUI helped created by PAGE version 4.8.9
# In conjunction with Tcl version 8.6

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
import tkinter as tk

from Application import App_support
from TweetAnalyzer import *

T = TwitterAnalysis()

def search(user):
    r = (user.get())
    T.name(r)


def common(name, common):
    try:
        common.configure(text=T.commonwords(name))
    except:
        common.configure(text="Search user first")

def percent(name, per):
    try:
        per.configure(text=T.tweetpercent(name))
    except:
        per.configure(text="Search user first")


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, result, entries, rt, ents
    root = Tk()
    rt = root
    result = tk.Label(rt)
    result.pack(side=tk.BOTTOM, padx=20, pady=20)
    App_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    App_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, ents
    w = Toplevel (root)
    App_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    App_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("600x450+446+140")
        top.title("Twitter Analysis")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.1, rely=0.13, relheight=0.74, relwidth=0.83)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=495)

        self.usernameL = Label(self.Frame1)
        self.usernameL.place(relx=0.02, rely=0.09, height=21, width=59)
        self.usernameL.configure(activebackground="#f9f9f9")
        self.usernameL.configure(activeforeground="black")
        self.usernameL.configure(background="#d9d9d9")
        self.usernameL.configure(disabledforeground="#a3a3a3")
        self.usernameL.configure(foreground="#000000")
        self.usernameL.configure(highlightbackground="#d9d9d9")
        self.usernameL.configure(highlightcolor="black")
        self.usernameL.configure(text='''Username''')

        self.usernamefield = Entry(self.Frame1)
        self.usernamefield.place(relx=0.14, rely=0.09, relheight=0.06
                , relwidth=0.53)
        self.usernamefield.configure(background="white")
        self.usernamefield.configure(disabledforeground="#a3a3a3")
        self.usernamefield.configure(font="TkFixedFont")
        self.usernamefield.configure(foreground="#000000")
        self.usernamefield.configure(highlightbackground="#d9d9d9")
        self.usernamefield.configure(highlightcolor="black")
        self.usernamefield.configure(insertbackground="black")
        self.usernamefield.configure(selectbackground="#c4c4c4")
        self.usernamefield.configure(selectforeground="black")

        self.searchB = Button(self.Frame1)
        self.searchB.place(relx=0.73, rely=0.09, height=24, width=86)
        self.searchB.configure(activebackground="#d9d9d9")
        self.searchB.configure(activeforeground="#000000")
        self.searchB.configure(background="#d9d9d9")
        self.searchB.configure(disabledforeground="#a3a3a3")
        self.searchB.configure(foreground="#000000")
        self.searchB.configure(highlightbackground="#d9d9d9")
        self.searchB.configure(highlightcolor="black")
        self.searchB.configure(pady="0")
        self.searchB.configure(text='''Search''')
        self.searchB.configure(width=86)
        self.searchB.configure(command=(lambda e=self.usernamefield: search(e)))

        self.common = Label(self.Frame1)
        self.common.place(relx=0.14, rely=0.66, relheight=0.21, relwidth=0.53)
        self.common.configure(background="white")
        self.common.configure(disabledforeground="#a3a3a3")
        self.common.configure(font="TkFixedFont")
        self.common.configure(foreground="#000000")
        self.common.configure(highlightbackground="#d9d9d9")
        self.common.configure(highlightcolor="black")
        self.common.configure(width=264)

        self.commonB = Button(self.Frame1)
        self.commonB.place(relx=0.73, rely=0.66, height=24, width=99)
        self.commonB.configure(activebackground="#d9d9d9")
        self.commonB.configure(activeforeground="#000000")
        self.commonB.configure(background="#d9d9d9")
        self.commonB.configure(disabledforeground="#a3a3a3")
        self.commonB.configure(foreground="#000000")
        self.commonB.configure(highlightbackground="#d9d9d9")
        self.commonB.configure(highlightcolor="black")
        self.commonB.configure(pady="0")
        self.commonB.configure(text='''Common Words''')
        self.commonB.configure(command=(lambda e=self.usernamefield: common(e, self.common)))

        self.per = Label(self.Frame1)
        self.per.place(relx=0.14, rely=0.33, relheight=0.19, relwidth=0.53)
        self.per.configure(background="white")
        self.per.configure(font="TkTextFont")
        self.per.configure(foreground="black")
        self.per.configure(highlightbackground="#d9d9d9")
        self.per.configure(highlightcolor="black")
        self.per.configure(width=264)

        self.percentB = Button(self.Frame1)
        self.percentB.place(relx=0.73, rely=0.33, height=30, width=90)
        self.percentB.configure(activebackground="#d9d9d9")
        self.percentB.configure(activeforeground="#000000")
        self.percentB.configure(background="#d9d9d9")
        self.percentB.configure(disabledforeground="#a3a3a3")
        self.percentB.configure(foreground="#000000")
        self.percentB.configure(highlightbackground="#d9d9d9")
        self.percentB.configure(highlightcolor="black")
        self.percentB.configure(pady="0")
        self.percentB.configure(text='''Percentage''')
        self.percentB.configure(width=90)
        self.percentB.configure(command=(lambda e=self.usernamefield: percent(e, self.per)))


if __name__ == '__main__':
    vp_start_gui()

