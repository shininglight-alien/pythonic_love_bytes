import glob
import imagehash
from PIL import Image

my_img_url = r"C:\Users\Ellaine\Downloads\eleyn\ellaine1.jpg"
my_hash = imagehash.average_hash(Image.open(my_img_url))

sheyn = glob.glob('./sheyn/*.jpg')
for file in sheyn:
    try:
        Image.open(file)
        print(f"Successfully opened {file}")
    except FileNotFoundError:
        print(f"Could not open {file}")


eleyn_img = Image.open(my_img_url)
sheyn_img = Image.open(selected)
couple_img = Image.new('RGB', (eleyn_img.width + sheyn_img.width, eleyn_img.height))
couple_img.paste(eleyn_img, (0, 0))
couple_img.paste(sheyn_img, (eleyn_img.width, 0))
couple_img.save('my_valentine_day_date.jpg')
couple_img.show()
