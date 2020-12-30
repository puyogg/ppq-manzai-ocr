# %%
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
# %%
# Get image paths
images = glob.glob('./manzais/chapter1/*.jpg')
print(images)

# %%
def scrape_message(filename: str) -> str:
    im = cv2.imread(filename)
    # plt.imshow(im[1250:2000, :])
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = (im < 30) * 255
    im = im[1250:2000, :].astype(np.uint8)

    im_pil = Image.fromarray(im.astype(np.uint8))
    plt.imshow(im_pil, cmap='gray')
    text = pytesseract.image_to_string(im_pil, lang='jpn')
    return text.strip()

text = scrape_message(images[1])
print(text)

# %%
def scrape_header(filename: str) -> str:
    im = cv2.imread(filename)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = (im > 180) * 255
    im = im[1315:1405].astype(np.uint8)
    for i in range(100, 500):
        cv2.floodFill(im, None, (i, 89), 0)
    im_pil = Image.fromarray(im.astype(np.uint8))
    plt.imshow(im_pil, cmap='gray')
    text = pytesseract.image_to_string(im_pil, lang='jpn')
    # text = text.replace('タッチしてすすむ', '')
    return text.strip()

text = scrape_header(images[1])
print(text)

# %%
