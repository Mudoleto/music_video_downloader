import tkinter as tk
from tkinter import ttk

from util.verificador_pagina import comprobacion
from util.descargador_audio import descargarAudio
from util.descargador_video import descargarVideo

class InterfazGrafica(ttk.Frame):
    
    def Descargar(self, mp3, video, url_entry):
        self.url = url_entry.get()
        self.mp3 = mp3
        self.video = video
        
        descargar_audio = video.get()
        descargar_video = mp3.get()
        
        verificacion = comprobacion()
        verificacion = verificacion.comprobacion_pagina(self.url)
        
        print(descargar_audio, descargar_video, verificacion)
                
        if descargar_video and descargar_audio and verificacion == True:
            _descargar_audio = descargarAudio()
            _descargar_audio = _descargar_audio.mp3(self.url)
            _descargar_video = descargarVideo()
            _descargar_video = _descargar_video.mp4(self.url)
            
            
        elif descargar_video == False and descargar_audio and verificacion == True:
            _descargar_audio = descargarAudio()
            _descargar_audio = _descargar_audio.mp3(self.url)
            
            
        elif descargar_video and verificacion == True and descargar_audio == False:
            _descargar_video = descargarVideo()
            _descargar_video = _descargar_video.mp4(self.url)
            
        
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Mudo: audio y video")
        main_window.geometry('300x250')
        
        url_video = ttk.Label(master=main_window, text="Ingresa URL", font="Calibri 12 bold")
        url_video.pack() 
        
        input_frame = ttk.Frame(master=main_window)
        input_frame.pack(pady=10)
        
        entry = ttk.Entry(master=input_frame, width=25)
        entry.pack(side='left', padx=10)
        
        self.checkbox_mp3_value = tk.BooleanVar(self)
        checkbox_mp3 = ttk.Checkbutton(master=main_window, text = "MP3", variable=self.checkbox_mp3_value)
        checkbox_mp3.place(x=40, y=70)
        
        self.checkbox_video_value = tk.BooleanVar(self)
        checkbox_video = ttk.Checkbutton(master=main_window, text="video", variable=self.checkbox_video_value)
        checkbox_video.place(x=40, y=90)
        
        button = ttk.Button(master=input_frame, text="Descargar", command=lambda: self.Descargar(self.checkbox_video_value, self.checkbox_mp3_value, entry))
        button.pack(side='left')

main_window = tk.Tk()
app = InterfazGrafica(main_window)
app.mainloop()