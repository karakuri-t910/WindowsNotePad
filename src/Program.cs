using System;
using System.Windows.Forms;

namespace LightCodeEditor {
    class Program {
        [STAThread]
        static void Main(string[] args) {
            Application.EnableVisualStyles();
            // �A�v�������s
            Application.Run(new MainWindow());
        }
    }
}