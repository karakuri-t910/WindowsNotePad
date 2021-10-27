$POWERSHELL = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$PSHELL_ARGS= "-Command"

# コンパイラ
$CC         = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
# 実行形式
$TARGET     = "winexe"
# ソースファイル
$SRC_FILES  = ".\src\Program.cs"
# ライブラリ（DLL）
$DLL_FILES  = ""
# 実行ファイル
$EXE_FILE   = "LightCodeEditor.exe"

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
            # コンパイル時にデバッグ情報（pdbファイル）も出力
            & $CC  /target:$TARGET /out:$EXE_FILE /optimize+ $SRC_FILES /debug:full
        }
        "run" {
            # プログラム実行
            & Start-Process $EXE_FILE
        }
    }
}