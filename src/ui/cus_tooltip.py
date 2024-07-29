
class ToolTip:
    """
    为组件增加悬浮提示气泡。

    :param widget: 要增加悬浮提示的组件
    :param text: 提示信息内容
    """

    def __init__(self, widget, text: str = ''):
        self.widget = widget
        self.text = text
        self.tips = None
        self.id = None
        # 绑定光标移入、移出和点击事件
        self._binding()

    def _binding(self) -> None:
        """配置鼠标绑定事件"""
        self.widget.bind("<Enter>", lambda _: self._after(True))
        self.widget.bind("<Leave>", lambda _: self._after(False))
        self.widget.bind("<ButtonPress>", lambda _: self._after(False))

    def _after(self, enter: bool) -> None:
        """活用 enter 来判断是否要展示提示气泡"""
        if self.id:
            self.widget.after_cancel(self.id)
            self.id = None

        if enter:
            self.id = self.widget.after(TOOLTIP_DELAY, self._show)
        else:
            self._hide()

    def _show(self) -> None:
        """显示气泡提示"""
        x = self.widget.winfo_rootx() + TOOLTIP_PADDING
        y = self.widget.winfo_rooty() - TOOLTIP_PADDING
        # 创建一个悬浮窗口
        self.tips = tw = ttk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        ttk.Label(tw, text=self.text, background=COLOR_MAP['tooltip'], relief='solid', borderwidth=1).pack(ipadx=1)

    def _hide(self) -> None:
        """隐藏气泡提示"""
        if self.tips:
            self.tips.destroy()
            self.tips = None
