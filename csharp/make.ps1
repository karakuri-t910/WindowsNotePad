# コンパイラ
$CC         = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"

# 実行形式
$TARGET     = "winexe"

# ソースファイル（必ず配列で指定）
$SRC_FILES = @(".\src\Program.cs",
               ".\src\Window.cs",
               ".\src\Window.Designer.cs")

# ライブラリ（DLL）
$DLL_FILES  = @("/reference:")

# 実行ファイル
$EXE_FILE   = "LightCodeEditor.exe"

# 実行権限を取得
$STATE = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$IS_ADMIN = $STATE.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# カレントディレクトリ
$CURRENT_DIR = [System.IO.Directory]::GetCurrentDirectory()




<##
 # ヘルプの表示
 #>
function ShowHelp() {
    Write-Output "Help:"
    Write-Output "    ./make.ps1 [option]"
    Write-Output ""
    Write-Output "    [option]"
    Write-Output "        clean:"
    Write-Output "            コンパイルして生成されたファイルを削除します。"
    Write-Output "        debug:"
    Write-Output "            デバッグ情報を表示する処理を有効にしてコンパイルします。"
    Write-Output "        help:"
    Write-Output "            当スクリプトの使い方を表示します。"
    Write-Output "        run:"
    Write-Output "            アプリの実行をします。"
    Write-Output "        setup:"
    Write-Output "            【管理者権限でのみ実行可能】"
    Write-Output "            開発環境を構築します。"
    Write-Output "            必要な外部ライブラリのダウンロードなど。"
    Write-Output "        teardown:"
    Write-Output "            【管理者権限でのみ実行可能】"
    Write-Output "            setup で構築した開発環境を削除します。"
}

<##
 # 開発環境の構築
 #>
function SetUp() {
    # パッケージ
    $PACKAGE_SOURCE = "https://www.nuget.org/api/v2"
    
    # パッケージ保存先
    $INSTALL_DEST = $CURRENT_DIR + "\packages"
    
    # NuGet を最新に更新
    Install-PackageProvider Nuget -Verbose
    
    # パッケージのダウンロード
    Find-Package -Name ScottPlot -Source $PACKAGE_SOURCE
    Install-Package ScottPlot -Source $PACKAGE_SOURCE -Force -SkipDependencies -Destination $INSTALL_DEST
}

<##
 # setup で構築した環境を削除する
 #>
function TearDown() {
    Uninstall-Package ScottPlot -Source $INSTALL_DEST
}





if (!$Args.Length) {
    # コンパイル実行：先頭の & は実行演算子
    & $CC /target:$TARGET /out:$EXE_FILE /optimize+ $SRC_FILES
}
else {
    switch ($Args[0]) {
        "clean" {
            # デバッグ情報（pdbファイル）があれば削除
            $ISEXIST = Test-Path *.pdb
            if ($ISEXIST) {
                & Remove-Item *.pdb
            }
            # EXEファイルの削除
            & Remove-Item $EXE_FILE
        }
        "debug" {
            $TARGET = "exe"
            $DEF_SYMBOL = "DEBUG"
            # コンパイル時にデバッグ情報（pdbファイル）も出力
            & $CC /target:$TARGET /out:$EXE_FILE /define:$DEF_SYMBOL /optimize+ $SRC_FILES /debug:full
        }
        "help" {
            ShowHelp
        }
        "run" {
            # プログラム実行
            & Start-Process $EXE_FILE
        }
        "setup" {
            if (!$IS_ADMIN) {
                Write-Output "setup は「管理者で実行」してください。"
                exit
            }
            
            SetUp
        }
        "teardown" {
            if (!$IS_ADMIN) {
                Write-Output "setup は「管理者で実行」してください。"
                exit
            }
            
            TearDown
        }
    }
}