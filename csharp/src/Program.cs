using System;
using System.IO;
using System.Runtime.CompilerServices;
using System.Windows.Forms;

namespace LightCodeEditor {
    class Debug {
        // <summary>
        // ���O���R���\�[����ɕ\��
        // </summary>
        public static void Log(string message,
            [CallerFilePath]   string filename = null,
            [CallerMemberName] string membername = null,
            [CallerLineNumber] uint   line = 0)
        {
            Console.WriteLine("[{0}]{1}({2}): {3}", Path.GetFileName(filename), membername, line, message);
        }
    }
    
    class Program {
        // <summary>
        // ���C�����\�b�h
        // </summary>
        [STAThread]
        static void Main(string[] args) {
            Application.EnableVisualStyles();
            // �A�v�������s
            Application.Run(new MainWindow());
        }
    }
}