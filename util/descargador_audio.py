from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

class descargarAudio:
    def mp3(self, url):
        self.url = url

        try:
            if self.url:
                yt = YouTube(url, on_progress_callback = on_progress)
                print(yt.title)
                ys = yt.streams.get_audio_only()
                output_path = os.path.join("Descargas", "music")
                ys.download(output_path=output_path,mp3=True)
        except:
            print("No se logro descargar la musica")