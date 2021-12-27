# coding: shift-jis
import PySide6
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QApplication,
                               QDockWidget,
                               QMenuBar,
                               QTextEdit,
                               QVBoxLayout,
                               QWidget)
import os
import sys


class Menubar:
    def __init__(self, notepad, menubar):
        """���j���[�o�[�Ɗe���j���[���ڂ�ǉ����܂��B
        """
        
        # �t�@�C��(F)
        fileMenu = menubar.addMenu("�t�@�C��(&F)")
        self.SetFileMenu(notepad, fileMenu)
        
        # �ҏW(E)
        editMenu = menubar.addMenu("�ҏW(&E)")
        self.SetEditMenu(notepad, editMenu)
        
        # ����(O)
        formatMenu = menubar.addMenu("����(&O)")
        self.SetFormatMenu(notepad, formatMenu)
        
        # �\��(V)
        viewMenu = menubar.addMenu("�\��(&V)")
        self.SetViewMenu(notepad, viewMenu)
        
        # �w���v(H)
        helpMenu = menubar.addMenu("�w���v(&H)")
        self.SetHelpMenu(notepad, helpMenu)
        
    def SetFileMenu(self, notepad, fileMenu):
        """�t�@�C�����j���[���ڂ�ǉ����܂��B
        
        ����:
        ----------
        fileMenu object:
        �t�@�C�����j���[���ڂ̃I�u�W�F�N�g
        """
        # �t�@�C��(F) �� �V�K(N)
        fileNew = QAction("�V�K(&N)", notepad)
        fileNew.setShortcut("Ctrl+N")
        fileNew.triggered.connect(None)
        fileMenu.addAction(fileNew)
        
        # �t�@�C��(F) �� �V�����E�B���h�E(W)
        fileNewWindow = QAction("�V�����E�B���h�E(&W)", notepad)
        fileNewWindow.setShortcut("Ctrl+Shift+N")
        fileNewWindow.triggered.connect(None)
        fileMenu.addAction(fileNewWindow)
        
        # �t�@�C��(F) �� �J��...(O)
        fileOpen = QAction("�J��(&O)...", notepad)
        fileOpen.setShortcut("Ctrl+O")
        fileOpen.triggered.connect(None)
        fileMenu.addAction(fileOpen)
        
        # �t�@�C��(F) �� �㏑���ۑ�(S)
        fileSave = QAction("�㏑���ۑ�(&S)", notepad)
        fileSave.setShortcut("Ctrl+S")
        fileSave.triggered.connect(None)
        fileMenu.addAction(fileSave)
        
        # �t�@�C��(F) �� ���O��t���ĕۑ�...(A)
        fileSaveAs = QAction("���O��t���ĕۑ�(&A)...", notepad)
        fileSaveAs.setShortcut("Ctrl+Shift+S")
        fileSaveAs.triggered.connect(None)
        fileMenu.addAction(fileSaveAs)
        
        fileMenu.addSeparator()
        
        # �t�@�C��(F) �� �I��(X)
        fileExit = QAction("�I��(&X)", notepad)
        fileExit.setShortcut("Ctrl+Q")
        fileExit.triggered.connect(None)
        fileMenu.addAction(fileExit)
        
    def SetEditMenu(self, notepad, editMenu):
        """�ҏW���j���[���ڂ�ǉ����܂��B
        
        ����:
        ----------
        editMenu object:
        �ҏW���j���[���ڂ̃I�u�W�F�N�g
        """
        # �ҏW(E) �� ���ɖ߂�(U)
        editUndo = QAction("���ɖ߂�(&U)", notepad)
        editUndo.setShortcut("Ctrl+Z")
        editUndo.triggered.connect(None)
        editMenu.addAction(editUndo)
        
        editMenu.addSeparator()
        
        # �ҏW(E) �� �؂���(T)
        editCut = QAction("�؂���(&T)", notepad)
        editCut.setShortcut("Ctrl+X")
        editCut.triggered.connect(None)
        editMenu.addAction(editCut)
        
        # �ҏW(E) �� �R�s�[(C)
        editCopy = QAction("�R�s�[(&C)", notepad)
        editCopy.setShortcut("Ctrl+C")
        editCopy.triggered.connect(None)
        editMenu.addAction(editCopy)
        
        # �ҏW(E) �� �\��t��(P)
        editPaste = QAction("�\��t��(&P)", notepad)
        editPaste.setShortcut("Ctrl+V")
        editPaste.triggered.connect(None)
        editMenu.addAction(editPaste)
        
        # �ҏW(E) �� �폜(L)
        editDelete = QAction("�폜(&L)", notepad)
        editDelete.setShortcut("Del")
        editDelete.triggered.connect(None)
        editMenu.addAction(editDelete)
        
        editMenu.addSeparator()
        
        # �ҏW(E) �� Bing �Ō���(S)...
        editSearchBing = QAction("Bing �Ō���(&S)...", notepad)
        editSearchBing.setShortcut("Ctrl+E")
        editSearchBing.triggered.connect(None)
        editMenu.addAction(editSearchBing)
        
        # �ҏW(E) �� ����(F)...
        editSearch = QAction("����(&F)...", notepad)
        editSearch.setShortcut("Ctrl+F")
        editSearch.triggered.connect(None)
        editMenu.addAction(editSearch)
        
        # �ҏW(E) �� ��������(N)
        editSearchForward = QAction("��������(&N)", notepad)
        editSearchForward.setShortcut("F3")
        editSearchForward.triggered.connect(None)
        editMenu.addAction(editSearchForward)
        
        # �ҏW(E) �� �O������(V)
        editSearchBackward = QAction("�O������(&V)", notepad)
        editSearchBackward.setShortcut("Shift+F3")
        editSearchBackward.triggered.connect(None)
        editMenu.addAction(editSearchBackward)
        
        # �ҏW(E) �� �u��(R)...
        editReplace = QAction("�u��(&R)...", notepad)
        editReplace.setShortcut("Ctrl+R")
        editReplace.triggered.connect(None)
        editMenu.addAction(editReplace)
        
        # �ҏW(E) �� �ړ�(G)...
        editJump = QAction("�ړ�(&G)...", notepad)
        editJump.setShortcut("Ctrl+J")
        editJump.triggered.connect(None)
        editMenu.addAction(editJump)
        
        editMenu.addSeparator()
        
        # �ҏW(E) �� ���ׂđI��(A)
        editSelectAll = QAction("���ׂđI��(&A)", notepad)
        editSelectAll.setShortcut("Ctrl+A")
        editSelectAll.triggered.connect(None)
        editMenu.addAction(editSelectAll)
        
        # �ҏW(E) �� ���t�Ǝ���(D)
        editDateAndTime = QAction("���t�Ǝ���(&D)", notepad)
        editDateAndTime.setShortcut("F5")
        editDateAndTime.triggered.connect(None)
        editMenu.addAction(editDateAndTime)
        
    def SetFormatMenu(self, notepad, formatMenu):
        """�������j���[���ڂ�ǉ����܂��B
        
        ����:
        ----------
        formatMenu object:
        �������j���[���ڂ̃I�u�W�F�N�g
        """
        # ����(O) �� �E�[�Ő܂�Ԃ�(W)
        formatFoldback = QAction("�E�[�Ő܂�Ԃ�(&W)", notepad)
        formatFoldback.setShortcut("")
        formatFoldback.triggered.connect(None)
        formatMenu.addAction(formatFoldback)
        
        # ����(O) �� �t�H���g(F)...
        formatFont = QAction("�t�H���g(&F)...", notepad)
        formatFont.setShortcut("")
        formatFont.triggered.connect(None)
        formatMenu.addAction(formatFont)
        
    def SetViewMenu(self, notepad, viewMenu):
        """�\�����j���[���ڂ�ǉ����܂��B
        
        ����:
        ----------
        viewMenu object:
        �\�����j���[���ڂ̃I�u�W�F�N�g
        """
        # �\��(V) �� �Y�[��(Z)
        viewZoom = QAction("�Y�[��(&Z)", notepad)
        viewZoom.setShortcut("")
        viewZoom.triggered.connect(None)
        viewMenu.addAction(viewZoom)
        
        # �\��(V) �� �X�e�[�^�X�o�[(S)
        viewStatusbar = QAction("�X�e�[�^�X�o�[(&S)", notepad)
        viewStatusbar.setShortcut("")
        viewStatusbar.triggered.connect(None)
        viewMenu.addAction(viewStatusbar)
        
    def SetHelpMenu(self, notepad, helpMenu):
        """�w���v���j���[���ڂ�ǉ����܂��B
        
        ����:
        ----------
        helpMenu object:
        �w���v���j���[���ڂ̃I�u�W�F�N�g
        """
        # �w���v(H) �� �w���v�̕\��(H)
        helpShow = QAction("�w���v�̕\��(&H)", notepad)
        helpShow.setShortcut("")
        helpShow.triggered.connect(None)
        helpMenu.addAction(helpShow)
        
        # �w���v(H) �� �t�B�[�h�o�b�N�̑��M(F)
        helpSendFeedback = QAction("�t�B�[�h�o�b�N�̑��M(&F)", notepad)
        helpSendFeedback.setShortcut("")
        helpSendFeedback.triggered.connect(None)
        helpMenu.addAction(helpSendFeedback)
        
        helpMenu.addSeparator()
        
        # �w���v(H) �� Pyside6�Ń������̃o�[�W�������(A)
        helpThisVersion = QAction("Pyside6�Ń������̃o�[�W�������(&A)", notepad)
        helpThisVersion.setShortcut("")
        helpThisVersion.triggered.connect(None)
        helpMenu.addAction(helpThisVersion)


