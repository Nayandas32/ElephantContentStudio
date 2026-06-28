import customtkinter as ctk

from ui.components.card import Card
from ui.components.theme import FONT


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.build()

    # ==================================================

    def build(self):

        # -----------------------------
        # Title
        # -----------------------------

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=(FONT, 30, "bold")
        )

        title.pack(anchor="w", padx=25, pady=(20, 10))

        # -----------------------------
        # Statistics
        # -----------------------------

        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=20
        )

        cards = [

            ("📁 Total Projects", "0"),
            ("📹 Total Videos", "0"),
            ("☁ Uploaded", "0"),
            ("⏳ Pending", "0")

        ]

        for title_text, value_text in cards:

            card = Card(
                stats_frame,
                width=220,
                height=120
            )

            card.pack(
                side="left",
                padx=10,
                pady=10
            )

            card.pack_propagate(False)

            title = ctk.CTkLabel(
                card,
                text=title_text,
                font=(FONT, 16, "bold")
            )

            title.pack(
                pady=(18, 5)
            )

            value = ctk.CTkLabel(
                card,
                text=value_text,
                font=(FONT, 30)
            )

            value.pack()

        # -----------------------------
        # Project Section
        # -----------------------------

        project_card = Card(
            self
        )

        project_card.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        header = ctk.CTkFrame(
            project_card,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        lbl = ctk.CTkLabel(
            header,
            text="Recent Projects",
            font=(FONT, 22, "bold")
        )

        lbl.pack(
            side="left"
        )

        new_btn = ctk.CTkButton(
            header,
            text="+ New Project",
            width=160,
            command=self.new_project
        )

        new_btn.pack(
            side="right"
        )

        # -----------------------------
        # Project List
        # -----------------------------

        self.project_list = ctk.CTkScrollableFrame(
            project_card
        )

        self.project_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        empty = ctk.CTkLabel(
            self.project_list,
            text="No project created yet.",
            font=(FONT, 18)
        )

        empty.pack(
            pady=50
        )

    # ==================================================

    def new_project(self):

        win = ctk.CTkToplevel(self)

        win.title("Create Project")

        win.geometry("420x240")

        win.grab_set()

        ctk.CTkLabel(
            win,
            text="Project Name",
            font=(FONT, 18, "bold")
        ).pack(
            pady=(25, 10)
        )

        name_entry = ctk.CTkEntry(
            win,
            width=320
        )

        name_entry.pack()

        ctk.CTkLabel(
            win,
            text="Description"
        ).pack(
            pady=(20, 10)
        )

        desc_entry = ctk.CTkTextbox(
            win,
            width=320,
            height=70
        )

        desc_entry.pack()

        ctk.CTkButton(
            win,
            text="Create",
            width=140,
            command=lambda: self.create_project(
                win,
                name_entry.get(),
                desc_entry.get("1.0", "end").strip()
            )
        ).pack(
            pady=20
        )

    # ==================================================

    def create_project(
        self,
        window,
        name,
        description
    ):

        print(name)

        print(description)

        window.destroy()