# coding: shift-jis
import PySide6
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QApplication,
                               QWidget)
import os
import sys


class NotePad(QWidget):
    def __init__(self, width=800, height=500, title="タイトルなし", parent=None):
        """このメモ帳アプリの初期化を行います。
        
        引数:
        ----------
        widht: int
            ウィンドウの横幅
        height: int
            ウィンドウの高さ
        title: string
            ウィンドウタイトル
        parent: object
            このウィンドウの他に表示するウィンドウがある場合にのみ、
            そのウィンドウのインスタンスを引数に指定します。
        """
        super().__init__(parent)
        
        windowWidth = width
        windowHeight = height
        windowTitle = title + " - PySide6でメモ帳"
        
        # ウィンドウ設定
        self.resize(windowWidth, windowHeight)
        self.setWindowTitle(windowTitle)


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)
    notepad = NotePad()
    notepad.show()
    sys.exit(app.exec())