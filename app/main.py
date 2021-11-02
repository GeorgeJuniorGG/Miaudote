import os
from pathlib import Path
from sys import platform
from kivy.lang.builder import Builder

from kivymd.app import MDApp
from kivy.resources import resource_add_path
from kivy.core.window import Window
from kivy.factory import Factory

os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class MainApp(MDApp):

    # [hotfix] problema na atualização do kivymd
    def load_all_kv_files(self, path_to_directory):
        for path_to_dir, dirs, files in os.walk(path_to_directory):
            if "venv" in path_to_dir or "__pycache__" in path_to_dir:
                continue
            for name_file in files:
                if (
                    os.path.splitext(name_file)[1] == ".kv"
                    and name_file != "style.kv"  # if use PyInstaller
                    and "__MACOS" not in path_to_dir  # if use Mac OS
                ):
                    path_to_kv_file = os.path.join(path_to_dir, name_file)
                    Builder.load_file(path_to_kv_file)

    def register_views(self):
        separator = '/'
        # [hotfix] problema dos separadores windows
        if platform == 'win32':
            separator = '\\'

        for path_to_dir, dirs, files in os.walk(self.directory):
            if "venv" in path_to_dir or "__pycache__" in path_to_dir:
                continue
            for name_file in files:
                if (os.path.splitext(name_file)[1] == ".py"
                    and name_file.find("Screen") != -1):
                    className = os.path.splitext(name_file)[0]
                    module = path_to_dir.split(separator)

                    pkg = ''
                    for i in range(len(module)-2, len(module)):
                        pkg += f'{module[i]}.'
                    pkg += f'{className}'

                    Factory.register(className, module=pkg)
                    
    def build(self):
        self.register_views()
        self.load_all_kv_files(self.directory)
        return Factory.MainScreenManager()

MainApp().run()