using System;
using System.Windows.Forms;

namespace LightCodeEditor {
    class Program {
        [STAThread]
        static void Main(string[] args) {
            Application.EnableVisualStyles();
            // ƒAƒvƒŠ‚ğÀs
            Application.Run(new MainWindow());
        }
    }
}