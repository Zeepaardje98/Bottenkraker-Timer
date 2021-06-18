class Theme:
    def __init__(self, root, parent, settings):
        self.root = root
        self.parent = parent
        self.settings = settings

    def valid_theme(string):
        if string in self.settings.get_settings(['themes']).keys()
            return True
        return False

    def change_theme(self, widget, parent):
        theme = self.settings.get_settings(['selected_theme'])
        if theme == 'default':
            return
        if parent:
            widget.config(background = self.settings.get_settings(['themes', theme, 'background']))

        if len(widget.children.values()) < 0:
            return
        for child in widget.children.values():
            self.change_theme(child, False)
            child.config(background = self.settings.get_settings(['themes', theme, 'background']))

    def submit_theme():
        if valid_theme(string):
            return
