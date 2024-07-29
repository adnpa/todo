import io

from src.todo import Todo
from src.ui.main_window import MainWindow

import base64

from PIL import Image
from ttkbootstrap.icons import Icon


def main() -> None:
    op = Todo()
    root = MainWindow(op)
    root.run()


if __name__ == '__main__':
    main()
