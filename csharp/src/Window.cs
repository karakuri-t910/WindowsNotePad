using System;
using System.Drawing;
using System.IO;
using System.Text;
using System.Windows.Forms;

namespace LightCodeEditor {
    partial class MainWindow: Form {
        private string fileName = null;
        private string title {
            set {this.Text = value;}
            get {return this.Text;}
        }
        
        // <summary>
        // 
        // </summary>
        void ClickOpen(object sender, EventArgs e) {
            OpenFileDialog file = new OpenFileDialog();
            file.Title = "開く";
            file.InitialDirectory = Path.GetDirectoryName(Application.ExecutablePath);
            if (file.ShowDialog() == DialogResult.OK ) {
                Controls[1].Text = File.ReadAllText(file.FileName);
                fileName = file.FileName;
                this.Text = "LightCodeEditor: " + Path.GetFileName(fileName);
            }
        }
        
        // <summary>
        // 
        // </summary>
        void ClickSave(object sender, EventArgs e) {
            if (fileName == null) {
                this.ClickSaveAs(sender, e);
            }
            else {
                File.WriteAllText(fileName, Controls[1].Text, Encoding.GetEncoding("shift-jis"));
            }
        }
        
        // <summary>
        // 
        // </summary>
        void ClickSaveAs(object sender, EventArgs e) {
            SaveFileDialog file = new SaveFileDialog();
            file.Title = "名前を付けて保存";
            file.InitialDirectory = Path.GetDirectoryName(Application.ExecutablePath);
            if (file.ShowDialog() == DialogResult.OK ) {
                File.WriteAllText(file.FileName, Controls[1].Text);
                fileName = "LightCodeEditor: " + file.FileName;
            }
        }
        
        // <summary>
        // 
        // </summary>
        void ClickOthersFont(object sender, EventArgs e) {
            ;
        }
        
        // <summary>
        // 
        // </summary>
        void ClickExit(object sender, EventArgs e) {
            Close();
        }
        
        // <summary>
        // コンストラクタ
        // </summary>
        public MainWindow() {
            // ウィンドウの構成
            InitializeComponent();
        }
    }
}