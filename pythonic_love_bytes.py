import glob
import imagehash
import tkinter as tk
from PIL import Image, ImageTk

def show_message():
    popup = tk.Toplevel(root)
    popup.title("Valentine's Day Surprise!")
    message = "Ta-da! Here's your Valentine's Day date!"
    label = tk.Label(popup, text=message, font=("Arial", 24), wraplength=300)
    label.pack(pady=50)
    button = tk.Button(popup, text="OK", font=("Arial", 18), command=popup.destroy)
    button.pack(pady=20)
    popup.grab_set()

def show_main_window():
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

        # Convert the final couple image to a Tkinter-compatible photo image
        couple_img_tk = ImageTk.PhotoImage(couple_img)

        # Create a new Tkinter window and display the final couple image
        root.deiconify()  # Show the main window
        root.title("My Valentine's Day Date")
        label = tk.Label(root, image=couple_img_tk)
        label.pack(fill=tk.BOTH, expand=True)

        # Run the Tkinter mainloop
        root.mainloop()

    else:
        print("No .jpg files found in the ./sheyn/ directory.")

root = tk.Tk()
root.withdraw()

# Display the pop-up message
show_message()

# Show the main window
show_main_window()