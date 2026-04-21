import numpy as np
from PIL import Image
img = Image.open("new.jpeg").convert("RGB")
arr = np.array(img)
print(arr.shape)
print(arr[0][0])
gray = np.mean(arr, axis = 2)
Image.fromarray(gray.astype(np.uint8)).save("gray.jpeg")
neg = 255-arr
Image.fromarray(neg).save("neg.jpeg")

img = Image.open('new.jpeg').convert("L")
arr = np.array(img)
char = " .:-=+*#%@"
height,width = arr.shape
new_width = 100
new_height = int(height * new_width / width * 0.5)
img = img.resize((new_width,new_height))
arr = np.array(img)
ascii_img = ""
for row in arr:
    for pixel in row:
        index = int(pixel) * len(char) // 256
        ascii_img += char[index]
    ascii_img += "\n"


with open("ascii_art.txt", "w") as f:
    f.write(ascii_img)








