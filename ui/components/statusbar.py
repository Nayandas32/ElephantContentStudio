import customtkinter as ctk

from ui.components.theme import STATUS,TEXT_SECONDARY,FONT


class StatusBar(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(

            parent,

            height=28,

            fg_color=STATUS,

            corner_radius=0

        )

        self.pack_propagate(False)

        self.label = ctk.CTkLabel(

            self,

            text="Ready | Database : Connected | v0.1 Alpha",

            font=(FONT,11),

            text_color=TEXT_SECONDARY

        )

        self.label.pack(side="left",padx=15)