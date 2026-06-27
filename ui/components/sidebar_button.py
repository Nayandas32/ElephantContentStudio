import customtkinter as ctk

from ui.components.theme import PRIMARY,HOVER,FONT


class SidebarButton(ctk.CTkButton):

    def __init__(self,parent,text,command=None):

        super().__init__(

            parent,

            text=text,

            height=42,

            anchor="w",

            corner_radius=8,

            fg_color="transparent",

            hover_color=HOVER,

            font=(FONT,14),

            command=command

        )

    def activate(self):

        self.configure(fg_color=PRIMARY)

    def deactivate(self):

        self.configure(fg_color="transparent")