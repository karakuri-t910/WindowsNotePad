# coding: shift-jis
import PySide6
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QApplication,
                               QGridLayout,
                               QMenuBar,
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
        
        # �e�E�B�W�F�b�g�̐����Ƌ@�\�ǉ�
        self.BuildUi()
        
    def BuildUi(self):
        """�e�E�B�W�F�b�g�̐����Ƌ@�\�ǉ����s���܂��B
        """
        # ���j���[�o�[�̍쐬
        self.SetMenubar()
        
    def SetMenubar(self):
        """���j���[�o�[��ǉ����܂��B
        """
        self.menubar = QMenuBar(self)
        
        fileMenu = self.menubar.addMenu("�t�@�C��(&F)")
        
        # �t�@�C��(F) �� �V�K(N)
        fileNew = QAction("�V�K(&N)", self)
        fileNew.setShortcut("Ctrl+N")
        fileNew.triggered.connect(None)
        fileMenu.addAction(fileNew)
        
        # �t�@�C��(F) �� �V�����E�B���h�E(W)
        fileNewWindow = QAction("�V�����E�B���h�E(&W)", self)
        fileNewWindow.setShortcut("Ctrl+Shift+N")
        fileNewWindow.triggered.connect(None)
        fileMenu.addAction(fileNewWindow)
        
        # �t�@�C��(F) �� �J��...(O)
        fileOpen = QAction("�J��...(&O)", self)
        fileOpen.setShortcut("Ctrl+O")
        fileOpen.triggered.connect(None)
        fileMenu.addAction(fileOpen)
        
        # �t�@�C��(F) �� �㏑���ۑ�(S)
        fileSave = QAction("�㏑���ۑ�(&S)", self)
        fileSave.setShortcut("Ctrl+S")
        fileSave.triggered.connect(None)
        fileMenu.addAction(fileSave)
        
        # �t�@�C��(F) �� ���O��t���ĕۑ�...(A)
        fileSaveAs = QAction("���O��t���ĕۑ�...(&A)", self)
        fileSaveAs.setShortcut("Ctrl+Shift+S")
        fileSaveAs.triggered.connect(None)
        fileMenu.addAction(fileSaveAs)
        
        fileMenu.addSeparator()
        
        # �t�@�C��(F) �� �I��(X)
        fileExit = QAction("�I��(&X)", self)
        fileExit.setShortcut("Ctrl+Q")
        fileExit.triggered.connect(None)
        fileMenu.addAction(fileExit)
        
        # �ҏW(E)
        editMenu = self.menubar.addMenu("�ҏW(&E)")
        
        # �ҏW(E) �� 
        editUndo = QAction("���ɖ߂�(&U)", self)
        editUndo.setShortcut("Ctrl+Z")
        editUndo.triggered.connect(None)
        editMenu.addAction(editUndo)
        
        editMenu.addSeparator()
        
        # �ҏW(E) �� 
        editCut = QAction("�؂���(&T)", self)
        editCut.setShortcut("Ctrl+X")
        editCut.triggered.connect(None)
        editMenu.addAction(editCut)
        
        # �ҏW(E) �� 
        editCopy = QAction("�R�s�[(&C)", self)
        editCopy.setShortcut("Ctrl+C")
        editCopy.triggered.connect(None)
        editMenu.addAction(editCopy)
        
        # �ҏW(E) �� 
        editPaste = QAction("�\��t��(&P)", self)
        editPaste.setShortcut("Ctrl+V")
        editPaste.triggered.connect(None)
        editMenu.addAction(editPaste)
        
        # �ҏW(E) �� 
        editDelete = QAction("�폜(&L)", self)
        editDelete.setShortcut("Del")
        editDelete.triggered.connect(None)
        editMenu.addAction(editDelete)
        
        editMenu.addSeparator()
        
        # �ҏW(E) �� 
        editSearchBing = QAction("Bing �Ō���(&S)...", self)
        editSearchBing.setShortcut("Ctrl+E")
        editSearchBing.triggered.connect(None)
        editMenu.addAction(editSearchBing)
        
        # �ҏW(E) �� 
        editSearch = QAction("����(&F)...", self)
        editSearch.setShortcut("Ctrl+F")
        editSearch.triggered.connect(None)
        editMenu.addAction(editSearch)
        
        # �ҏW(E) �� 
        editSearchForward = QAction("��������(&N)", self)
        editSearchForward.setShortcut("F3")
        editSearchForward.triggered.connect(None)
        editMenu.addAction(editSearchForward)
        
        # �ҏW(E) �� 
        editSearchBackward = QAction("�O������(&V)", self)
        editSearchBackward.setShortcut("Shift+F3")
        editSearchBackward.triggered.connect(None)
        editMenu.addAction(editSearchBackward)
        
        # �ҏW(E) �� 
        editReplace = QAction("�u��(&R)...", self)
        editReplace.setShortcut("Ctrl+R")
        editReplace.triggered.connect(None)
        editMenu.addAction(editReplace)
        
        # �ҏW(E) �� 
        editJump = QAction("�ړ�(&G)...", self)
        editJump.setShortcut("Ctrl+J")
        editJump.triggered.connect(None)
        editMenu.addAction(editJump)
        
        editMenu.addSeparator()
        
        # �ҏW(E) �� 
        editSelectAll = QAction("���ׂđI��(&A)", self)
        editSelectAll.setShortcut("Ctrl+A")
        editSelectAll.triggered.connect(None)
        editMenu.addAction(editSelectAll)
        
        # �ҏW(E) �� 
        editDateAndTime = QAction("���t�Ǝ���(&D)", self)
        editDateAndTime.setShortcut("F5")
        editDateAndTime.triggered.connect(None)
        editMenu.addAction(editDateAndTime)
        
        # ����(O)
        formatMenu = self.menubar.addMenu("����(&O)")
        
        # ����(O) �� 
        formatFoldback = QAction("�E�[�Ő܂�Ԃ�(&W)", self)
        formatFoldback.setShortcut("")
        formatFoldback.triggered.connect(None)
        formatMenu.addAction(formatFoldback)
        
        # ����(O) �� 
        formatFont = QAction("�t�H���g(F)...", self)
        formatFont.setShortcut("")
        formatFont.triggered.connect(None)
        formatMenu.addAction(formatFont)
        
        # �\��(V)
        viewMenu = self.menubar.addMenu("�\��(&V)")
        
        # �\��(V) �� 
        viewZoom = QAction("�Y�[��(&Z)", self)
        viewZoom.setShortcut("")
        viewZoom.triggered.connect(None)
        viewMenu.addAction(viewZoom)
        
        # �\��(V) �� 
        viewStatusbar = QAction("�X�e�[�^�X�o�[(&S)", self)
        viewStatusbar.setShortcut("")
        viewStatusbar.triggered.connect(None)
        viewMenu.addAction(viewStatusbar)
        
        # �w���v(H)
        helpMenu = self.menubar.addMenu("�w���v(&H)")
        
        # �w���v(H) �� 
        helpShow = QAction("�w���v�̕\��(&H)", self)
        helpShow.setShortcut("")
        helpShow.triggered.connect(None)
        helpMenu.addAction(helpShow)
        
        # �w���v(H) �� 
        helpSendFeedback = QAction("�t�B�[�h�o�b�N�̑��M(&F)", self)
        helpSendFeedback.setShortcut("")
        helpSendFeedback.triggered.connect(None)
        helpMenu.addAction(helpSendFeedback)
        
        helpMenu.addSeparator()
        
        # �w���v(H) �� 
        helpThisVersion = QAction("Pyside6�Ń������̃o�[�W�������(&A)", self)
        helpThisVersion.setShortcut("")
        helpThisVersion.triggered.connect(None)
        helpMenu.addAction(helpThisVersion)


if __name__ == "__main__":
    # ���ϐ���PySide6��o�^
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)
    notepad = NotePad()
    notepad.show()
    sys.exit(app.exec())