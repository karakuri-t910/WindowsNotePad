using System;
using System.Windows.Forms;

namespace LightCodeEditor {
    class Program {
        [STAThread]
        static void Main(string[] args) {
            Application.EnableVisualStyles();
            // アプリを実行
            Application.Run(new MainWindow());
        }
    }
}