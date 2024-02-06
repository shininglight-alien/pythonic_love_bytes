import glob
import imagehash
from PIL import Image

my_img_url = r"C:\Users\Ellaine\Downloads\eleyn\ellaine1.jpg"
my_hash = imagehash.average_hash(Image.open(my_img_url))

sheyn = glob.glob('./sheyn/*.jpg')
selected = r"C:\Users\Ellaine\Downloads\sheyn"[0]
accepted_diff = 1000
for img in sheyn:
    img_hash = imagehash.average_hash(Image.open(img))
    diff = img_hash - my_hash
    if diff < accepted_diff:
        selected = img
        accepted_diff = diff

eleyn_img = Image.open(my_img_url)
sheyn_img = Image.open(selected)
couple_img = Image.new('RGB', (eleyn_img.width + sheyn_img.width, eleyn_img.height))
couple_img.paste(eleyn_img, (0, 0))
couple_img.paste(sheyn_img, (eleyn_img.width, 0))
couple_img.save('my_valentine_day_date.jpg')
couple_img.show()
