using System;
using System.Windows.Forms;

namespace LightCodeEditor {
    class MainWindow: Form {
        private void InitializeComponent() {
            this.Text = "LightCodeEditor";
        }
        
        public MainWindow() {
            InitializeComponent();
        }
    }
    
    class Program {
        static void Main(string[] args) {
            Application.EnableVisualStyles();
            Application.Run(new MainWindow());
        }
    }
}