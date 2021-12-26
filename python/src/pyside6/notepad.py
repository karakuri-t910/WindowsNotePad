# coding: shift-jis
import PySide6
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QApplication,
                               QWidget)
import os
import sys


class NotePad(QWidget):
    def __init__(self, width=800, height=500, title="�^�C�g���Ȃ�", parent=None):
        """���̃������A�v���̏��������s���܂��B
        
        ����:
        ----------
        widht: int
            �E�B���h�E�̉���
        height: int
            �E�B���h�E�̍���
        title: string
            �E�B���h�E�^�C�g��
        parent: object
            ���̃E�B���h�E�̑��ɕ\������E�B���h�E������ꍇ�ɂ̂݁A
            ���̃E�B���h�E�̃C���X�^���X�������Ɏw�肵�܂��B
        """
        super().__init__(parent)
        
        windowWidth = width
        windowHeight = height
        windowTitle = title + " - PySide6�Ń�����"
        
        # �E�B���h�E�ݒ�
        self.resize(windowWidth, windowHeight)
        self.setWindowTitle(windowTitle)


if __name__ == "__main__":
    # ���ϐ���PySide6��o�^
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)
    notepad = NotePad()
    notepad.show()
    sys.exit(app.exec())