import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent,width=230,corner_radius=0)

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="🐘 Elephant",
            font=("Segoe UI",24,"bold")
        )

        title.pack(pady=(30,40))

        buttons = [

            "🏠 Dashboard",
            "📥 Downloader",
            "📤 Uploader",
            "📅 Scheduler",
            "📝 Metadata",
            "📊 Analytics",
            "⚙ Settings"

        ]

        for text in buttons:

            btn = ctk.CTkButton(

                self,

                text=text,

                height=42,

                anchor="w"

            )

            btn.pack(fill="x",padx=15,pady=6)

        version = ctk.CTkLabel(

            self,

            text="v0.1 Alpha"

        )

        version.pack(side="bottom",pady=20)