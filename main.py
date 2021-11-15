from functools import reduce
from PIL import Image
import pyautogui
import time

middle = (950, 550)
top_left = (100, 150)
top_right = (3000, 150)

def zoom_in():
    zoom_in_button = (950, 80)
    pyautogui.moveTo(*zoom_in_button)
    pyautogui.click()
    time.sleep(0.4)

def zoom_out():
    zoom_out_button = (1080, 80)
    pyautogui.moveTo(*zoom_out_button)
    pyautogui.click()
    time.sleep(0.4)

def drag_to_top_left():
    pyautogui.moveTo(*top_left, 0.2)
    pyautogui.dragTo(middle[0], middle[1]+150, 0.5)
    time.sleep(0.2)

def drag_to_top_right():
    pyautogui.moveTo(*top_right, 0.2)
    pyautogui.dragTo(middle[0], middle[1]+150, 0.5)
    time.sleep(0.2)

def drag_down():
    pyautogui.moveTo(middle[0], 130+850, 0.1)
    pyautogui.dragTo(middle[0], 70, 0.8)
    time.sleep(0.2)


def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height), 'white')
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_page():
    images = []
    images.append(pyautogui.screenshot(region=(300, 130, 1100, 850)))
    drag_down()
    images.append(pyautogui.screenshot(region=(300, 130, 1100, 850)))
    final =reduce(get_concat_v, images)
    return final


def get_left_page():
    zoom_in()
    drag_to_top_left()
    img = get_page()
    zoom_out()
    return img


def get_right_page():
    zoom_in()
    drag_to_top_right()
    img = get_page()
    zoom_out()
    return img


def save_book(name, pages):
    pyautogui.click(500, 1070)
    time.sleep(0.2)
    for i in range(pages-1):
        if i%2 == 0:
            im = get_left_page()
        else:
            im = get_right_page()
            time.sleep(0.2)
            pyautogui.moveTo(930+600, 100+850)
            pyautogui.click()
            time.sleep(0.8)
        im.save(f'{name}-page{i+1}.png')
        print(f'saved page {i+1} successfully')

name = 'radiation' # input('name: ')
pages = 5 # int(input('pages count: '))
save_book(name, pages)
# time.sleep(1)
# pyautogui.scroll(-750, *middle)
# pyautogui.moveTo(300, 130)
