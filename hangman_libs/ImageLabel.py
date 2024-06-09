#!python3
import itertools
import PIL.Image
import PIL.ImageTk
import tkinter

class ImageLabel(tkinter.Label):
    """
    A Label that displays images, and plays them if they are gifs
    """
    def __make_photoimage(self, theImage):
        source_pil_image = theImage
        source_pil_image = source_pil_image.convert("RGBA")    
        photoimg = PIL.ImageTk.PhotoImage(image=source_pil_image)
        return photoimg

    MININUM_DURATION = 20
    def load(self, im,  bgtype="check"):
        ''' :im: A PIL PIL.Image instance or a string filename'''    
        if isinstance(im, str):
            im = PIL.Image.open(im)
        frames = []
        duration = []
        try:
            for i in itertools.count(1):
                imphoto = self.__make_photoimage(im.copy())
                frames.append(imphoto)
                try:
                    duration.append(im.info['duration'])
                    if duration[-1] == 0:
                        duration[-1] = ImageLabel.MININUM_DURATION
                except:
                    duration.append(100)
                im.seek(i)
        except EOFError:
            pass
        self.frames = itertools.cycle(frames)
        self.duration = itertools.cycle(duration)
        self.__stop = False
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def stop(self):
        self.__stop = True

    def resume(self):
        self.__stop = False

    def next_frame(self):
        if self.__stop:
            return
        if self.winfo_viewable():
            if self.frames:
                self.config(image=next(self.frames))
        self.after(next(self.duration), self.next_frame)


if __name__ == "__main__":
    import sys, os    

    self_dir  = os.path.dirname(__file__)
    gif_filename = os.path.join(self_dir,'__imagelabel.gif')

    root = tkinter.Tk()
    lbl =  ImageLabel(root)
    lbl.load(gif_filename)
    lbl.pack()

    root.mainloop()
    