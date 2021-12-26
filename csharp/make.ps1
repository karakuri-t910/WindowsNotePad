# �R���p�C��
$CC         = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"

# ���s�`��
$TARGET     = "winexe"

# �\�[�X�t�@�C���i�K���z��Ŏw��j
$SRC_FILES = @(".\src\Program.cs",
               ".\src\Window.cs",
               ".\src\Window.Designer.cs")

# ���C�u�����iDLL�j
$DLL_FILES  = @("/reference:")

# ���s�t�@�C��
$EXE_FILE   = "LightCodeEditor.exe"

# ���s�������擾
$STATE = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$IS_ADMIN = $STATE.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# �J�����g�f�B���N�g��
$CURRENT_DIR = [System.IO.Directory]::GetCurrentDirectory()




<##
 # �w���v�̕\��
 #>
function ShowHelp() {
    Write-Output "Help:"
    Write-Output "    ./make.ps1 [option]"
    Write-Output ""
    Write-Output "    [option]"
    Write-Output "        clean:"
    Write-Output "            �R���p�C�����Đ������ꂽ�t�@�C�����폜���܂��B"
    Write-Output "        debug:"
    Write-Output "            �f�o�b�O����\�����鏈����L���ɂ��ăR���p�C�����܂��B"
    Write-Output "        help:"
    Write-Output "            ���X�N���v�g�̎g������\�����܂��B"
    Write-Output "        run:"
    Write-Output "            �A�v���̎��s�����܂��B"
    Write-Output "        setup:"
    Write-Output "            �y�Ǘ��Ҍ����ł̂ݎ��s�\�z"
    Write-Output "            �J�������\�z���܂��B"
    Write-Output "            �K�v�ȊO�����C�u�����̃_�E�����[�h�ȂǁB"
    Write-Output "        teardown:"
    Write-Output "            �y�Ǘ��Ҍ����ł̂ݎ��s�\�z"
    Write-Output "            setup �ō\�z�����J�������폜���܂��B"
}

<##
 # �J�����̍\�z
 #>
function SetUp() {
    # �p�b�P�[�W
    $PACKAGE_SOURCE = "https://www.nuget.org/api/v2"
    
    # �p�b�P�[�W�ۑ���
    $INSTALL_DEST = $CURRENT_DIR + "\packages"
    
    # NuGet ���ŐV�ɍX�V
    Install-PackageProvider Nuget -Verbose
    
    # �p�b�P�[�W�̃_�E�����[�h
    Find-Package -Name ScottPlot -Source $PACKAGE_SOURCE
    Install-Package ScottPlot -Source $PACKAGE_SOURCE -Force -SkipDependencies -Destination $INSTALL_DEST
}

<##
 # setup �ō\�z���������폜����
 #>
function TearDown() {
    Uninstall-Package ScottPlot -Source $INSTALL_DEST
}





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
            $TARGET = "exe"
            $DEF_SYMBOL = "DEBUG"
            # �R���p�C�����Ƀf�o�b�O���ipdb�t�@�C���j���o��
            & $CC /target:$TARGET /out:$EXE_FILE /define:$DEF_SYMBOL /optimize+ $SRC_FILES /debug:full
        }
        "help" {
            ShowHelp
        }
        "run" {
            # �v���O�������s
            & Start-Process $EXE_FILE
        }
        "setup" {
            if (!$IS_ADMIN) {
                Write-Output "setup �́u�Ǘ��҂Ŏ��s�v���Ă��������B"
                exit
            }
            
            SetUp
        }
        "teardown" {
            if (!$IS_ADMIN) {
                Write-Output "setup �́u�Ǘ��҂Ŏ��s�v���Ă��������B"
                exit
            }
            
            TearDown
        }
    }
}