import ttkbootstrap as ttk
from src.constant import *


class CusText(ttk.Text):
    """
    文本编辑框，加入提示文字、滚动条。

    :param root: 主窗口
    """

    def __init__(self, root, placeholder=""):
        super().__init__(root, undo=True, font=("", 10), wrap='none', height=1)
        self.root = root
        self._manage_placeholder(self, placeholder)
        self.bind("<Return>", self.enter_callback)
        self.bind("<BackSpace>", self.backspace_callback)

    def enter_callback(self, *kw):
        self.config(height=len(self.get("1.0", ttk.END).split("\n")))

    def backspace_callback(self, *kw):
        # 获取当前光标位置的索引
        cursor_pos = self.index("insert")
        # 获取当前所在行号
        current_line = int(cursor_pos.split(".")[0])
        # 获取当前行的第一个字符位置
        line_start = f"{current_line}.0"
        if cursor_pos == line_start:  # 只有在行首按回车才调整
            self.config(height=len(self.get("1.0", ttk.END).split("\n")) - 2)

    def _config_scrollbar(self, text: ttk.Text) -> None:
        """建立配置文本框滚动条"""
        scrollbar = ttk.Scrollbar(self.root)
        scrollbar.pack(side=ttk.LEFT)
        scrollbar.config(command=text.yview)
        text.config(yscrollcommand=scrollbar.set)

    def _manage_placeholder(self, text: ttk.Text, placeholder: str) -> None:
        """管理文本框提示文字占位符"""
        if placeholder:
            text.insert("1.0", placeholder)
            text.config(fg=COLOR_MAP['placeholder'])
            text.bind("<FocusIn>", lambda event, t=text, p=placeholder: self._on_focus_in(t, p))
            text.bind("<FocusOut>", lambda event, t=text, p=placeholder: self._on_focus_out(t, p))

    @staticmethod
    def _on_focus_in(text: ttk.Text, placeholder: str) -> None:
        """文本框获得焦点时，清除提示文字"""
        if text.get("1.0", "end-1c") == placeholder:
            text.delete("1.0", "end")
            text.config(fg=COLOR_MAP['text'])

    @staticmethod
    def _on_focus_out(text: ttk.Text, placeholder: str) -> None:
        """文本框失去焦点时，添加提示文字"""
        if not text.get("1.0", "end-1c"):
            text.insert("1.0", placeholder)
            text.config(fg=COLOR_MAP['placeholder'])
