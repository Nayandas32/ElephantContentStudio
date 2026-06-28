import customtkinter as ctk

from ui.main_window import MainWindow

from core.logger import Logger


logger = Logger.get_logger()


def main():

    logger.info("=====================================")
    logger.info("Elephant Content Studio Starting...")
    logger.info("=====================================")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = MainWindow()

    logger.info("UI Loaded Successfully.")

    app.mainloop()

    logger.info("Application Closed.")


if __name__ == "__main__":
    main()