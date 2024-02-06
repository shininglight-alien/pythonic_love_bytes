import glob
import imagehash
from PIL import Image

my_img_url = r"C:\Users\Ellaine\Downloads\eleyn\ellaine1.jpg"
my_hash = imagehash.average_hash(Image.open(my_img_url))

# list of all picture files in sheyn
sheyn_imgfiles = glob.glob(r"C:\Users\Ellaine\Downloads\sheyn\*")

if r"C:\Users\Ellaine\Downloads\sheyn":
    selected = sheyn_imgfiles[0]
    accepted_diff = 1000
    for img in sheyn_img_files:
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
else:
    print("No .jpg files found in the ./sheyn/ directory.")
