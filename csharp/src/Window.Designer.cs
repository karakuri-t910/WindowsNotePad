using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace LightCodeEditor {
    partial class MainWindow {
        private MenuStrip           menuBar     = new MenuStrip();
        
        private ToolStripMenuItem   fileMenu    = new ToolStripMenuItem();
        private ToolStripMenuItem   fileOpen    = new ToolStripMenuItem();
        private ToolStripMenuItem   fileSave    = new ToolStripMenuItem();
        private ToolStripMenuItem   fileSaveAs  = new ToolStripMenuItem();
        private ToolStripMenuItem   fileExit    = new ToolStripMenuItem();
        
        private ToolStripMenuItem   othersMenu  = new ToolStripMenuItem();
        private ToolStripMenuItem   othersFont  = new ToolStripMenuItem();
        
        private RichTextBox         textbox     = new RichTextBox();
        
        // <summary>
        // 
        // </summary>
        private void CreateWindow() {
            // �^�C�g��
            if (this.fileName == null) {
                this.Text = "LightCodeEditor: " + "(New File)";
            }
            else {
                this.Text = "LightCodeEditor: " + this.fileName;
            }
            this.ClientSize = new Size(600, 500);
        }
        
        // <summary>
        // 
        // </summary>
        private void CreateFileMenu() {
            this.fileMenu.Text = "�t�@�C��(&F)";
            this.fileMenu.ShortcutKeys = Keys.Control | Keys.F;
            
            this.fileOpen.Text = "�J��...(&O)";
            this.fileOpen.ShortcutKeys = Keys.Control | Keys.O;
            this.fileOpen.Click += ClickOpen;
            this.fileMenu.DropDownItems.Add(this.fileOpen);
            
            this.fileSave.Text = "�ۑ�(&S)";
            this.fileSave.ShortcutKeys = Keys.Control | Keys.S;
            this.fileSave.Click += ClickSave;
            this.fileMenu.DropDownItems.Add(this.fileSave);
            
            this.fileSaveAs.Text = "���O��t���ĕۑ�...(&A)";
            this.fileSaveAs.ShortcutKeys = Keys.Control | Keys.Shift | Keys.S;
            this.fileSaveAs.Click += ClickSaveAs;
            this.fileMenu.DropDownItems.Add(this.fileSaveAs);
            
            this.fileMenu.DropDownItems.Add(new ToolStripSeparator());
            
            this.fileExit.Text = "�I��(&X)";
            this.fileExit.ShortcutKeys = Keys.Control | Keys.W;
            this.fileExit.Click += ClickExit;
            this.fileMenu.DropDownItems.Add(this.fileExit);
        }
        
        // <summary>
        // 
        // </summary>
        private void CreateOthersMenu() {
            this.othersMenu.Text = "���̑�(&O)";
            
            this.othersFont.Text = "�t�H���g";
            this.othersFont.Click += ClickOthersFont;
            this.othersMenu.DropDownItems.Add(this.othersFont);
        }
        
        // <summary>
        // 
        // </summary>
        private void CreateMenuBar() {
            this.menuBar.Items.Add(this.fileMenu);
            this.menuBar.Items.Add(this.othersMenu);
        }
        
        // <summary>
        // 
        // </summary>
        private void CreateTextbox() {
            this.textbox.Font = new Font("MS UI Gothic", 12);
            this.textbox.Top = this.menuBar.ClientSize.Height;
            this.textbox.Width = ClientRectangle.Width;
            this.textbox.Height = ClientRectangle.Height - this.textbox.Top;
            this.textbox.Multiline = true;
            this.textbox.Anchor = AnchorStyles.Left  |
                                  AnchorStyles.Right |
                                  AnchorStyles.Top   |
                                  AnchorStyles.Bottom;
            this.textbox.ScrollBars = RichTextBoxScrollBars.Vertical;
        }
        
        // <summary>
        // 
        // </summary>
        private void InitializeComponent() {
            // 
            this.SuspendLayout();
            
            // �E�B���h�E
            this.CreateWindow();
            
            // �u�t�@�C��(F)�v���j���[
            this.CreateFileMenu();
            
            // �u���̑�(O)�v���j���[
            this.CreateOthersMenu();
            
            // ���j���[�o�[
            this.CreateMenuBar();
            
            // �e�L�X�g�{�b�N�X
            this.CreateTextbox();
            
            this.Controls.Add(this.menuBar);
            this.Controls.Add(this.textbox);
            
            // 
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}