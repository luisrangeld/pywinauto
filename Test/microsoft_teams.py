import pywinauto
import pyperclip
from pywinauto.application import Application
import time

teams_app = Application(backend="uia").connect(title_re=".*Microsoft Teams")
dlg = teams_app.window(title_re=".*Microsoft Teams")
dlg.wait("visible", timeout=10)

luis_chat = dlg.child_window(title="Chat Luis Rangel (Usted)", auto_id="menur1b", control_type="TreeItem").wait("ready", timeout=10)
luis_chat.click_input()

message = "Hello from Pywinauto via paste method! 🚀"
pyperclip.copy(message)

msg_box = dlg.child_window(title="Escribe un mensaje\n", auto_id="new-message-0b55198a-344b-45cd-b393-378f285f6983", control_type="Edit").wrapper_object()
msg_box.set_focus()
time.sleep(1)
msg_box.type_keys("^v")
msg_box.type_keys("{ENTER}")
time.sleep(5)


