def __init__(self, parent):

    super().__init__(parent)

    self.db = DatabaseManager()

    self.build()

    self.load_projects()