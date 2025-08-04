from subprocess import Popen
from pywinauto import Desktop
from time import sleep

Popen('calc.exe', shell = True )
dialog = Desktop(backend='uia').Calculator
dialog.wait('visible')
sleep(3)
dialog.Tres.click()
sleep(1)
dialog.Más.click()
sleep(1)
dialog.Siete.click()
sleep(1)
# puedo tambien usar dialog.Es_igual_a.click()
dialog.child_window(title="Es igual a", auto_id="equalButton", control_type="Button").click()
