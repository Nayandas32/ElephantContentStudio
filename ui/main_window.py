"""
Elephant Content Studio

Version : v0.1.2B Commit 2

File : main_window.py
"""

import customtkinter as ctk

from ui.sidebar import Sidebar

from ui.pages.dashboard import Dashboard
from ui.pages.downloader import DownloaderPage
from ui.pages.uploader import UploaderPage
from ui.pages.scheduler import SchedulerPage
from ui.pages.metadata import MetadataPage
from ui.pages.analytics import AnalyticsPage
from ui.pages.settings import SettingsPage


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        # -------------------------
        # Window
        # -------------------------

        self.title("🐘 Elephant Content Studio")

        self.geometry("1400x850")

        self.minsize(1200, 700)

        # -------------------------
        # Grid Layout
        # -------------------------

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # -------------------------
        # Sidebar
        # -------------------------

        self.sidebar = Sidebar(

            self,

            self.show_page

        )

        self.sidebar.grid(

            row=0,

            column=0,

            sticky="ns"

        )

        # -------------------------
        # Main Container
        # -------------------------

        self.container = ctk.CTkFrame(

            self,

            corner_radius=0

        )

        self.container.grid(

            row=0,

            column=1,

            sticky="nsew"

        )

        self.container.grid_rowconfigure(

            0,

            weight=1

        )

        self.container.grid_columnconfigure(

            0,

            weight=1

        )

        # -------------------------
        # Pages
        # -------------------------

        self.pages = {

            "dashboard": Dashboard,

            "downloader": DownloaderPage,

            "uploader": UploaderPage,

            "scheduler": SchedulerPage,

            "metadata": MetadataPage,

            "analytics": AnalyticsPage,

            "settings": SettingsPage

        }

        self.current_page = None

        # Default Page

        self.show_page("dashboard")

    # ===================================================

    def show_page(

        self,

        page_name

    ):

        if self.current_page is not None:

            self.current_page.destroy()

        page_class = self.pages.get(page_name)

        if page_class is None:

            return

        self.current_page = page_class(

            self.container

        )

        self.current_page.grid(

            row=0,

            column=0,

            sticky="nsew"

        )