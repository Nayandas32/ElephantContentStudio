import customtkinter as ctk

from ui.components.card import Card

from ui.components.theme import FONT


class Dashboard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        self.build()

    def build(self):

        title = ctk.CTkLabel(

            self,

            text="Dashboard",

            font=(FONT,28,"bold")

        )

        title.pack(anchor="w",padx=25,pady=(20,10))

        top = ctk.CTkFrame(self,fg_color="transparent")

        top.pack(fill="x",padx=20)

        for text in [

            "Total Videos",

            "Uploaded",

            "Pending",

            "Failed"

        ]:

            card = Card(top,width=220,height=120)

            card.pack(side="left",padx=10,pady=10)

            card.pack_propagate(False)

            lbl = ctk.CTkLabel(

                card,

                text=text,

                font=(FONT,16,"bold")

            )

            lbl.pack(pady=(20,5))

            value = ctk.CTkLabel(

                card,

                text="0",

                font=(FONT,30)

            )

            value.pack()