
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 
from requests import get 
from PIL import Image,ImageTk
from datetime import datetime 
import os , time , sys
import requests
import urllib.request
from style import Style
from help.contact_developer import Help

class Main:
    def __init__(self,root):
        self.URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        self.API = '06051f3cad0ad7ba821ba795bf6d124f'
        self.root = root
        self.variable_city = StringVar()
        self.object_style = Style(self.root)
        self.object_help = Help(self.root)

        # return function show_errors

        #--------- create button get information weather --------------------
        self.image_get_date = Image.open('images\\get_data.png')
        self.insert_image_get_date = ImageTk.PhotoImage(self.image_get_date)





        #----------- create Entry get date -----------------------------------

        self.entry_data = Entry(
            self.root , background='#404040' ,font=('poppins',22) , bg='#404040',
            border=0,justify='center',fg='white' , textvariable=self.variable_city
        ).place(x=240,y=150)

        self.button = Button(
            self.root, image=self.insert_image_get_date,
            background='#404040', borderwidth=0, activebackground='#404040',command=self.check_connection

        ).place(x=560, y=140)





    def check_connection(self):
        """Verify the device is connected to the Internet"""
        self.url_website = 'https://openweathermap.org/'
        self.timeout = 5
        try :
            request = requests.get(self.url_website, timeout=self.timeout)
            if request :
                self.check_city()
                self.get_date()

        except (requests.ConnectionError, requests.Timeout) as exception:
            pass




    def check_city(self):
        """Check the entered value if it is empty"""
        self.label_error = Label(self.root  , fg='red',font=('bold',17) , width=30)
        self.label_error.place(x=200,y=215)

        if self.variable_city.get() == '':
            self.label_error['text'] = 'The field cannot be left blank'

        else :
            self.label_error['text'] = ''



    def get_date(self):
        """The Function Get Data And , Verify the device is connected to the Internet"""

        self.url_api = requests.get(self.URL.format(self.variable_city.get(),self.API))
        if self.url_api :
            self.jsonData = self.url_api.json()
            self.city = self.jsonData['name']
            self.country = self.jsonData['sys']['country']

            self.temp_klv = self.jsonData['main']['temp']
            self.temp_celcuis = (self.temp_klv - 273.15)
            self.temp_fehr = (self.temp_klv - 273.15) * 9 / 5 + 32
            self.weather = self.jsonData['weather'][0]['main']
            self.pressure = self.jsonData['main']['pressure']
            self.description = self.jsonData['weather'][0]['description']
            self.humidity = self.jsonData['main']['humidity']

            self.final_result = (
                self.city, self.country, self.temp_klv, self.temp_celcuis,
                self.temp_fehr, self.weather, self.pressure, self.description, self.humidity

            )
            if self.final_result :
                self.show_data()


    def show_data(self):
        self.object_style.l1['text'] = self.final_result[0] + '-' + self.final_result[1]
        self.object_style.l2['text'] = ('{:.0f}°C , {:.0f}°F'.format(self.final_result[3],self.final_result[4]))
        self.object_style.l3['text'] = self.final_result[6]
        self.object_style.l4['text'] = self.final_result[7]
        self.object_style.l5['text'] = self.final_result[8]


        self.label_weather_now = Label(
            self.root , text="TODAY'S WEATHER", font=('Helvetica', 12),
            foreground='#000000'
            ).place(x=170,y=260)

        self.label_temp_celcuis = Label(self.root, font=('poppins', 25), fg='red',
                                        text='{:.0f}°C'.format(self.final_result[3]))
        self.label_temp_celcuis.place(x=500, y=300)

        self.current_weather = Label(self.root, text='Weather |', font=('poppins', 12) ,fg='#8255B9')
        self.current_weather.place(x=510, y=370)

        self.label_insert_weather = Label(self.root , font=('poppins', 14)  , fg='#000000' , text='')
        self.label_insert_weather.place(x=590,y=370)

        self.label_insert_weather['text'] = self.final_result[5]


        self.get_icon()


        #--------------------- Add Image Weather Logo ------------------------------------------------------------

    def get_icon(self):
        """Get Icon Current Weather!"""

        self.data = requests.get(self.URL.format(self.variable_city.get(),self.API))
        self.file_josn = self.data.json()
        self.icon = self.file_josn['weather'][0]['icon']
        urllib.request.urlretrieve(f'http://openweathermap.org/img/wn/{self.icon}.png', 'images\\image_weather.png')


        self.image_con = Image.open('images\\image_weather.png')
        self.insert_image_icon = ImageTk.PhotoImage(self.image_con)


        self.label_icon = Label(
            self.root , image=self.insert_image_icon , width=90 , height=60,
            font = ('poppins', 33, 'bold')
        ).place(x=450,y=240)



def main(*args):
    """The Main Function"""
    app = Tk()
    object_main = Main(app)
    app.mainloop()

if __name__=='__main__':
    main()
