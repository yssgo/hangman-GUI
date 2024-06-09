#!python3
import tkinter

class TextLabel(tkinter.Label):
    """
    A Label that displays images, and plays them if they are gifs
    """
    MININUM_DURATION = 20
    def blink(self, fglist=[], bglist=[], duration=250, /):
        self.fglist, self.fgindex = fglist, 0
        self.bglist, self.bgindex = bglist, 0
        self.duration = max(self.MININUM_DURATION, duration)
        self.next_frame()
        self.__stop = False

    def stop(self):
        self.__stop = True

    def resume(self):
        self.__stop = False

    def next_frame(self):
        if self.__stop:
            return
        if self.winfo_viewable():
            if self.fglist:
                self.config(fg=self.fglist[self.fgindex])
                self.fgindex += 1
                self.fgindex %= len(self.fglist)
            if self.bglist:
                self.config(bg=self.bglist[self.bgindex])
                self.bgindex += 1
                self.bgindex %= len(self.bglist)
        self.after(self.duration, self.next_frame)

if __name__ == "__main__":
    import sys, os

    root = tkinter.Tk()
    lbl =  TextLabel(root, text="졌습니다", font=('D2Coding', 20, 'normal'))
    lbl.pack()
    lbl.blink(['yellow','blue'],['blue','yellow'], 250)

    root.mainloop()
