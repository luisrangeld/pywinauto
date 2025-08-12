from pywinauto import Desktop

print([x.window_text() for x in Desktop(backend='uia').windows()])