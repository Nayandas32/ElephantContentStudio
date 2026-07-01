import customtkinter as ctk

from ui.components.theme import FONT
from services.download_service import DownloadService
from core.current_project import get_project


class DownloaderPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.service = DownloadService()

        self.build()

    def build(self):

        ctk.CTkLabel(
            self,
            text="Downloader",
            font=(FONT, 28, "bold")
        ).pack(pady=25)

        self.url = ctk.CTkEntry(
            self,
            width=700,
            placeholder_text="Paste YouTube URL"
        )

        self.url.pack(pady=15)

        ctk.CTkButton(
            self,
            text="Download",
            command=self.start_download
        ).pack()

    # ======================================

    def start_download(self):

        project = get_project()

        print("CURRENT PROJECT =", project)

        if project is None:

            print("PROJECT IS NONE")

            dialog = ctk.CTkInputDialog(
                text="Please open a project first.",
                title="No Project"
            )

            return

        print("PROJECT FOUND")

        self.service.set_project(project)

        self.service.download(
            self.url.get().strip()
        )