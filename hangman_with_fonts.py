import tkinter as tk
import random
import sys
import copy
from renderfont import *
root = tk.Tk()
root.minsize(600,400)

        
word_list = [
    'apple',
    'banana',
    'python',
    'game',
    'program',
] 

stages = []
for st in '0123456':
    stages.append(CustomFont(root, 'fonts/Hangman_Stage.ttf', 256, st, fill=(170,0,0)).photoimage)

IMG_LOGO = CustomFont(root, 'fonts/Hangman_Logo.ttf', 200, 'hangman', fill=(0,255,0)).photoimage

FNT_WARNING =('D2Coding', 12, 'normal')
FNT_INPUT = FNT_STATE = ('D2Coding', 16, 'normal')
FNT_DISPLAY = ('D2Coding', 16, 'normal')
FNT_WIN = FNT_LOSE = ("D2Coding", 20,"bold")

#lbl_logo = tk.Label(root, text=logo, font=FNT_LOGO, justify='left', fg='blue', bg='#eff')
lbl_logo = tk.Label(root, image = IMG_LOGO, bg='#eff')
lbl_logo.pack(anchor='center', expand=True, ipadx=20, ipady=20)
lbl_font_blurb = tk.Label(root, text='D2Coding 폰트를 사용합니다')
lbl_font_blurb.pack()

root.update() # tkinter 창 보이기

import time
time.sleep(3.26)

lbl_logo.destroy()
lbl_font_blurb.destroy()

def init_game():
    global answer_word, memory, display
    global end_of_game, live
    
    answer_word = random.choice(word_list)
    memory = []
    display = []
    for i in answer_word: #answer_word의 문자열 개수만큼 반복
        display += ['_']

    end_of_game = False
    live = 6

init_game()

mainframe = tk.Frame(root)
mainframe.pack(expand=True, fill='both')

#stages[live]
lbl_state = tk.Label(mainframe, image=stages[-1-live])
lbl_state.pack(fill='x', expand=True)


def longest(words):
    return max(len(w) for w in words)
lbl_display = tk.Label(mainframe, text=' '.join(display), font=FNT_DISPLAY, width=max(longest(word_list),50))
lbl_display.pack(fill='x', expand=True)
frm_Input = tk.Frame(mainframe)
lbl_Input = tk.Label(frm_Input, text="알파벳을 입력하세요", font=FNT_INPUT)

def new_game(*args):
    if len(args)==0:
        # Button clicked
        pass
    elif len(args)==1:
        # Enter key pressed
        pass        

    btn_Input.unbind('<Return>')
    init_game()
    lbl_Warning.pack_forget()
    lbl_Lose.pack_forget()
    lbl_Win.pack_forget()
    lbl_state.config(image=stages[-1-live]) #stages[live]
    lbl_display.config(text=' '.join(display))
    ent_Input.bind('<Return>', check)
    btn_Input.config(text='입력')
    ent_Input.config(state='normal')
    ent_Input.focus_set()    


def check(*args):    
    global end_of_game, live
    if len(args)==0:
        # Button clicked
        pass
    elif len(args)==1:
        # Enter key pressed
        pass
        
    def hide_warning():
        lbl_Warning.pack_forget()
    guess_letter = ent_Input.get().lower()
    ent_Input.delete(0,'end')

    if guess_letter == '':
        lbl_Warning.pack_forget()
        return
    if guess_letter in memory:
        lbl_Warning.pack()
        return
    else:
        lbl_Warning.pack_forget()
        memory.append(guess_letter)

    
    for position in range(len(answer_word)):
        if answer_word [position] == guess_letter:
            display[position] = guess_letter

    lbl_display.config(text = ' '.join(display))
    
    if guess_letter not in answer_word:
        live -= 1
        if live >= 0:
            lbl_state.config(image = stages[-1-live]) #stages[live]

    if live == 0:
        end_of_game = True
        lbl_Warning.pack_forget()
        lbl_Lose.pack()

    elif "_" not in display:
        end_of_game = True
        lbl_Warning.pack_forget()        
        lbl_Win.pack()
    
    
    if end_of_game:
        ent_Input.unbind('<Return>')
        ent_Input.config(state = 'disabled')
        btn_Input.config(text = '새 게임', command=new_game)
        btn_Input.bind('<Return>', new_game)
        btn_Input.focus_set()
        
    

ent_Input = tk.Entry(frm_Input, width=2, font=FNT_INPUT)
ent_Input.bind('<Return>', check)
btn_Input = tk.Button(frm_Input, text="입력", command=check,font=FNT_INPUT)

lbl_Input.pack(side='left',expand='true')
ent_Input.pack(side='left',expand='true')
btn_Input.pack(side='left',expand='true')
frm_Input.pack(expand=True)

frm_Warning = tk.Frame(mainframe)
lbl_Warning = tk.Label(frm_Warning, text="이미 입력했던 알파벳입니다", font=FNT_WARNING)
lbl_Lose = tk.Label(frm_Warning, text="졌습니다", font=FNT_LOSE, fg='#f88', bg='yellow')
lbl_Win = tk.Label(frm_Warning, text="이겼습니다", font=FNT_WIN, fg='#00f', bg='#ff0')
frm_Warning.pack(expand=True, fill='x')

ent_Input.focus_set()

root.mainloop()

