import ttkbootstrap as ttk


class CustomEntry(ttk.Entry):
    """
    输入框，加入提示文字、滚动条。

    :param root: 主窗口
    """

    def __init__(self, root, placeholder="", side=ttk.LEFT):
        super().__init__(root, font=("", 10))
        self.root = root
        self._manage_placeholder(self, placeholder)

    def _manage_placeholder(self, text: ttk.Entry, placeholder: str) -> None:
        """管理文本框提示文字占位符"""
        if placeholder:
            text.insert(0, placeholder)
            text.bind("<FocusIn>", lambda event, t=text, p=placeholder: self._on_focus_in(t, p))
            text.bind("<FocusOut>", lambda event, t=text, p=placeholder: self._on_focus_out(t, p))

    @staticmethod
    def _on_focus_in(text: ttk.Entry, placeholder: str) -> None:
        """文本框获得焦点时，清除提示文字"""
        if text.get() == placeholder:
            text.delete(0, "end")

    @staticmethod
    def _on_focus_out(text: ttk.Entry, placeholder: str) -> None:
        """文本框失去焦点时，添加提示文字"""
        if not text.get():
            text.insert(0, placeholder)
            # text.config(fg=COLOR_MAP['placeholder'])
