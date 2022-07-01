


from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime

class Style :
	""" The class responsible for the appearance
	of the application, adding images and titles """

	def __init__(self,master):
		self.master = master
		self.master.title('Weather Forecast')
		self.master.geometry('814x760+470+70')
		self.master.resizable(width=False,height=False)
		self.master.iconbitmap('images\\title.icon.ico')
	


		# ---------- Create Function Add App Titles ---------------
		self.add_title()
		self.add_time()
		self.add_version()
		self.add_image_search()
		self.add_image_box()
		self.add_labels_titles()
		self.add_image_logo()

		#----------------------------------------------------------

	def add_title(self):
		""" Add Title Frame And ,Add Name Application """
		self.frame = Frame(self.master , background='#AED6F1' ,width=800 , height=80).place(x=6,y=4)
		self.name_app = Label(
			self.frame,text='Weather Forecast',font=('poppins',22),
			bg='#AED6F1',fg='#1C2833').place(x=310,y=16)

		


	def add_time(self):
		""" Function, add time and date """
		self.time = datetime.now()
		self.hour = self.time.strftime('%H:%M:%S %p')

		self.label_hour = Label(self.frame , text=f'{self.hour}',font=('poppins',22) ,bg='#AED6F1',fg='#1C2833').place(x=600,y=16)
		self.master.after(1000,self.add_time)


		# Add The Date 
		self.date = datetime.now()
		self.full_date = self.date.strftime('%Y-%m-%d')
		self.label_date = Label(self.frame,text=f'{self.full_date}',font=('poppins',22) ,bg='#AED6F1',fg='#1C2833').place(x=70,y=16)




	def add_version(self):
		""" The Function Add Label Version """
		self.label = Label(
			self.master , background='#9DBCD9' , width=1030 

			).place(x=0,y=720)
		self.version = Label(self.master,background='#9DBCD9',width=30,text='Version 1.0').place(x=2,y=720)




	def add_image_search(self):
		"""The Function Add Label Search Image"""
		self.image_search = Image.open('images\\search.png')
		self.insert_image_search = ImageTk.PhotoImage(self.image_search)

		self.label_search = Label(
			self.master ,
			width=500 , height=100,
			image=self.insert_image_search ,
			borderwidth=0 
		).place(x=180,y=120)



	def add_image_box(self):
		self.image_box = Image.open('images\\box.png')
		self.insert_image_box = ImageTk.PhotoImage(self.image_box)

		self.label_box = Label(
			self.master , width=800 , height=100 ,
			image=self.insert_image_box , borderwidth=0
		).place(x=14,y=600)



	def add_image_logo(self):
		"""Add Image Logo """
		self.image_logo = Image.open('images\\logo.png')
		self.insert_image_logo = ImageTk.PhotoImage(self.image_logo)

		self.label_image_logo = Label(
			self.master, image=self.insert_image_logo, font=('poppins', 20, 'bold'),

		).place(x=280, y=280)



	def add_labels_titles(self):
		"""The Function Add Titles Labels in Image Box"""
		self.lable_1 = Label(self.master ,  text='Location' , font=('poppins',12,'bold'),background='#1ab5ef',fg='white').place(x=70,y=617)
		self.lable_2 = Label(self.master, text='Temperature', font=('poppins', 12, 'bold'), background='#1ab5ef',
							 fg='white').place(x=200, y=617)

		self.lable_3 = Label(self.master, text='Pressure', font=('poppins', 12, 'bold'), background='#1ab5ef',
							 fg='white').place(x=377, y=617)

		self.lable_4 = Label(self.master, text='Description', font=('poppins', 12, 'bold'), background='#1ab5ef',
							 fg='white').place(x=520, y=617) # Humidity

		self.lable_5 = Label(self.master, text='Humidity', font=('poppins', 12, 'bold'), background='#1ab5ef',
							 fg='white').place(x=670, y=617)  # Humidity



		# # Create Label Result None
		self.l1 = Label(self.master, text='....', font=('poppins', 12, 'bold'), background='#1ab5ef', fg='#000000')
		self.l1.place(x=70, y=645)

		self.l2 = Label(self.master, text='....', font=('poppins', 12, 'bold'), background='#1ab5ef', fg='#000000')
		self.l2.place(x=210, y=645)

		self.l3 = Label(self.master, text='....', font=('poppins', 12, 'bold'), background='#1ab5ef', fg='#000000')
		self.l3.place(x=400, y=645)

		self.l4 = Label(self.master, text='....', font=('poppins', 11, 'bold'), background='#1ab5ef', fg='#000000')
		self.l4.place(x=530, y=645)

		self.l5 = Label(self.master, text='....', font=('poppins', 12, 'bold'), background='#1ab5ef', fg='#000000')
		self.l5.place(x=690, y=645)



