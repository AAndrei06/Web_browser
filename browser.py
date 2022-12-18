from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon,QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import tkinter

error = False
bg_color_for_settings = "#D2D2D2"
fg_color_for_settings = "black"


class MyWebBrowser(QMainWindow):

	def __init__(self):
		super().__init__()

		self.home_url = 'http://www.google.com'

		self.style = """
					"""
					
		self.font = QFont("Arial Black",12)
		self.font_back_forward = QFont("consolas",16)

		self.window = QWidget()
		self.window.setWindowTitle("Arseni\'s Browser")

		self.layout = QVBoxLayout()
		self.horizontal = QHBoxLayout()

		self.url_bar = QTextEdit()
		self.url_bar.setMaximumHeight(30)
		self.url_bar.setFont(QFont("Arial",11))
		self.url_bar.setMaximumHeight(32)
		self.url_bar.setObjectName("url_bar_id")
		self.url_bar.setPlaceholderText('🔍 Search...')

		self.search_button = QPushButton('🔍')
		self.search_button.setMaximumHeight(35)
		self.search_button.setMinimumWidth(42)
		self.search_button.setMaximumWidth(45)
		self.search_button.setFont(self.font)
		self.search_button.setObjectName("search_button_id")

		self.settings_button = QPushButton('⚙')
		self.settings_button.setMaximumHeight(35)
		self.settings_button.setMinimumWidth(38)
		self.settings_button.setMaximumWidth(40)	
		self.settings_button.setFont(self.font)
		self.settings_button.setObjectName("settings_button_id")

		self.back_button = QPushButton("<")
		self.back_button.setMinimumHeight(20)
		self.back_button.setMinimumWidth(38)
		self.back_button.setMaximumWidth(40)
		self.back_button.setFont(self.font_back_forward)

		self.forward_button = QPushButton(">")
		self.forward_button.setMinimumHeight(25)
		self.forward_button.setMinimumWidth(38)
		self.forward_button.setMaximumWidth(40)
		self.forward_button.setFont(self.font_back_forward)

		self.refresh_button = QPushButton("🗘")
		self.refresh_button.setMaximumWidth(39)
		self.refresh_button.setMinimumWidth(36)
		self.refresh_button.setMaximumHeight(35)
		self.refresh_button.setFont(QFont("Arial Black",14))

		self.home_button = QPushButton('🏠')
		self.home_button.setMinimumWidth(38)
		self.home_button.setMaximumWidth(40)
		self.home_button.setMaximumHeight(35)
		self.home_button.setFont(QFont("consolas",14))

		self.horizontal.addWidget(self.back_button)
		self.horizontal.addWidget(self.forward_button)
		self.horizontal.addWidget(self.refresh_button)
		self.horizontal.addWidget(self.home_button)
		self.horizontal.addWidget(self.url_bar)
		self.horizontal.addWidget(self.search_button)
		self.horizontal.addWidget(self.settings_button)

		self.browser = QWebEngineView()

		self.copyright = QLabel()
		self.copyright.setText("	© 2022 Arseni\'s Software CEO - Arseni Andrei")
		self.copyright.setObjectName("copyright_id")
		self.copyright.setMaximumHeight(11)

		self.layout.addLayout(self.horizontal)
		self.layout.addWidget(self.browser)
		self.layout.addWidget(self.copyright)

		self.browser.setUrl(QUrl("http://google.com"))

		self.search_button.clicked.connect(lambda: self.search_url(self.url_bar.toPlainText()))
		self.back_button.clicked.connect(self.browser.back)
		self.forward_button.clicked.connect(self.browser.forward)
		self.home_button.clicked.connect(self.go_home)
		self.refresh_button.clicked.connect(self.browser.reload)
		self.settings_button.clicked.connect(self.settings_window)

		self.window.setLayout(self.layout)
		self.window.show()

	def search_url(self,url):
		if not url.startswith("http://"):
			url = "http://"+url

		self.url_bar.setText(url)
		self.browser.setUrl(QUrl(url))

	def go_home(self):
		self.browser.setUrl(QUrl(self.home_url))
		self.url_bar.setText(" ")

	def google_change(self):
		self.home_url = 'http://google.com'

	def bing_change(self):
		self.home_url = 'http://bing.com'

	def duck_change(self):
		self.home_url = 'http://duck.com'

	def yahoo_change(self):
		self.home_url = 'http://yahoo.com'

	def change_theme_light(self):
		self.style = """
						QWidget{
						background-color: #F5F5F5;
							}
						QPushButton
						{

						background-color: #E8E8E8;
						border: 1px solid black;
						border-radius: 4px;

						}

						QTextEdit#url_bar_id
						{
							background-color: #E8E8E8;
							border: 1px solid black;
							border-radius: 5px;

						}
						QPushButton:hover{

							background-color:  lightblue;
						}

					"""

		self.window.setStyleSheet(self.style)

	def change_theme_dark(self):
		self.style = """
						QWidget{
						background-color: #27272E;
							}
						QPushButton
						{

						background-color: #A5A5A5;
						border: 1px solid #050505;
						border-radius: 4px;

						}

						QTextEdit#url_bar_id
						{
							background-color: #A5A5A5;
							border: 1px solid #050505;
							border-radius: 5px;

						}
						QPushButton:hover{

							background-color:  white;
						}
						QLabel#copyright_id
						{
							color: white;

						}

					"""

		self.window.setStyleSheet(self.style)

	def change_theme_hacker(self):
		self.style = """
						QWidget{
						background-color: #1D1D1D;
							}
						QPushButton
						{

						background-color: #78006E;
						border: 1px solid #00980B;
						border-radius: 4px;

						}

						QTextEdit#url_bar_id
						{
							background-color: #1D1D1D;
							border: 1px solid #00980B;
							border-radius: 5px;
							color: #00980B;

						}
						QPushButton:hover{

							background-color:  green;

						}
						QLabel#copyright_id
						{
							color: white;

						}

					"""

		self.window.setStyleSheet(self.style)

	def change_theme_vintage(self):

		self.style = """
						QWidget{
						background-color: #F2EECB;
							}
						QPushButton
						{

						background-color: #9BC756;
						border: 1px solid #F8DC43;
						border-radius: 4px;

						}

						QTextEdit#url_bar_id
						{
							background-color: #D2FA95;
							border: 1px solid #F8DC43;
							border-radius: 5px;

						}
						QPushButton:hover{

							background-color:  #E7FAAD;

						}

					"""

		self.window.setStyleSheet(self.style)

	def settings_window(self):
		settings_window = tkinter.Tk()
		settings_window.title("Browser's Settings")
		settings_window.geometry("700x800")
		try:
			icon = tkinter.PhotoImage(file = "web_icon.png")
			settings_window.iconphoto(False,icon)
			settings_window.configure(bg = bg_color_for_settings)
		except:
			settings_window.configure(bg = bg_color_for_settings)

		title_of_page = tkinter.Label(settings_window,fg = fg_color_for_settings,font = ("Arial Black",35,"bold"),text = "Setările browserului:",bg = bg_color_for_settings)
		title_of_page.place(x = 20,y = 40)
		title1 = tkinter.Label(settings_window,fg = fg_color_for_settings,font = ("Arial",20,"bold"),text = "Alege Motorul de Căutare:",bg = bg_color_for_settings)
		title1.place(x = 60,y = 150)
		google_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "red",text = "Google",command = self.google_change,bg = "#DBDBDB")
		google_button.place(x = 80,y = 220)
		bing_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "blue",text = "Microsoft Bing",command = self.bing_change,bg = "#DBDBDB")
		bing_button.place(x = 188,y = 220)
		duck_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "#FFFFFF",text = "DuckDuckGo",command = self.duck_change,bg = "#FF4902")
		duck_button.place(x = 380,y = 220)
		yahoo_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "white",text = "Yahoo!",command = self.yahoo_change,bg = "purple")
		yahoo_button.place(x = 530,y = 220)

		title2 = tkinter.Label(settings_window,fg = fg_color_for_settings,font = ("Arial",20,"bold"),text = "Alege o temă:",bg = bg_color_for_settings)
		title2.place(x = 60, y = 320)
		theme1_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "#011C45",bg = "#FFFFFF",text = "*Luminoasă*",command = self.change_theme_light)
		theme1_button.place(x = 80,y = 410)
		theme2_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "#011C45",bg = "#535353",text = "☻Întunecată☻",command = self.change_theme_dark)
		theme2_button.place(x = 230,y = 410)
		theme3_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "#359E01",bg = "black",text = "</Hacker>",command = self.change_theme_hacker)
		theme3_button.place(x = 390,y = 410)
		theme4_button = tkinter.Button(settings_window,font = ("consolas",12,"bold"),fg = "#00095E",bg = "#AE9939",text = "~Vintage~",command = self.change_theme_vintage)
		theme4_button.place(x = 515,y = 410)

		thanks = tkinter.Label(settings_window,bg = bg_color_for_settings,fg = fg_color_for_settings,font = ("Arial Black",55,"bold"),text = "Îți mulțumim\ncă folosești\nacest browser!\n😊")
		thanks.place(x = 800,y = 200)

		title3 = tkinter.Label(settings_window, fg = fg_color_for_settings, font = ("Arial",18,"bold"),text = "Contactați dezvolatorul:",bg = bg_color_for_settings)
		title3.place(x = 60,y = 550)
		contact1 = tkinter.Label(settings_window, fg = fg_color_for_settings, font = ("consolas",14,"bold"),text = "Instagram: andrei.arseni.127\n\nFacebook: Andrei Arseni    \n\nGmail: andreiarsenii90@gmail.com",bg = bg_color_for_settings)
		contact1.place(x = 80,y = 600)
		copyright_set = tkinter.Label(settings_window,fg = fg_color_for_settings,font = ("consolas",10,"bold"),text = "	© 2022 Arseni\'s Software CEO - Arseni Andrei",bg = bg_color_for_settings)
		copyright_set.place(x = 40,y = 770)
		settings_window.mainloop()

app = QApplication([])

window = MyWebBrowser()

try:
	icon = QIcon("web_icon.png")
	app.setWindowIcon(icon)
except:
	error = True
app.exec_()





