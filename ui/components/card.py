import customtkinter as ctk

from ui.components.theme import CARD,BORDER


class Card(ctk.CTkFrame):

    def __init__(self,parent,**kwargs):

        super().__init__(

            parent,

            fg_color=CARD,

            border_color=BORDER,

            border_width=1,

            corner_radius=15,

            **kwargs

        )