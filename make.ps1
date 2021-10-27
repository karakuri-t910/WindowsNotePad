$POWERSHELL = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$PSHELL_ARGS= "-Command"

# �R���p�C��
$CC         = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
# ���s�`��
$TARGET     = "winexe"
# �\�[�X�t�@�C��
$SRC_FILES  = ".\src\Program.cs"
# ���C�u�����iDLL�j
$DLL_FILES  = ""
# ���s�t�@�C��
$EXE_FILE   = "LightCodeEditor.exe"

if (!$Args.Length) {
    # �R���p�C�����s�F�擪�� & �͎��s���Z�q
    & $CC /target:$TARGET /out:$EXE_FILE /optimize+ $SRC_FILES
}
else {
    switch ($Args[0]) {
        "clean" {
            # �f�o�b�O���ipdb�t�@�C���j������΍폜
            $ISEXIST = Test-Path *.pdb
            if ($ISEXIST) {
                & Remove-Item *.pdb
            }
            # EXE�t�@�C���̍폜
            & Remove-Item $EXE_FILE
        }
        "debug" {
            # �R���p�C�����Ƀf�o�b�O���ipdb�t�@�C���j���o��
            & $CC  /target:$TARGET /out:$EXE_FILE /optimize+ $SRC_FILES /debug:full
        }
        "run" {
            # �v���O�������s
            & Start-Process $EXE_FILE
        }
    }
}