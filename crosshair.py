import win32api
import win32gui
import win32con
import cv2
import keyboard

def draw_crosshair():
    # Get the dimensions of the primary monitor
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Create a DC object
    desktop_dc = win32gui.GetDC(0)
    crosshair_pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))

    # Draw the center dot
    win32gui.SelectObject(desktop_dc, crosshair_pen)
    win32gui.MoveToEx(desktop_dc, width//2, height//2, )
    win32gui.LineTo(desktop_dc, (width//2)+1, (height//2)+1)

    # Release the DC object
    win32gui.ReleaseDC(0, desktop_dc)

# Call the draw_crosshair() in a while true to keep the crosshair function going to draw the crosshair center dot
while True:
    draw_crosshair()
    if keyboard.is_pressed("q"):
        break