import os
from pathlib import Path
from kivy.resources import resource_add_path
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mui.chat.ChatScreen import ChatScreen
from mem.chat.ChatManager import ChatManager
from mlo.chat.ChatService import ChatService
from mlo.database.firebaseChatDB import FChatDB

os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class CustomApp( MDApp):
    KV_FILES = [ 
                 'mui/chat/ChatScreen.kv',
               ]
    #DEBUG = True

    CLASSES = {
        'ChatScreen': 'mui.chat.ChatScreen'
    }

    def build_app(self):
        global manager
        manager = ScreenManager()
        userID = '1KNReiiLyeguu1FZVtM926FPAHa2'
        db = FChatDB()
        service = ChatService(db, 'testChat', userID)
        screen = ChatScreen()
        manager.add_widget(screen)
        controller = ChatManager(screen, service, userID) 
        
        return manager


CustomApp().run()