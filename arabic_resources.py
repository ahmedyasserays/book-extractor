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



def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height), 'white')
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_page():
    images = []
    images.append(pyautogui.screenshot(region=(550, 220, 850, 700)))
    pyautogui.moveTo(*middle)
    pyautogui.scroll(-1000)
    time.sleep(0.5)
    images.append(pyautogui.screenshot(region=(550, 120, 850, 760)))
    final = get_concat_v(*images)
    return final


def save_book(name, pages):
    pyautogui.click(500, 1070)
    time.sleep(0.2)
    for i in range(pages):
        im = get_page()
        pyautogui.press('right')
        im.save(f'{name}-page{i+1}.png')
        time.sleep(1)
        print(f'saved page {i+1} successfully')

name = 'Arabic-sources' # input('name: ')
pages = 149 # int(input('pages count: '))

save_book(name, pages)
# pyautogui.click(500, 1070)
# time.sleep(0.2)
# get_page().save('screen.png')
