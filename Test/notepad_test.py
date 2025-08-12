#for Notepad I do not need to add the path because Calculator is already in Pywinauto for testing purposes

from pywinauto.application import Application
from pywinauto import Desktop
from time import sleep

# Start notepad
app = Application(backend="uia").start("notepad.exe")
sleep(2)

# Search the notepad window
ventana = Desktop(backend='uia').window(title_re= ".*(Bloc de notas|Notepad).*")
ventana.wait("visible", timeout=10)

# Write text
ventana.type_keys("¡Hola! Soy Luis ", with_spaces=True)
sleep(2)

# Click: Editar > Fecha y Hora
ventana.Editar.click_input()
sleep(1)
ventana.child_window(title="Fecha y hora", control_type="MenuItem").click_input()
sleep(2)

# Zoom In
for i in range (5):
    ventana.Ver.click_input()
    sleep(2)
    ventana.child_window(title="Zoom", control_type="MenuItem").click_input()
    ventana.child_window(title="Acercar", control_type="MenuItem").click_input()
    sleep(2)
    

