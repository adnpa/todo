import atexit
import base64
import os
import tempfile
import zlib

import ttkbootstrap as ttk
from ttkbootstrap import dialogs
from PIL import ImageTk

from src.task import Task
from src.ui.cus_entry import CustomEntry
from src.ui.cus_text import CusText
from src.constant import *
import PIL.Image
import PIL.ImageTk


class CustomDialog(ttk.Toplevel):
    """
    弹出任务输入对话框
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.result = ()
        self.parent = parent
        print("create diag")
        # 纯 UI 建立函数，最后加上阻塞流程，等待窗口被销毁或关闭
        self._setup_window()
        self._create_widgets()
        self.wait_window(self)

    def _setup_window(self) -> None:
        """窗口配置"""
        # self.style.theme_use(COLOR_THEME)
        # self.title(LABEL_MAP['settings_title'])
        # self.iconbitmap(self.parent.icon_path)
        self.resizable(width=False, height=False)
        self.place_window_center()
        # 在任务栏中不显示条目
        self.transient(self.parent)
        # 使窗口获得焦点，阻止与其他窗口交互
        self.grab_set()

    def _create_widgets(self) -> None:
        """创建控件元素"""
        master = ttk.Frame(self)
        master.pack(padx=10, pady=10, fill="both", expand=True)
        # 标题
        title = CustomEntry(master, "标题", ttk.TOP)
        title.pack(side=ttk.TOP, pady=5, fill='x', expand=True)
        # 描述
        description = CusText(master, "描述")
        description.pack(side=ttk.TOP)
        # 选择按钮
        bt_frame = ttk.Frame(master)
        bt_frame.pack(side=ttk.TOP, padx=10, pady=10, fill="both", expand=True)

        # 截止日期
        def on_label_click(event):
            dialog = dialogs.DatePickerDialog()
            deadline.config(compound='left')
            deadline.config(text=str(dialog.date_selected))

        self.img = PIL.Image.open('icon/calendar.png').resize((25, 25))
        self.photo = ImageTk.PhotoImage(self.img)
        deadline = ttk.Label(bt_frame, image=self.photo, text='截止日期')
        deadline.bind("<Button-1>", on_label_click)
        deadline.pack(side=ttk.LEFT, padx=5, pady=1, expand=False, fill='x')

        # 优先级
        priority = ttk.Combobox(bt_frame, state='readonly',
                                values=['优先级1', '优先级2', '优先级3', '优先级4'])
        priority.current(3)
        priority.pack(side=ttk.LEFT, padx=10, pady=10, fill="x", expand=True)
        # 标签
        tag = CustomEntry(bt_frame, "tag")
        tag.pack(side=ttk.LEFT, padx=5, pady=1, expand=True, fill='x')

        # 分割线
        sep = ttk.Separator(master)
        sep.pack(side=ttk.TOP, padx=10, pady=10, fill="x", expand=True)

        # 添加按钮
        def on_button_click():
            priority_map = {'优先级1': URGENT, '优先级2': HIGH, '优先级3': MEDIUM, '优先级4': LOW}
            task = Task(0, title.get(), description.get("1.0", ttk.END), priority_map[priority.get()], tag.get(), False)
            self.parent.op.create_task(task)
            self.parent.add_task(task)
            self.destroy()

        add_task_button = ttk.Button(master, text='添加任务', command=on_button_click)
        add_task_button.pack(side=ttk.TOP, anchor='e', padx=5, pady=1)

        #


def create_icon() -> str:
    """
    从 base64 编码中生成临时图标，在程序结束时自动删除。
    好处是打包时不用导入资源文件。

    :return: 返回图标文件路径
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.ico') as temp_file:
        temp_file.write(zlib.decompress(base64.b64decode(ICON_BASE64)))

    ico_path = temp_file.name
    # 显式声明程序退出时，删除临时图标文件，避免在个别系统平台自动删除失败
    atexit.register(os.remove, ico_path)
    return ico_path

    # def validate(self) -> bool:
    #     """验证输入提取码有效性"""
    #     expiry = self.var_expiry.get()
    #     password = self.var_password.get()
    #     # 用正则检查用户输入，为 False 时窗口继续停留
    #     if not re.match("^[a-zA-Z0-9]{4}$", password):
    #         Messagebox.show_warning(title=LABEL_MAP['validate_title'], message=LABEL_MAP['validate_msg'], master=self)
    #         return False
    #
    #     # 结果被 share 函数直接获取
    #     self.result = (expiry, password)
    #     self.destroy()
    #     return True
    #
    # def show_input_dialog():
    #     def get_input():
    #         global user_input
    #         user_input = entry.get()
    #         dialog.destroy()
    #
    #     dialog = tk.Toplevel(root)
    #     dialog.title("Input Dialog")
    #
    #     label = tk.Label(dialog, text="Please enter a value:")
    #     label.pack(padx=20, pady=10)
    #
    #     entry = tk.Entry(dialog)
    #     entry.pack(padx=20, pady=10)
    #
    #     button = tk.Button(dialog, text="OK", command=get_input)
    #     button.pack(padx=20, pady=10)
    #
    #     dialog.mainloop()
