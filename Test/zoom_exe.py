from pywinauto.application import Application
from pywinauto.timings import time

zoom_app = Application(backend="uia").start(r"ruta de Zoom.exe") #insertar acá la ruta de tu aplicación

dlg = zoom_app.window(title_re='.*Zoom.*')
dlg.wait("visible", timeout=20)

sign_in = zoom_app.ZoomWorkplace.child_window(title="Iniciar sesión", control_type="Button").wrapper_object()
sign_in.click_input()

email_box = zoom_app.ZoomWorkplace.child_window(title="Correo electrónico o número de teléfono", control_type="Edit")
email_box.type_keys('^a{BACKSPACE}')
email_box.type_keys("email") #insertar acá el email de tu cuenta de Zoom

next_button_01 = zoom_app.ZoomWorkplace.child_window(title="Siguiente", control_type="Button")
next_button_01.click_input()

pwd_box = zoom_app.ZoomWorkplace.child_window(title="Contraseña", control_type="Edit")
pwd_box.type_keys('^a{BACKSPACE}')
pwd_box.type_keys("password") #insertar acá la contraseña de tu cuenta de Zoom

sign_in_button = zoom_app.ZoomWorkplace.child_window(title="Iniciar sesión", control_type="Button")
sign_in_button.click_input()

digit1 = zoom_app.ZoomWorkplace.child_window(title="Introducir el dígito 1 del código de verificación En blanco", control_type="Edit")
digit1.wait("visible",timeout=10)
digit1.wrapper_object()
digit1.click_input()
digit1.type_keys('6')

digit2 = zoom_app.ZoomWorkplace.child_window(title="Dígito 2 En blanco", control_type="Edit").wrapper_object()
digit2.type_keys('5')

digit3 = zoom_app.ZoomWorkplace.child_window(title="Dígito 3 En blanco", control_type="Edit").wrapper_object()
digit3.type_keys('4')

digit4 = zoom_app.ZoomWorkplace.child_window(title="Dígito 4 En blanco", control_type="Edit").wrapper_object()
digit4.type_keys('3')

digit5 = zoom_app.ZoomWorkplace.child_window(title="Dígito 5 En blanco", control_type="Edit").wrapper_object()
digit5.type_keys('2')

digit6 = zoom_app.ZoomWorkplace.child_window(title="Dígito 6 En blanco", control_type="Edit").wrapper_object()
digit6.type_keys('1')

time.sleep(2)

verify_button = zoom_app.ZoomWorkplace.child_window(title="Verificar", control_type="Button").wrapper_object()
verify_button.click_input()


assert digit1.exists(), "El campo del dígito 1 no existe"
assert digit1.is_visible(), "El campo del dígito 1 no es visible"

assert verify_button.window_text() == "Verificar", "El botón no es 'Verificar'"

error_msg = zoom_app.ZoomWorkplace.child_window(title="El código de verificación que ha introducido es incorrecto", control_type="Text")
assert error_msg.exists(), "No apareció el mensaje de error esperado"


time.sleep(3)
identifier = zoom_app.ZoomWorkplace.print_control_identifiers()