from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

class descargarVideo:
    def mp4(self, url):
        self.url = url
        try:
            if self.url:
                yt = YouTube(url, on_progress_callback=on_progress)
                print(yt.title)
                ys = yt.streams.get_highest_resolution()
                output_path = os.path.join("Descargas", "video")
                ys.download(output_path=output_path)
        except:
            print("No se logro descargar el video")
        