import customtkinter as ctk

class DownloaderPage(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        ctk.CTkLabel(

            self,

            text="Downloader\n\nComing Soon",

            font=("Segoe UI",28,"bold")

        ).pack(expand=True)