import yt_dlp
from pathlib import Path
from tkinter import messagebox


class DownloadService:

    def __init__(self):

        self.project = None

    def set_project(self, project):

        self.project = project

    def get_project_folder(self):

        folder = Path("projects") / self.project[1] / "downloads"

        folder.mkdir(parents=True, exist_ok=True)

        return folder

    def download(self, url):

        if "&list=" in url:
         url = url.split("&list=")[0]

        folder = self.get_project_folder()

        ydl_opts = {

            "format": "bestvideo+bestaudio/best",

            "merge_output_format": "mp4",

            "outtmpl": str(folder / "%(title)s.%(ext)s"),

            "noplaylist": True,
            

            "quiet": False
            

        }

        try:
         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])

        except Exception as e:
         print(e)
        messagebox.showerror(
        "Download Error",
        str(e)
     )
           