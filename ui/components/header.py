import customtkinter as ctk

from ui.components.theme import HEADER,TEXT,FONT


class Header(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(

            parent,

            height=60,

            fg_color=HEADER,

            corner_radius=0

        )

        self.pack_propagate(False)

        title = ctk.CTkLabel(

            self,

            text="🐘 Elephant Content Studio",

            font=(FONT,22,"bold"),

            text_color=TEXT

        )

        title.pack(side="left",padx=20)