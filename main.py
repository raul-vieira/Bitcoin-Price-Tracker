from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image

# importing
import requests
import json
# colors:
co0 = '#444466' # Black
co1 = '#feffff' # White
co2 = '#6f9fbd' # Blue
background = '#484f60'

# creating window:
janela = Tk()
janela.title('')
janela.geometry('380x300')
janela.configure(bg=background)

# creating window frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1, ipadx=157)

frame_superior = Frame(janela, width=380, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_superior.grid(row=1,column=0)

frame_inferior = Frame(janela, width=340, height=350, bg=background, pady=0, padx=0, relief='flat')
frame_inferior.grid(row=2,column=0)

# function to get data
def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL'
    # http request
    response = requests.get(api_link)

    # converting data on dictionary
    data = response.json()

    # USD price
    usd_value = float(data['USD'])
    usd_value_format = '$ {:,.3f}'.format(usd_value)
    l_price_usd['text'] = usd_value_format

    # EUR price
    eur_value = float(data['EUR'])
    eur_value_format = '€ {:,.3f}'.format(eur_value)
    l_price_eur['text'] = eur_value_format

    # BRL price
    brl_value = float(data['BRL'])
    brl_value_format = 'R$ {:,.3f}'.format(brl_value)
    l_price_brl['text'] = brl_value_format

    frame_inferior.after(1000, info) 

# superior frame config
image = Image.open('images/iconbitcoin.png')
image = image.resize((40,40),Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

l_icon = Label(frame_superior, image=image, compound=LEFT, bg=co1, relief=FLAT)
l_icon.place(x=10, y=3)

l_name = Label(frame_superior, text= 'Bitcoin Price Tracker', bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Roboto 25'))
l_name.place(x=60, y=3)

# inferior frame config
l_price_usd = Label(frame_inferior, text='', bg=background, fg=co1, relief=FLAT, anchor='center', font=('Roboto 40'))
l_price_usd.place(x=20, y=50)

l_price_eur = Label(frame_inferior, text= '', bg=background, fg=co1, relief=FLAT, anchor='center', font=('Roboto 25'))
l_price_eur.place(x=20, y=130)

l_price_brl = Label(frame_inferior, text= '', bg=background, fg=co1, relief=FLAT, anchor='center', font=('Roboto 25'))
l_price_brl.place(x=20, y=180)

info()

janela.mainloop()

