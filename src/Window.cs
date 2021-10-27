using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace LightCodeEditor {
    class MainWindow: Form {
        void onOpen(object sender, EventArgs e) {
            OpenFileDialog file = new OpenFileDialog();
            file.Title = "�J��";
            file.InitialDirectory = Path.GetDirectoryName(Application.ExecutablePath);
            if (file.ShowDialog() == DialogResult.OK ) {
                Controls[1].Text = File.ReadAllText(file.FileName);
            }
        }
        
        void onSaveAs(object sender, EventArgs e) {
            SaveFileDialog file = new SaveFileDialog();
            file.Title = "���O��t���ĕۑ�";
            file.InitialDirectory = Path.GetDirectoryName(Application.ExecutablePath);
            if (file.ShowDialog() == DialogResult.OK ) {
                File.WriteAllText(file.FileName, Controls[1].Text);
            }
        }
        
        void onExit(object sender, EventArgs e) {
            Close();
        }
        
        private void InitializeComponent() {
            // �^�C�g��
            this.Text = "LightCodeEditor";
            this.ClientSize = new Size(600, 500);
            
            // ���j���[�o�[
            ToolStripMenuItem fileMenu = new ToolStripMenuItem();
            fileMenu.Text = "�t�@�C��(&F)";
            fileMenu.ShortcutKeys = Keys.Control | Keys.F;
            
            ToolStripMenuItem fileOpen = new ToolStripMenuItem();
            fileOpen.Text = "�J��...(&O)";
            fileOpen.ShortcutKeys = Keys.Control | Keys.O;
            fileOpen.Click += onOpen;
            fileMenu.DropDownItems.Add(fileOpen);
            
            ToolStripMenuItem fileSaveAs = new ToolStripMenuItem();
            fileSaveAs.Text = "���O��t���ĕۑ�...(&A)";
            fileSaveAs.ShortcutKeys = Keys.Control | Keys.Shift | Keys.S;
            fileSaveAs.Click += onSaveAs;
            fileMenu.DropDownItems.Add(fileSaveAs);
            
            fileMenu.DropDownItems.Add(new ToolStripSeparator());
            
            ToolStripMenuItem fileExit = new ToolStripMenuItem();
            fileExit.Text = "�I��(&X)";
            fileExit.Click += onExit;
            fileMenu.DropDownItems.Add(fileExit);
            
            // ���j���[�o�[
            MenuStrip menuBar = new MenuStrip();
            menuBar.Items.Add(fileMenu);
            this.Controls.Add(menuBar);
            
            // �e�L�X�g�{�b�N�X
            TextBox textbox = new TextBox();
            textbox.Font = new Font("YuGothR", 12);
            textbox.Top = menuBar.ClientSize.Height;
            textbox.Width = ClientRectangle.Width;
            textbox.Height = ClientRectangle.Height - textbox.Top;
            textbox.Multiline = true;
            textbox.Anchor = AnchorStyles.Left  |
                             AnchorStyles.Right |
                             AnchorStyles.Top   |
                             AnchorStyles.Bottom;
            this.Controls.Add(textbox);
        }
        
        // �R���X�g���N�^
        public MainWindow() {
            // �E�B���h�E�̍\��
            InitializeComponent();
        }
    }
}