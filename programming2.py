from functools import reduce
from PIL import Image
import pyautogui
import time

middle = (950, 550)
top_left = (100, 150)
top_right = (3000, 150)



def drag_down():
    pyautogui.moveTo(middle[0], 130+850, 0.1)
    pyautogui.dragTo(middle[0], 70, 0.8)
    time.sleep(0.2)


def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height), 'white')
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst



def get_left_page():
    images = []
    x = 75
    images.append(pyautogui.screenshot(region=(x, 200, 1200, 780)))
    pyautogui.moveTo(middle[0], 900)
    pyautogui.drag(0, -880, 0.5)
    pyautogui.moveTo(*middle)
    images.append(pyautogui.screenshot(region=(x, 196, 1200, 804)))
    # pyautogui.moveTo(middle[0], 900)
    # pyautogui.drag(0, -750, 0.5)
    # pyautogui.moveTo(*middle)
    # n = 210 
    # images.append(pyautogui.screenshot(region=(x, n, 1200, 900-n)))
    return reduce(get_concat_v, images)


def get_right_page():
    # pyautogui.scroll(1000)
    pyautogui.moveTo(middle[0], 150)
    time.sleep(0.5)
    pyautogui.drag(0, 880, 0.5)
    time.sleep(0.5)
    pyautogui.moveTo(2000, 300)
    pyautogui.drag(-2000, 0, 0.5)
    time.sleep(0.5)
    x = 600
    images = []
    images.append(pyautogui.screenshot(region=(x, 200, 1200, 750)))
    pyautogui.moveTo(middle[0], 900)
    pyautogui.drag(0, -880, 0.5)
    pyautogui.moveTo(*middle)
    images.append(pyautogui.screenshot(region=(x, 165, 1200, 840)))
    # pyautogui.moveTo(middle[0], 900)
    # pyautogui.drag(0, -750, 0.5)
    # pyautogui.moveTo(*middle)
    # n = 210 
    # images.append(pyautogui.screenshot(region=(x, n, 1200, 900-n)))
    return reduce(get_concat_v, images)


def save_book(name, pages):
    pyautogui.click(500, 1070)
    time.sleep(0.2)
    for i in range(pages-1):
        if i%2 == 0:
            im = get_left_page()
        else:
            
            im = get_right_page()
            pyautogui.press('right')
            time.sleep(1)
        im.save(f'{name}-page{i+1}.png')
        print(f'saved page {i+1} successfully')

name = 'programming' # input('name: ')
pages = 105 # int(input('pages count: '))
save_book(name, pages)
# pyautogui.click(500, 1070)
# time.sleep(0.2)
# get_right_page().save('screen.png')

# pyautogui.press('right')
# time.sleep(0.5)
# pyautogui.press('left')
# pyautogui.click(500, 1070)
# pyautogui.moveTo(middle[0], 100)