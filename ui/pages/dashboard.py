import customtkinter as ctk
from tkinter import messagebox

from ui.components.card import Card
from ui.components.theme import FONT

from core.database import DatabaseManager


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.db = DatabaseManager()

        self.build()

        self.load_projects()

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

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )

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

            lbl = ctk.CTkLabel(
                card,
                text=title_text,
                font=(FONT, 16, "bold")
            )

            lbl.pack(
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

        project_card = Card(self)

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
        # Scrollable Project List
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
            # ==================================================
    # Create New Project Window
    # ==================================================

    def new_project(self):

        win = ctk.CTkToplevel(self)

        win.title("Create New Project")

        win.geometry("450x320")

        win.resizable(False, False)

        win.grab_set()

        # -----------------------------
        # Title
        # -----------------------------

        title = ctk.CTkLabel(
            win,
            text="Create New Project",
            font=(FONT, 22, "bold")
        )

        title.pack(
            pady=(20, 20)
        )

        # -----------------------------
        # Project Name
        # -----------------------------

        name_label = ctk.CTkLabel(
            win,
            text="Project Name",
            font=(FONT, 15)
        )

        name_label.pack(anchor="w", padx=30)

        name_entry = ctk.CTkEntry(
            win,
            width=360,
            placeholder_text="Example: Gopal Bhar Season 1"
        )

        name_entry.pack(
            padx=30,
            pady=(5, 15)
        )

        # -----------------------------
        # Description
        # -----------------------------

        desc_label = ctk.CTkLabel(
            win,
            text="Description",
            font=(FONT, 15)
        )

        desc_label.pack(anchor="w", padx=30)

        desc_entry = ctk.CTkTextbox(
            win,
            width=360,
            height=90
        )

        desc_entry.pack(
            padx=30,
            pady=(5, 20)
        )

        # -----------------------------
        # Buttons
        # -----------------------------

        button_frame = ctk.CTkFrame(
            win,
            fg_color="transparent"
        )

        button_frame.pack(fill="x", padx=30)

        cancel_btn = ctk.CTkButton(
            button_frame,
            text="Cancel",
            width=120,
            fg_color="gray40",
            command=win.destroy
        )

        cancel_btn.pack(
            side="left"
        )

        create_btn = ctk.CTkButton(
            button_frame,
            text="Create Project",
            width=160,
            command=lambda: self.create_project(
                win,
                name_entry.get(),
                desc_entry.get("1.0", "end").strip()
            )
        )

        create_btn.pack(
            side="right"
        )
            # ==================================================
    # Create Project
    # ==================================================

    def create_project(
        self,
        window,
        name,
        description
    ):

        name = name.strip()

        if not name:

            messagebox.showwarning(
                "Project",
                "Project name cannot be empty."
            )

            return

        try:

            self.db.create_project(
                name,
                description
            )

            window.destroy()

            self.load_projects()

            messagebox.showinfo(
                "Success",
                "Project created successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==================================================
    # Load Projects
    # ==================================================

    def load_projects(self):

        for widget in self.project_list.winfo_children():

            widget.destroy()

        projects = self.db.get_projects()

        if len(projects) == 0:

            empty = ctk.CTkLabel(

                self.project_list,

                text="No project created yet.",

                font=(FONT,18)

            )

            empty.pack(
                pady=40
            )

            return

        for project in projects:

            project_id = project[0]
            project_name = project[1]
            created_at = project[3]

            row = Card(
                self.project_list,
                height=70
            )

            row.pack(
                fill="x",
                padx=5,
                pady=5
            )

            row.pack_propagate(False)

            info = ctk.CTkFrame(
                row,
                fg_color="transparent"
            )

            info.pack(
                side="left",
                padx=15,
                pady=10,
                expand=True,
                fill="both"
            )

            ctk.CTkLabel(

                info,

                text=project_name,

                font=(FONT,18,"bold")

            ).pack(
                anchor="w"
            )

            ctk.CTkLabel(

                info,

                text=f"Created : {created_at}",

                font=(FONT,12)

            ).pack(
                anchor="w"
            )

            delete_btn = ctk.CTkButton(

                row,

                text="🗑 Delete",

                width=110,

                fg_color="#c0392b",

                hover_color="#922b21",

                command=lambda pid=project_id: self.delete_project(pid)

            )

            delete_btn.pack(
                side="right",
                padx=15
            )

    # ==================================================
    # Delete Project
    # ==================================================

    def delete_project(
        self,
        project_id
    ):

        answer = messagebox.askyesno(

            "Delete Project",

            "Are you sure you want to delete this project?"

        )

        if not answer:

            return

        try:

            self.db.delete_project(project_id)

            self.load_projects()

        except Exception as e:

            messagebox.showerror(

                "Error",

                str(e)

            )