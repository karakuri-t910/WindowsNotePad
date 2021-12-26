using System;
using System.IO;
using System.Runtime.CompilerServices;
using System.Windows.Forms;

namespace LightCodeEditor {
    class Debug {
        // <summary>
        // ログをコンソール上に表示
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
        // メインメソッド
        // </summary>
        [STAThread]
        static void Main(string[] args) {
            Application.EnableVisualStyles();
            // アプリを実行
            Application.Run(new MainWindow());
        }
    }
}