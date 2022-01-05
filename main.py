
from keep_alive import keep_alive

import csv
import gspread
from datetime import datetime
from datetime import timedelta
import time
#from oauth2client.service_account import service_account
#import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd
#import lxml

from PIL import Image
import time
import requests
from datetime import date      

from PIL import GifImagePlugin    

def evalua(x,y,im):
    
    image = Image.open(im)
    #box = (390, 630, 420, 660)
    box = (x, y, x+30, y+30)
    region = image.crop(box)


    pixval = list(region.getdata())
    fuerza = 0
    for i in range(0, 900 ):
          if pixval[i]<105 and pixval[i]>86 and pixval[i]!=93 and pixval[i]!=92 and pixval[i]!=91 and pixval[i]!=103 and pixval[i]!=90 and pixval[i]!=89 and pixval[i]!=101 and pixval[i]!=102:

              fuerza = fuerza +1
    #region.show()
    print(fuerza)
    if fuerza > 55:
        print("tormenta")
        #print(pixval)
        print(name)
      
        imageObject.save(name)    
        #region.show()

        mensaje()
        time.sleep(1800)           
        
        
    else:
        print("Sin Novedad") 

def abanico(xi,yi,imi):
    im=imi
    abajo=0
    costado = 0
    for abajo in range (-5,1):
        x= xi + (abajo*15)
        for costado  in range (-6,6): 
            y = yi + (costado*15)
            print("coordinadas")
            print(x,y)
            if x==223 and y==213:
                DCDC=1
            else:
                evalua(x,y,im)




def mensaje():
    import requests

    idBot = '5005183215:AAEq_uzhLr5iBuE1Seu-A19QUwOVvrHp2mE'
    idGrupo = '-789912637'

    def enviarMensaje(mensaje):
        requests.post('https://api.telegram.org/bot' + idBot + '/sendMessage',
                  data={'chat_id': idGrupo, 'text': mensaje, 'parse_mode': 'HTML'})

    enviarMensaje("Alerta de Tormenta")
    enviarMensaje("https://www2.contingencias.mendoza.gov.ar/radar/animacion.gif")






keep_alive()

while True:
  try:

      today = round(time.time())
      
      name =  str(today)+".gif"

      print(name)

      img_data = requests.get("https://www2.contingencias.mendoza.gov.ar/radar/animacion.gif").content

      
      with open("temporal.gif", 'wb') as handler:
          handler.write(img_data)

          
      
      imageObject = Image.open("temporal.gif")
      print(imageObject.is_animated)
      print(imageObject.n_frames)


      for frame in range(imageObject.n_frames-1,imageObject.n_frames):
        imageObject.seek(frame)        

        #UNIC = "c:\\Users\\Eduardo\\SCRIPTS\\CONTINGENCIAS\\IMAGE\\"+str(name)
        imageObject.save("UNICO.gif")    


        abanico(283,243,"UNICO.gif")
        time.sleep(300)   
  except:
    a=1