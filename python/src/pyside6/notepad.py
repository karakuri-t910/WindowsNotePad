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
        
        # 各ウィジェットの生成と機能追加
        self.BuildUi()
        
    def BuildUi(self):
        """各ウィジェットの生成と機能追加を行います。
        """
        # メニューバーの作成
        self.SetMenubar()
        
    def SetMenubar(self):
        """メニューバーを追加します。
        """
        self.menubar = QMenuBar(self)
        
        fileMenu = self.menubar.addMenu("ファイル(&F)")
        
        # ファイル(F) → 新規(N)
        fileNew = QAction("新規(&N)", self)
        fileNew.setShortcut("Ctrl+N")
        fileNew.triggered.connect(None)
        fileMenu.addAction(fileNew)
        
        # ファイル(F) → 新しいウィンドウ(W)
        fileNewWindow = QAction("新しいウィンドウ(&W)", self)
        fileNewWindow.setShortcut("Ctrl+Shift+N")
        fileNewWindow.triggered.connect(None)
        fileMenu.addAction(fileNewWindow)
        
        # ファイル(F) → 開く...(O)
        fileOpen = QAction("開く...(&O)", self)
        fileOpen.setShortcut("Ctrl+O")
        fileOpen.triggered.connect(None)
        fileMenu.addAction(fileOpen)
        
        # ファイル(F) → 上書き保存(S)
        fileSave = QAction("上書き保存(&S)", self)
        fileSave.setShortcut("Ctrl+S")
        fileSave.triggered.connect(None)
        fileMenu.addAction(fileSave)
        
        # ファイル(F) → 名前を付けて保存...(A)
        fileSaveAs = QAction("名前を付けて保存...(&A)", self)
        fileSaveAs.setShortcut("Ctrl+Shift+S")
        fileSaveAs.triggered.connect(None)
        fileMenu.addAction(fileSaveAs)
        
        fileMenu.addSeparator()
        
        # ファイル(F) → 終了(X)
        fileExit = QAction("終了(&X)", self)
        fileExit.setShortcut("Ctrl+Q")
        fileExit.triggered.connect(None)
        fileMenu.addAction(fileExit)
        
        # 編集(E)
        editMenu = self.menubar.addMenu("編集(&E)")
        
        # 編集(E) → 
        editUndo = QAction("元に戻す(&U)", self)
        editUndo.setShortcut("Ctrl+Z")
        editUndo.triggered.connect(None)
        editMenu.addAction(editUndo)
        
        editMenu.addSeparator()
        
        # 編集(E) → 
        editCut = QAction("切り取り(&T)", self)
        editCut.setShortcut("Ctrl+X")
        editCut.triggered.connect(None)
        editMenu.addAction(editCut)
        
        # 編集(E) → 
        editCopy = QAction("コピー(&C)", self)
        editCopy.setShortcut("Ctrl+C")
        editCopy.triggered.connect(None)
        editMenu.addAction(editCopy)
        
        # 編集(E) → 
        editPaste = QAction("貼り付け(&P)", self)
        editPaste.setShortcut("Ctrl+V")
        editPaste.triggered.connect(None)
        editMenu.addAction(editPaste)
        
        # 編集(E) → 
        editDelete = QAction("削除(&L)", self)
        editDelete.setShortcut("Del")
        editDelete.triggered.connect(None)
        editMenu.addAction(editDelete)
        
        editMenu.addSeparator()
        
        # 編集(E) → 
        editSearchBing = QAction("Bing で検索(&S)...", self)
        editSearchBing.setShortcut("Ctrl+E")
        editSearchBing.triggered.connect(None)
        editMenu.addAction(editSearchBing)
        
        # 編集(E) → 
        editSearch = QAction("検索(&F)...", self)
        editSearch.setShortcut("Ctrl+F")
        editSearch.triggered.connect(None)
        editMenu.addAction(editSearch)
        
        # 編集(E) → 
        editSearchForward = QAction("次を検索(&N)", self)
        editSearchForward.setShortcut("F3")
        editSearchForward.triggered.connect(None)
        editMenu.addAction(editSearchForward)
        
        # 編集(E) → 
        editSearchBackward = QAction("前を検索(&V)", self)
        editSearchBackward.setShortcut("Shift+F3")
        editSearchBackward.triggered.connect(None)
        editMenu.addAction(editSearchBackward)
        
        # 編集(E) → 
        editReplace = QAction("置換(&R)...", self)
        editReplace.setShortcut("Ctrl+R")
        editReplace.triggered.connect(None)
        editMenu.addAction(editReplace)
        
        # 編集(E) → 
        editJump = QAction("移動(&G)...", self)
        editJump.setShortcut("Ctrl+J")
        editJump.triggered.connect(None)
        editMenu.addAction(editJump)
        
        editMenu.addSeparator()
        
        # 編集(E) → 
        editSelectAll = QAction("すべて選択(&A)", self)
        editSelectAll.setShortcut("Ctrl+A")
        editSelectAll.triggered.connect(None)
        editMenu.addAction(editSelectAll)
        
        # 編集(E) → 
        editDateAndTime = QAction("日付と時刻(&D)", self)
        editDateAndTime.setShortcut("F5")
        editDateAndTime.triggered.connect(None)
        editMenu.addAction(editDateAndTime)
        
        # 書式(O)
        formatMenu = self.menubar.addMenu("書式(&O)")
        
        # 書式(O) → 
        formatFoldback = QAction("右端で折り返す(&W)", self)
        formatFoldback.setShortcut("")
        formatFoldback.triggered.connect(None)
        formatMenu.addAction(formatFoldback)
        
        # 書式(O) → 
        formatFont = QAction("フォント(F)...", self)
        formatFont.setShortcut("")
        formatFont.triggered.connect(None)
        formatMenu.addAction(formatFont)
        
        # 表示(V)
        viewMenu = self.menubar.addMenu("表示(&V)")
        
        # 表示(V) → 
        viewZoom = QAction("ズーム(&Z)", self)
        viewZoom.setShortcut("")
        viewZoom.triggered.connect(None)
        viewMenu.addAction(viewZoom)
        
        # 表示(V) → 
        viewStatusbar = QAction("ステータスバー(&S)", self)
        viewStatusbar.setShortcut("")
        viewStatusbar.triggered.connect(None)
        viewMenu.addAction(viewStatusbar)
        
        # ヘルプ(H)
        helpMenu = self.menubar.addMenu("ヘルプ(&H)")
        
        # ヘルプ(H) → 
        helpShow = QAction("ヘルプの表示(&H)", self)
        helpShow.setShortcut("")
        helpShow.triggered.connect(None)
        helpMenu.addAction(helpShow)
        
        # ヘルプ(H) → 
        helpSendFeedback = QAction("フィードバックの送信(&F)", self)
        helpSendFeedback.setShortcut("")
        helpSendFeedback.triggered.connect(None)
        helpMenu.addAction(helpSendFeedback)
        
        helpMenu.addSeparator()
        
        # ヘルプ(H) → 
        helpThisVersion = QAction("Pyside6でメモ帳のバージョン情報(&A)", self)
        helpThisVersion.setShortcut("")
        helpThisVersion.triggered.connect(None)
        helpMenu.addAction(helpThisVersion)


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)
    notepad = NotePad()
    notepad.show()
    sys.exit(app.exec())