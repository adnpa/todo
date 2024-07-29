class RightClickMenu(ttk.Menu):
    """
    为组件增加右键菜单。

    :param widget: 只接收输入框（entry）和文本框（text）组件
    """

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self._make_menu()

    def _make_menu(self):
        """配置输入框右键菜单"""
        self.add_command(label=LABEL_MAP['undo'], command=lambda: self.widget.event_generate('<<Undo>>'))
        self.add_command(label=LABEL_MAP['redo'], command=lambda: self.widget.event_generate('<<Redo>>'))
        self.add_separator()
        self.add_command(label=LABEL_MAP['cut'], command=lambda: self.widget.event_generate('<<Cut>>'))
        self.add_command(label=LABEL_MAP['copy'], command=lambda: self.widget.event_generate('<<Copy>>'))
        self.add_command(label=LABEL_MAP['paste'], command=lambda: self.widget.event_generate('<<Paste>>'))
        self.add_separator()
        self.add_command(label=LABEL_MAP['select_all'], command=lambda: self.widget.event_generate('<<SelectAll>>'))
        self.add_command(label=LABEL_MAP['clear'], command=lambda: self.widget.event_generate('<<Clear>>'))

    def show_menu(self, e) -> None:
        """显示右键菜单"""
        self.tk_popup(e.x_root, e.y_root)
