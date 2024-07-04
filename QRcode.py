import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        master.geometry("500x500")

        # Set the font style to Montserrat
        font_style = "Montserrat"

        # Create a label for the input text
        self.label = tk.Label(master, text="Enter text or link:", font=(font_style, 14))
        self.label.pack()

        # Create an entry widget for the input text
        self.text_entry = tk.Entry(master, font=(font_style, 12))
        self.text_entry.pack()

        # Create a button to generate the QR code
        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code, font=(font_style, 12))
        self.generate_button.pack()

        # Set the background color to "#2C3E50"
        master.configure(background="#2C3E50")

        # Create a label to display the generated QR code
        self.qr_code_label = tk.Label(master, bg="#2C3E50")
        self.qr_code_label.pack()

        # Create a button to print the generated QR code
        self.print_button = tk.Button(master, text="Print QR Code", command=self.print_qr_code, font=(font_style, 12))
        self.print_button.pack()

    def generate_qr_code(self):
        # Get the text from the input entry
        text = self.text_entry.get()

        # Generate the QR code image
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert the image to a format that can be displayed in tkinter
        img = ImageTk.PhotoImage(img)

        # Update the label to display the generated QR code
        self.qr_code_label.configure(image=img)
        self.qr_code_label.image = img

    def print_qr_code(self):
        # Get the generated QR code image
        img = self.qr_code_label.image

        # Convert the PhotoImage to an Image object
        pil_img = ImageTk.getimage(img)

        # Prompt the user to select a location to save the image
        file_path = filedialog.asksaveasfilename(defaultextension=".png")

        # Save the image to the selected location
        pil_img.save(file_path)


root = tk.Tk()
qrcode_generator = QRCodeGenerator(root)
root.mainloop()
