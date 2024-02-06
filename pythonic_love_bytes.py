import glob
import imagehash
from PIL import Image

my_img_url = r"C:\Users\Ellaine\Downloads\eleyn\ellaine1.jpg"
my_hash = imagehash.average_hash(Image.open(my_img_url))

# Get a list of all .jpg files in the ./sheyn/ directory
sheyn_img_files = glob.glob(r"C:\Users\Ellaine\Downloads\sheyn\*.jpg")

if sheyn_img_files:
    selected = sheyn_img_files[0]
    accepted_diff = 1000
    for img in sheyn_img_files:
        img_hash = imagehash.average_hash(Image.open(img))
        diff = img_hash - my_hash
        if diff < accepted_diff:
            selected = img
            accepted_diff = diff
            
    eleyn_img = Image.open(my_img_url)
    sheyn_img = Image.open(selected)
    
    max_width = max(eleyn_img.width, sheyn_img.width)
    max_height = max(eleyn_img.height, sheyn_img.height)
    
    couple_img = Image.new('RGB', (max_width, max_height))
    
    couple_img.paste(eleyn_img, (0, 0))
    couple_img.paste(sheyn_img, (0, max_height - sheyn_img.height))
    
    couple_img.save('my_valentine_day_date.jpg')
    couple_img.show()
    
    print("No .jpg files found in the ./sheyn/ directory.")