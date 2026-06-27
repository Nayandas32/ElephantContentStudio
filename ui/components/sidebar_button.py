import customtkinter as ctk

from ui.components.theme import (
    PRIMARY,
    HOVER,
    TEXT,
    FONT
)


class SidebarButton(ctk.CTkButton):

    def __init__(self, parent, text, command=None):

        super().__init__(
            parent,

            text=text,

            command=command,

            height=42,

            anchor="w",

            corner_radius=8,

            fg_color="transparent",

            hover_color=HOVER,

            text_color=TEXT,

            font=(FONT, 14),

            border_width=0
        )

        self.is_active = False

    # ===========================
    # Active Button
    # ===========================

    def activate(self):

        self.is_active = True

        self.configure(

            fg_color=PRIMARY,

            hover_color=PRIMARY

        )

    # ===========================
    # Normal Button
    # ===========================

    def deactivate(self):

        self.is_active = False

        self.configure(

            fg_color="transparent",

            hover_color=HOVER

        )