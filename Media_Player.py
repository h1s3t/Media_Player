from re import L
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import pygame
pygame.init()
root = Tk()
root.title('MediaPlayer')
root.geometry('800x400')
root.resizable(False,False)
songs = ['13aurora - red crystal castles','Mr.Kitty - After Dark','Молчат Дома - Клетка']
i = 0
current_song = songs[i]
playing = False
played = True
#Картинки
play = PhotoImage(file = r"buttons/play.png")
stop = PhotoImage(file = r"buttons/stop.png")
next_song = PhotoImage(file = r"buttons/next.png")
previous_song = PhotoImage(file = r"buttons/previous.png")
quit_img = PhotoImage(file = r"buttons/quit.png")
md_ico = ImageTk.PhotoImage(Image.open('icos/md_ico.png'))
mk_ico = ImageTk.PhotoImage(Image.open('icos/mk_ico.png'))
au_ico = ImageTk.PhotoImage(Image.open('icos/13a_ico.png'))
#Обновление переменных
def update_playing():
    global playing
    playing = True
def update_i():
    global current_song
    current_song = songs[i]
#Функции кнопок
def play_func():
    global played
    if playing:
        btn_play.config(image=stop)
        btn_play.config(command=stop_func)
        if current_song == songs[0]:
            if played:
                pygame.mixer.music.load('Media_Player/13aurora - red crystal castles.mp3')
                pygame.mixer.music.play()
                played = False
            if played == False:
                pygame.mixer.music.unpause()
        elif current_song == songs[1]:
            if played:
                pygame.mixer.music.load('Media_Player/Mr. Kitty - After Dark.mp3')
                pygame.mixer.music.play()
                played = False
            if played == False:
                pygame.mixer.music.unpause()
        elif current_song == songs[2]:
            if played:
                pygame.mixer.music.load('Media_Player/Молчат Дома - Клетка.mp3')
                pygame.mixer.music.play()
                played = False
            if played == False:
                pygame.mixer.music.unpause()
def nextsong():
    global i
    global played
    i+=1
    played = True
    pygame.mixer.music.pause()
    btn_play.config(image=play,command=btn_play_func)
    if i>2:
        i=0
def previoussong():
    global i
    global played
    i-=1
    played = True
    pygame.mixer.music.pause()
    btn_play.config(image=play,command=btn_play_func)
    if i<0:
        i=2
def stop_func():
    global playing
    btn_play.config(image=play)
    pygame.mixer.music.pause()
    playing = True
    btn_play.config(command=btn_play_func)
#Дебаг
def debug():
    print(playing)
    print(played)
    print(i)
#Картинка песни
current_song_image = [au_ico,mk_ico,md_ico]
song_ico = Label(root,image=current_song_image[i])
def song_ico_change():
    if current_song == songs[0]:
        song_ico.config(image=current_song_image[0])
    elif current_song == songs[1]:
        song_ico.config(image=current_song_image[1])
    elif current_song == songs[2]:
        song_ico.config(image=current_song_image[2])
    root.after(100,song_ico_change)
song_ico_change()
#Название песни
song_name = Label(root,text=songs[i])
def song_name_change():
    if current_song == songs[0]:
        song_name.config(text=songs[0])
    elif current_song == songs[1]:
        song_name.config(text=songs[1])
    elif current_song == songs[2]:
        song_name.config(text=songs[2])
    root.after(100,song_name_change)
song_name_change()
#Функции кнопок(совмещённые)
def btn_play_func():
    update_playing()
    play_func()
def btn_nextsong_func():
    nextsong()
    update_i()
def btn_previoussong_func():
    previoussong()
    update_i()
#Кнопки
btn_play = Button(root,image=play,borderwidth=0,command=btn_play_func)
btn_play.place(x=400,y=200)
btn_nextsong = Button(root,image=next_song,borderwidth=0,command=btn_nextsong_func)
btn_nextsong.place(x=600,y=200)
btn_previoussong = Button(root,image=previous_song,borderwidth=0,command=btn_previoussong_func)
btn_previoussong.place(x=200,y=200)
btn_close = Button(root,image=quit_img,borderwidth=0,command=quit)
btn_close.pack(anchor=NW)
song_ico.place(x=375,y=50)
song_name.place(x=375,y=150)
#Цикл программы
root.mainloop()
