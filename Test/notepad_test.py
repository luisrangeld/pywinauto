from pywinauto.application import Application
from pywinauto import Desktop
from time import sleep

# Paso 1: Inicia el Bloc de notas
app = Application(backend="uia").start("notepad.exe")
sleep(2)

# Paso 2: Buscar la ventana del Bloc de notas
ventana = Desktop(backend='uia').window(title_re= ".*(Bloc de notas|Notepad).*")
ventana.wait("visible", timeout=10)

# Escribir texto
ventana.type_keys("¡Hola! Soy Luis ", with_spaces=True)
sleep(2)

# Hacer click en Editar > Fecha y Hora
ventana.Editar.click_input()
sleep(1)
ventana.child_window(title="Fecha y hora", control_type="MenuItem").click_input()
sleep(2)

# Hacer Zoom
for i in range (5):
    ventana.Ver.click_input()
    sleep(2)
    ventana.child_window(title="Zoom", control_type="MenuItem").click_input()
    ventana.child_window(title="Acercar", control_type="MenuItem").click_input()
    sleep(2)
    
