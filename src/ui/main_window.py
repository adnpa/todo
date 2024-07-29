import base64

import ttkbootstrap as ttk
import ttkbootstrap.dialogs as dialogs
from ttkbootstrap.icons import Icon

from src.constant import ICON_BASE64
from src.ui.cus_dialog import CustomDialog
from PIL import Image, ImageTk


class MainWindow(ttk.Window):
    """
    程序主窗口，继承自 ttk.Window。

    :param op: 主逻辑功能类的实例
    """

    def __init__(self, op):
        """初始化 UI 元素"""
        super().__init__(size=(800, 600))
        self.op = op
        self._setup_window()
        self._create_widgets()
        self._load_tasks()

    def _setup_window(self):
        self.title("test_window")
        self.style.theme_use('litera')
        self.place_window_center()

    def _create_widgets(self) -> None:
        # 侧栏
        self.sidebar = ttk.Frame(self)
        self.sidebar.pack(side=ttk.LEFT, expand=False, fill='x')
        self._setup_sidebar()

        # 分割线
        self.separator = ttk.Separator(self, orient='vertical')
        self.separator.pack(side=ttk.LEFT, fill='y')
        # 任务列表
        self.task_list = ttk.Frame(self)
        self.task_list.pack(side=ttk.LEFT, padx=5, pady=100, expand=True, fill='y')

    def _create_treeview(self):
        tree = ttk.Treeview()
        self.tree = tree

    def add_task(self, task):
        # 创建包含按钮和文本的框架
        task_frame = ttk.Frame(self.task_list)
        task_frame.pack(anchor='n', expand=True, fill='x')
        ttk.IntVar(task_frame).set(task.id)
        # 描述
        description = ttk.Label(task_frame, text=task.description)
        description.pack(side=ttk.BOTTOM, padx=30, anchor='w', expand=True, fill='both')
        # 是否完成
        check_button = ttk.Checkbutton(task_frame, name="completed", state="normal")
        check_button.pack(side=ttk.LEFT, padx=5, pady=1, expand=True, fill='both')
        # 标题
        title = ttk.Label(task_frame, name="title", text=task.title)
        title.pack(side=ttk.LEFT, padx=5, pady=1, expand=True, fill='both')
        # 优先级
        priority = ttk.Label(task_frame, name="priority", text=task.priority)
        priority.pack(side=ttk.LEFT, padx=5, pady=1, expand=True, fill='both')
        # 截止日期
        deadline = ttk.Label(task_frame, name="deadline", text=task.deadline)
        deadline.pack(side=ttk.LEFT, padx=5, pady=1, expand=True, fill='both')
        # 标签
        tag = ttk.Label(task_frame, name="tag", text=task.tag)
        tag.pack(side=ttk.LEFT, padx=5, pady=1, expand=True, fill='both')

        def check_callback():
            self.op.negate_task(task.id)
            taskdb = self.op.get_task(task.id)
            title.config(text=taskdb.title)
            priority.config(text=taskdb.priority)
            deadline.config(text=taskdb.deadline)
            tag.config(text=taskdb.tag)
            description.config(text=taskdb.description)

        check_button.config(variable=task.completed, command=check_callback)

    def _setup_sidebar(self):
        # 添加任务
        self.add_task_b = ttk.Button(self.sidebar, text="添加任务", width=30, command=self._add_task_button_click)
        self.add_task_b.pack(anchor='n', side=ttk.TOP, expand=True, fill='both')

        # img = ttk.PhotoImage(data=Icon.error)
        # img_label = ttk.Label(self.sidebar, image=img)
        # img_label.pack(side=ttk.LEFT, padx=5, pady=1, expand=True, fill='both')

    def _add_task_button_click(self):
        self.diag()

    def diag(self):
        CustomDialog(self)
        # try:
        # 创建对话框实例，如果对话框没有返回输入值，则忽略
        # self.dialog_result = CustomDialog(self)
        # if self.dialog_result.result:
        # self.prepare_run()
        # self.handle_input(task_count_check=False)
        # self.handle_bdstoken()
        # self.handle_list_dir()
        # self.setup_share()
        # self.handle_process_share()
        # except Exception as e:
        #     self.insert_logs(f'程序出现未预料错误，信息如下：\n{e}\n{traceback.format_exc()}')
        # finally:
        #     self.network.s.close()
        #     self.change_status('stopped')

    def _load_tasks(self):
        tasks = self.op.get_tasks()
        for task in tasks:
            self.add_task(task)

    def run(self) -> None:
        self.mainloop()


class RightClickMenu(ttk.Menu):
    """
    为组件增加右键菜单。

    :param widget: 只接收输入框（entry）和文本框（text）组件
    """

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        # self._make_menu()

    # def _make_menu(self):
    #     """配置输入框右键菜单"""
    #     self.add_command(label=LABEL_MAP['undo'], command=lambda: self.widget.event_generate('<<Undo>>'))
    #     self.add_command(label=LABEL_MAP['redo'], command=lambda: self.widget.event_generate('<<Redo>>'))
    #     self.add_separator()
    #     self.add_command(label=LABEL_MAP['cut'], command=lambda: self.widget.event_generate('<<Cut>>'))
    #     self.add_command(label=LABEL_MAP['copy'], command=lambda: self.widget.event_generate('<<Copy>>'))
    #     self.add_command(label=LABEL_MAP['paste'], command=lambda: self.widget.event_generate('<<Paste>>'))
    #     self.add_separator()
    #     self.add_command(label=LABEL_MAP['select_all'], command=lambda: self.widget.event_generate('<<SelectAll>>'))
    #     self.add_command(label=LABEL_MAP['clear'], command=lambda: self.widget.event_generate('<<Clear>>'))

    def show_menu(self, e) -> None:
        """显示右键菜单"""
        self.tk_popup(e.x_root, e.y_root)
