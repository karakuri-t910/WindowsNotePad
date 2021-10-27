using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace LightCodeEditor {
    class MainWindow: Form {
        void onOpen(object sender, EventArgs e) {
            OpenFileDialog file = new OpenFileDialog();
            file.Title = "開く";
            file.InitialDirectory = Path.GetDirectoryName(Application.ExecutablePath);
            if (file.ShowDialog() == DialogResult.OK ) {
                Controls[1].Text = File.ReadAllText(file.FileName);
            }
        }
        
        void onSaveAs(object sender, EventArgs e) {
            SaveFileDialog file = new SaveFileDialog();
            file.Title = "名前を付けて保存";
            file.InitialDirectory = Path.GetDirectoryName(Application.ExecutablePath);
            if (file.ShowDialog() == DialogResult.OK ) {
                File.WriteAllText(file.FileName, Controls[1].Text);
            }
        }
        
        void onExit(object sender, EventArgs e) {
            Close();
        }
        
        private void InitializeComponent() {
            // タイトル
            this.Text = "LightCodeEditor";
            this.ClientSize = new Size(600, 500);
            
            // メニューバー
            ToolStripMenuItem fileMenu = new ToolStripMenuItem();
            fileMenu.Text = "ファイル(&F)";
            fileMenu.ShortcutKeys = Keys.Control | Keys.F;
            
            ToolStripMenuItem fileOpen = new ToolStripMenuItem();
            fileOpen.Text = "開く...(&O)";
            fileOpen.ShortcutKeys = Keys.Control | Keys.O;
            fileOpen.Click += onOpen;
            fileMenu.DropDownItems.Add(fileOpen);
            
            ToolStripMenuItem fileSaveAs = new ToolStripMenuItem();
            fileSaveAs.Text = "名前を付けて保存...(&A)";
            fileSaveAs.ShortcutKeys = Keys.Control | Keys.Shift | Keys.S;
            fileSaveAs.Click += onSaveAs;
            fileMenu.DropDownItems.Add(fileSaveAs);
            
            fileMenu.DropDownItems.Add(new ToolStripSeparator());
            
            ToolStripMenuItem fileExit = new ToolStripMenuItem();
            fileExit.Text = "終了(&X)";
            fileExit.Click += onExit;
            fileMenu.DropDownItems.Add(fileExit);
            
            // メニューバー
            MenuStrip menuBar = new MenuStrip();
            menuBar.Items.Add(fileMenu);
            this.Controls.Add(menuBar);
            
            // テキストボックス
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
        
        // コンストラクタ
        public MainWindow() {
            // ウィンドウの構成
            InitializeComponent();
        }
    }
}