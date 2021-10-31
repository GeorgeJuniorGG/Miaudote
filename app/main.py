import os
from pathlib import Path

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.core.window import Window

os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
KV_DIR = f"{os.environ['MIAUDOTE_ROOT']}/mui/kvfiles"
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

for kv_file in os.listdir(KV_DIR):
    kv = str(os.path.join(KV_DIR, kv_file))
    Builder.load_file(kv)

KV = """
MainScreenManager:
"""

Window.size = (375,667)

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()