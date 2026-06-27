import customtkinter as ctk

class AnalyticsPage(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        ctk.CTkLabel(

            self,

            text="Analytics\n\nComing Soon",

            font=("Segoe UI",28,"bold")

        ).pack(expand=True)