class Textbox:
    def __init__(self, notepad, textbox):
        pass


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
        # �p�����N���X(QWidget)�̏�����
        super().__init__(parent)
        
        self.windowWidth = width
        self.windowHeight = height
        self.windowTitle = title + " - PySide6�Ń�����"
        
        # �E�B���h�E�ݒ�
        self.resize(self.windowWidth, self.windowHeight)
        self.setWindowTitle(self.windowTitle)
        
        # �e�E�B�W�F�b�g�̐����Ƌ@�\�ǉ�
        self.BuildUi()
        
    def BuildUi(self):
        """�e�E�B�W�F�b�g�̐����Ƌ@�\�ǉ����s���܂��B
        """
        vBox = QVBoxLayout()
        
        # ���j���[�o�[�̍쐬
        self.menubar = QMenuBar(self)
        Menubar(self, self.menubar)
        
        # �e�L�X�g�{�b�N�X
        self.textbox = QTextEdit(self)
        Textbox(self, self.textbox)
        
        vBox.addWidget(self.menubar)
        vBox.addWidget(self.textbox)
        
        self.setLayout(vBox)


if __name__ == "__main__":
    # ���ϐ���PySide6��o�^
    dirname = os.path.dirname(PySide6.__file__)
    pluginPath = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = pluginPath
    
    app = QApplication(sys.argv)
    notepad = NotePad()
    notepad.show()
    sys.exit(app.exec())