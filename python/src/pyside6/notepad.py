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
        """メニューバーと各メニュー項目を追加します。
        """
        
        # ファイル(F)
        fileMenu = menubar.addMenu("ファイル(&F)")
        self.SetFileMenu(notepad, fileMenu)
        
        # 編集(E)
        editMenu = menubar.addMenu("編集(&E)")
        self.SetEditMenu(notepad, editMenu)
        
        # 書式(O)
        formatMenu = menubar.addMenu("書式(&O)")
        self.SetFormatMenu(notepad, formatMenu)
        
        # 表示(V)
        viewMenu = menubar.addMenu("表示(&V)")
        self.SetViewMenu(notepad, viewMenu)
        
        # ヘルプ(H)
        helpMenu = menubar.addMenu("ヘルプ(&H)")
        self.SetHelpMenu(notepad, helpMenu)
        
    def SetFileMenu(self, notepad, fileMenu):
        """ファイルメニュー項目を追加します。
        
        引数:
        ----------
        fileMenu object:
        ファイルメニュー項目のオブジェクト
        """
        # ファイル(F) → 新規(N)
        fileNew = QAction("新規(&N)", notepad)
        fileNew.setShortcut("Ctrl+N")
        fileNew.triggered.connect(None)
        fileMenu.addAction(fileNew)
        
        # ファイル(F) → 新しいウィンドウ(W)
        fileNewWindow = QAction("新しいウィンドウ(&W)", notepad)
        fileNewWindow.setShortcut("Ctrl+Shift+N")
        fileNewWindow.triggered.connect(None)
        fileMenu.addAction(fileNewWindow)
        
        # ファイル(F) → 開く...(O)
        fileOpen = QAction("開く(&O)...", notepad)
        fileOpen.setShortcut("Ctrl+O")
        fileOpen.triggered.connect(None)
        fileMenu.addAction(fileOpen)
        
        # ファイル(F) → 上書き保存(S)
        fileSave = QAction("上書き保存(&S)", notepad)
        fileSave.setShortcut("Ctrl+S")
        fileSave.triggered.connect(None)
        fileMenu.addAction(fileSave)
        
        # ファイル(F) → 名前を付けて保存...(A)
        fileSaveAs = QAction("名前を付けて保存(&A)...", notepad)
        fileSaveAs.setShortcut("Ctrl+Shift+S")
        fileSaveAs.triggered.connect(None)
        fileMenu.addAction(fileSaveAs)
        
        fileMenu.addSeparator()
        
        # ファイル(F) → 終了(X)
        fileExit = QAction("終了(&X)", notepad)
        fileExit.setShortcut("Ctrl+Q")
        fileExit.triggered.connect(None)
        fileMenu.addAction(fileExit)
        
    def SetEditMenu(self, notepad, editMenu):
        """編集メニュー項目を追加します。
        
        引数:
        ----------
        editMenu object:
        編集メニュー項目のオブジェクト
        """
        # 編集(E) → 元に戻す(U)
        editUndo = QAction("元に戻す(&U)", notepad)
        editUndo.setShortcut("Ctrl+Z")
        editUndo.triggered.connect(None)
        editMenu.addAction(editUndo)
        
        editMenu.addSeparator()
        
        # 編集(E) → 切り取り(T)
        editCut = QAction("切り取り(&T)", notepad)
        editCut.setShortcut("Ctrl+X")
        editCut.triggered.connect(None)
        editMenu.addAction(editCut)
        
        # 編集(E) → コピー(C)
        editCopy = QAction("コピー(&C)", notepad)
        editCopy.setShortcut("Ctrl+C")
        editCopy.triggered.connect(None)
        editMenu.addAction(editCopy)
        
        # 編集(E) → 貼り付け(P)
        editPaste = QAction("貼り付け(&P)", notepad)
        editPaste.setShortcut("Ctrl+V")
        editPaste.triggered.connect(None)
        editMenu.addAction(editPaste)
        
        # 編集(E) → 削除(L)
        editDelete = QAction("削除(&L)", notepad)
        editDelete.setShortcut("Del")
        editDelete.triggered.connect(None)
        editMenu.addAction(editDelete)
        
        editMenu.addSeparator()
        
        # 編集(E) → Bing で検索(S)...
        editSearchBing = QAction("Bing で検索(&S)...", notepad)
        editSearchBing.setShortcut("Ctrl+E")
        editSearchBing.triggered.connect(None)
        editMenu.addAction(editSearchBing)
        
        # 編集(E) → 検索(F)...
        editSearch = QAction("検索(&F)...", notepad)
        editSearch.setShortcut("Ctrl+F")
        editSearch.triggered.connect(None)
        editMenu.addAction(editSearch)
        
        # 編集(E) → 次を検索(N)
        editSearchForward = QAction("次を検索(&N)", notepad)
        editSearchForward.setShortcut("F3")
        editSearchForward.triggered.connect(None)
        editMenu.addAction(editSearchForward)
        
        # 編集(E) → 前を検索(V)
        editSearchBackward = QAction("前を検索(&V)", notepad)
        editSearchBackward.setShortcut("Shift+F3")
        editSearchBackward.triggered.connect(None)
        editMenu.addAction(editSearchBackward)
        
        # 編集(E) → 置換(R)...
        editReplace = QAction("置換(&R)...", notepad)
        editReplace.setShortcut("Ctrl+R")
        editReplace.triggered.connect(None)
        editMenu.addAction(editReplace)
        
        # 編集(E) → 移動(G)...
        editJump = QAction("移動(&G)...", notepad)
        editJump.setShortcut("Ctrl+J")
        editJump.triggered.connect(None)
        editMenu.addAction(editJump)
        
        editMenu.addSeparator()
        
        # 編集(E) → すべて選択(A)
        editSelectAll = QAction("すべて選択(&A)", notepad)
        editSelectAll.setShortcut("Ctrl+A")
        editSelectAll.triggered.connect(None)
        editMenu.addAction(editSelectAll)
        
        # 編集(E) → 日付と時刻(D)
        editDateAndTime = QAction("日付と時刻(&D)", notepad)
        editDateAndTime.setShortcut("F5")
        editDateAndTime.triggered.connect(None)
        editMenu.addAction(editDateAndTime)
        
    def SetFormatMenu(self, notepad, formatMenu):
        """書式メニュー項目を追加します。
        
        引数:
        ----------
        formatMenu object:
        書式メニュー項目のオブジェクト
        """
        # 書式(O) → 右端で折り返す(W)
        formatFoldback = QAction("右端で折り返す(&W)", notepad)
        formatFoldback.setShortcut("")
        formatFoldback.triggered.connect(None)
        formatMenu.addAction(formatFoldback)
        
        # 書式(O) → フォント(F)...
        formatFont = QAction("フォント(&F)...", notepad)
        formatFont.setShortcut("")
        formatFont.triggered.connect(None)
        formatMenu.addAction(formatFont)
        
    def SetViewMenu(self, notepad, viewMenu):
        """表示メニュー項目を追加します。
        
        引数:
        ----------
        viewMenu object:
        表示メニュー項目のオブジェクト
        """
        # 表示(V) → ズーム(Z)
        viewZoom = QAction("ズーム(&Z)", notepad)
        viewZoom.setShortcut("")
        viewZoom.triggered.connect(None)
        viewMenu.addAction(viewZoom)
        
        # 表示(V) → ステータスバー(S)
        viewStatusbar = QAction("ステータスバー(&S)", notepad)
        viewStatusbar.setShortcut("")
        viewStatusbar.triggered.connect(None)
        viewMenu.addAction(viewStatusbar)
        
    def SetHelpMenu(self, notepad, helpMenu):
        """ヘルプメニュー項目を追加します。
        
        引数:
        ----------
        helpMenu object:
        ヘルプメニュー項目のオブジェクト
        """
        # ヘルプ(H) → ヘルプの表示(H)
        helpShow = QAction("ヘルプの表示(&H)", notepad)
        helpShow.setShortcut("")
        helpShow.triggered.connect(None)
        helpMenu.addAction(helpShow)
        
        # ヘルプ(H) → フィードバックの送信(F)
        helpSendFeedback = QAction("フィードバックの送信(&F)", notepad)
        helpSendFeedback.setShortcut("")
        helpSendFeedback.triggered.connect(None)
        helpMenu.addAction(helpSendFeedback)
        
        helpMenu.addSeparator()
        
        # ヘルプ(H) → Pyside6でメモ帳のバージョン情報(A)
        helpThisVersion = QAction("Pyside6でメモ帳のバージョン情報(&A)", notepad)
        helpThisVersion.setShortcut("")
        helpThisVersion.triggered.connect(None)
        helpMenu.addAction(helpThisVersion)


class Textbox:
    def __init__(self, notepad, textbox):
        pass


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
        # 継承元クラス(QWidget)の初期化
        super().__init__(parent)
        
        self.windowWidth = width
        self.windowHeight = height
        self.windowTitle = title + " - PySide6でメモ帳"
        
        # ウィンドウ設定
        self.resize(self.windowWidth, self.windowHeight)
        self.setWindowTitle(self.windowTitle)
        
        # 各ウィジェットの生成と機能追加
        self.BuildUi()
        
    def BuildUi(self):
        """各ウィジェットの生成と機能追加を行います。
        """
        vBox = QVBoxLayout()
        
        # メニューバーの作成
        self.menubar = QMenuBar(self)
        Menubar(self, self.menubar)
        
        # テキストボックス
        self.textbox = QTextEdit(self)
        Textbox(self, self.textbox)
        
        vBox.addWidget(self.menubar)
        vBox.addWidget(self.textbox)
        
        self.setLayout(vBox)


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    pluginPath = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = pluginPath
    
    app = QApplication(sys.argv)
    notepad = NotePad()
    notepad.show()
    sys.exit(app.exec())