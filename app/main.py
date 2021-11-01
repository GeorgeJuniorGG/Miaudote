import os
from pathlib import Path

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

    def register_views(self):
        for path_to_dir, dirs, files in os.walk(self.directory):
            if "venv" in path_to_dir or "__pycache__" in path_to_dir:
                continue
            for name_file in files:
                if (os.path.splitext(name_file)[1] == ".py"
                    and name_file.find("Screen") != -1):
                    className = os.path.splitext(name_file)[0]
                    module = path_to_dir.split('/')
                    module = f'{module[7]}.{module[8]}.{className}'
                    Factory.register(className, module=module)
                    

    def build(self):
        self.register_views()
        self.load_all_kv_files(self.directory)
        return Factory.MainScreenManager()

MainApp().run()