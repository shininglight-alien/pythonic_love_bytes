import glob
import imagehash
import tkinter as tk
from PIL import Image, ImageTk

# create a popup window with the Valentine's Day message
def show_message():
    popup = tk.Toplevel(root)
    popup.title("Valentine's Day Surprise!")
    message = "Here's your Valentine's Day date! His name is Shane Jay."
    label = tk.Label(popup, text=message, font=("Arial", 24), wraplength=300)
    label.pack(pady=50)
    button = tk.Button(popup, text="OK", font=("Arial", 18), command=popup.destroy)
    button.pack(pady=20)
    popup.grab_set()

# loading images
def show_main_window():
    my_img_url = r"C:\Users\Ellaine\Downloads\eleyn\ellaine1.jpg"
    my_hash = imagehash.average_hash(Image.open(my_img_url))

# sheyn's images
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

# selecting sheyn's images
        eleyn_img = Image.open(my_img_url)
        sheyn_img = Image.open(selected)

# resizing images to fit the screen
        laptop_screen_width = 1366
        laptop_screen_height = 768
        
# dimensions based on aspect ratio
        aspect_ratio_eleyn = eleyn_img.width / eleyn_img.height
        aspect_ratio_sheyn = sheyn_img.width / sheyn_img.height

        if eleyn_img.height > sheyn_img.height:
            new_height = int(laptop_screen_height * 0.9)
            new_width = int(new_height * aspect_ratio_eleyn)
        else:
            new_height = int(laptop_screen_height * 0.9)
            new_width = int(new_height * aspect_ratio_sheyn)

        eleyn_img = eleyn_img.resize((new_width, new_height))
        sheyn_img = sheyn_img.resize((new_width, new_height))

# displaying images
        max_width = max(eleyn_img.width, sheyn_img.width)
        max_height = max(eleyn_img.height, sheyn_img.height)

        couple_img = Image.new('RGB', (max_width, max_height))

        couple_img.paste(eleyn_img, (0, 0))
        couple_img.paste(sheyn_img, (0, max_height - sheyn_img.height))

# convert the final couple image to a Tkinter-compatible photo image
        couple_img_tk = ImageTk.PhotoImage(couple_img)

# create a new Tkinter window and display the final couple image
        root.deiconify()  # Show the main window
        root.title("My Valentine's Day Date")
        label = tk.Label(root, image=couple_img_tk)
        label.pack(fill=tk.BOTH, expand=True)

# run the Tkinter mainloop
        root.mainloop()

    else:
        print("No .jpg files found in the ./sheyn/ directory.")

root = tk.Tk()
root.withdraw()

# display the pop-up message
show_message()

# show the main window
show_main_window()