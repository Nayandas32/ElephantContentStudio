import customtkinter as ctk

from ui.components.sidebar_button import SidebarButton


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, page_callback):

        super().__init__(
            parent,
            width=230,
            corner_radius=0
        )

        self.page_callback = page_callback
        self.buttons = {}

        self.grid_propagate(False)

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="🐘 Elephant",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(pady=(30, 40))

        # ==========================
        # Menu Items
        # ==========================

        menu_items = [

            ("dashboard", "🏠 Dashboard"),

            ("downloader", "📥 Downloader"),

            ("uploader", "📤 Uploader"),

            ("scheduler", "📅 Scheduler"),

            ("metadata", "📝 Metadata"),

            ("analytics", "📊 Analytics"),

            ("settings", "⚙ Settings")

        ]

        for page_name, text in menu_items:

            btn = SidebarButton(

                self,

                text=text,

                command=lambda p=page_name: self.select_page(p)

            )

            btn.pack(

                fill="x",

                padx=15,

                pady=6

            )

            self.buttons[page_name] = btn

        # প্রথমে Dashboard Active থাকবে

        self.activate_button("dashboard")

        # ==========================
        # Version
        # ==========================

        version = ctk.CTkLabel(

            self,

            text="v0.1 Alpha"

        )

        version.pack(

            side="bottom",

            pady=20

        )

    # =====================================================

    def select_page(self, page_name):

        self.activate_button(page_name)

        self.page_callback(page_name)

    # =====================================================

    def activate_button(self, active_page):

        for page, button in self.buttons.items():

            if page == active_page:

                button.activate()

            else:

                button.deactivate()