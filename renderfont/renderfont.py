from PIL import ImageFont, ImageDraw, Image
from PIL import Image, ImageChops

from PIL import ImageTk

class BBox:
    def __init__(self, bbox):
        ''' __init__(self, bbox:tuple)->None '''
        self.left, self.top, self.right, self.bottom = bbox
    @property
    def width(self):
        return self.right - self.left + 1;
    @property
    def height(self):
        return self.bottom - self.top + 1;

class CustomFont:
    def __init__(self, master, fontfile, font_size, txt, fill=(0,0,0), type_='normal'):
        self.master = master
        self.__font_render = None
        if not master:
            return
        self.__font_render = RenderFont(fontfile, fill)
        self.__render(font_size, txt, type_)
    def __render(self, font_size, txt, type_='normal'):
        self.__pil_image = self.__photo_image = None
        if not self.__font_render:
            return None
        self.__pil_image = self.__font_render.get_render(font_size, txt, type_)
        self.__photo_image = ImageTk.PhotoImage(self.__pil_image)
    @property
    def pilimage(self):
        if not self.__font_render:
            return None
        return self.__pil_image
    @property
    def photoimage(self):
        if not self.__font_render:
            return None
        return self.__photo_image

#https://stackoverflow.com/a/10616717
def trim_image(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

# https://stackoverflow.com/a/73428832
class RenderFont:
    def __init__(self, filename, fill=(0, 0, 0)):
        """
        constructor for RenderFont
        filename: the filename to the ttf font file
        fill: the color of the text
        """
        self._file = filename
        self._fill = fill
        self._image = None

    def get_render(self, font_size, txt, type_="normal"):
        """
        returns a transparent PIL image that contains the text
        font_size: the size of text
        txt: the actual text
        type_: the type of the text, "normal" or "bold"
        """
        if type(txt) is not str:
            raise TypeError("text must be a string")

        if type(font_size) is not int:
            raise TypeError("font_size must be a int")

        # Hangman Tkinter 가 주석으로 뺐음.
        # width = len(txt)*font_size
        # height = font_size+5
        # font = ImageFont.truetype(font=self._file, size=font_size)
        # self._image = Image.new(mode='RGBA', size=(width, height), color=(255, 255, 255))

        # Hangman Tkinter 가 넣었음.
        font = ImageFont.truetype(font=self._file, size=font_size)
        bbox = BBox(font.getbbox(txt))
        (width, height) = (bbox.width, bbox.height)
        self._image = Image.new(mode='RGBA', size=(width, height), color=(255, 255, 255))

        rgba_data = self._image.getdata()
        newdata = []

        for item in rgba_data:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newdata.append((255, 255, 255, 0))

            else:
                newdata.append(item)

        self._image.putdata(newdata)

        draw = ImageDraw.Draw(im=self._image)

        if type_ == "normal":
            draw.text(xy=(width/2, height/2), text=txt, font=font, fill=self._fill, anchor='mm')
        elif type_ == "bold":
            draw.text(xy=(width/2, height/2), text=txt, font=font, fill=self._fill, anchor='mm',
            stroke_width=1, stroke_fill=self._fill)

        return self._image
