#Importacion de librerias
import requests

class comprobacion:
    def comprobacion_pagina(self, url):
        self.url = url
        response = requests.get(url)
        
        try:   
            if response.ok:
                return True
            else:
                return False
        except(requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
            return "Falla.... No se logro la conexion con la pagina web:{}".format(e)
        except Exception as e:
            return "Falla.... Error desconocido:{}".format(e)