import pyautogui

def draw_line(start_x,start_y,move_x,move_y):
    pyautogui.mouseDown(start_x,start_y)
    pyautogui.move(move_x,move_y)
    pyautogui.mouseUp()

if __name__ == "__main__":
    draw_line(1081,350,309,-150)
    draw_line(1390,200,309,147)
    draw_line(1699,347,0,303)
    draw_line(1699,650,-618,0)
    draw_line(1081,650,0,-303)
    draw_line(1081,350,618,0)
    draw_line(1458,651,0,-200)
    draw_line(1458,451,150,0)
    draw_line(1608,451,0,200)
    draw_line(1165,400,80,0)
    draw_line(1245,400,0,80)
    draw_line(1245,480,-80,0)
    draw_line(1165,480,0,-80)
    pyautogui.screenshot('image.png')
