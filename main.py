from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import Tk
from tkinter.filedialog import askdirectory
import glob
from fpdf import FPDF
import configparser
from time import sleep

fileconf = configparser.ConfigParser()
fileconf.read('UserData.ini', encoding='utf-8')
sub_ip = int(input('Enter sublist:'))
g_ip = input('Enter group:')
Tk().withdraw()
print('Please select the folder containing files')
root = Tk()
root.withdraw()
root.attributes('-topmost', True)
filename = askdirectory(parent=root)
chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
#screen shot section
for i in range(97,102):
    URL = f'http://www.englishvocabularyexercises.com/AWL/AWLSublist{sub_ip:02d}-Ex{g_ip}{chr(i)}.htm'
    driver.get(URL)
    f = open('script.js', 'r')
    driver.execute_script(f.read())

    driver.save_screenshot(filename+f'/{chr(i)}.png')
driver.quit()

#pdf section
imagelist = glob.glob(f'{filename}/*.png')
pdf = FPDF()
x = int(fileconf.get('filename', 'x'))
y = int(fileconf.get('filename', 'y'))
fname = fileconf.get('filename', 'studentID')+' '+fileconf.get('filename', 'name')
if fileconf.get('filename', 'watermark') == '0':
    for image in imagelist:
        print('.',end='')
        pdf.add_page(image)
        pdf.image(image, x, y, 0)
        sleep(0.02)
else:
    for image in imagelist:
        print('.',end='')
        pdf.add_page(image)
        pdf.image(image, x, y, 0)
        pdf.set_font('Arial', 'B', 16)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 35, f"{fname}")
        sleep(0.02)
if fileconf.get('filename', 'display_week') == '1':
    pdf.output(f"{filename}/{fname} week{sub_ip}.pdf", "F")
else:
    pdf.output(f"{filename}/{fname}.pdf", "F")
print('\n Done!!!')