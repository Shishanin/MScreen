import keyboard
import pyautogui
import time
import os
import pystray
import PIL.Image
from winotify import Notification
import ctypes
import sys
image = PIL.Image.open('logo_app.png')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    
    def screen_mirror():
        screenTime = time.time()
        file_dir = str(os.path.abspath(os.getcwd()) + "\MScreenshots")
        filename = str(f'{file_dir}\ScreenShot-{screenTime}.png')

        try:
            os.makedirs(file_dir)
        except FileExistsError:
            print('Директория уже существует')

        
        pyautogui.screenshot(filename)

        screen_sins = Notification(
            app_id='MScreen',
            title='Screenshot screated',
            msg=filename,
            duration='short',
            icon=filename
        )   
        screen_sins.add_actions('Open Image', launch=filename)
        screen_sins.show()


    def open_dir():
        os.system(str("explorer.exe " + os.path.abspath(os.getcwd()) + "\MScreenshots"))


    def exit_app():
        app.stop()


    app = pystray.Icon("MScreen", image, menu=pystray.Menu(
        pystray.MenuItem('Screenshot', screen_mirror),
        pystray.MenuItem('Open Folder', open_dir),
        pystray.MenuItem('Exit', exit_app)
    ))

    keyboard.add_hotkey('Print Screen', screen_mirror)
    app.run()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)