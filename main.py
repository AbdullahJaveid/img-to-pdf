import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image  # Import the Pillow library


class ImageToPDFConverter:
    """
    A simple GUI application to convert image files (like PNG, JPG) to PDF.
    It uses the Pillow library for image processing and directly saves to a PDF.
    """

    def __init__(self):
        """
        Initializes the main application window (Tkinter).
        Sets up the GUI elements: labels, entry fields, and buttons.
        """
        self.root = tk.Tk()
        self.root.title("Image to PDF Converter")
        # Set initial window size for better usability
        self.root.geometry("400x200")

        # Label for selecting image
        self.label = tk.Label(self.root, text="Select an image file:")
        self.label.pack(pady=10)  # Add padding for better spacing

        # Entry field to display the image path
        self.image_path = tk.StringVar()
        self.entry = tk.Entry(
            self.root, textvariable=self.image_path, width=30)
        self.entry.pack(pady=5)

        # Button to select the image file
        self.select_button = tk.Button(
            self.root, text="Browse", command=self.select_image
        )
        self.select_button.pack(pady=5)

        # Button to start the conversion
        self.convert_button = tk.Button(
            # Disable until image is selected
            self.root, text="Convert to PDF", command=self.convert, state=tk.DISABLED
        )
        self.convert_button.pack(pady=10)

        # Status Label for displaying messages
        # Initialize with empty text and gray color
        self.status_label = tk.Label(self.root, text="", fg="gray")
        self.status_label.pack(pady=5)

        self.root.mainloop()  # Start the Tkinter event loop

    def select_image(self):
        """
        Opens a file dialog to select an image file.
        Updates the entry field with the selected path.
        Enables the convert button if a valid image is selected.
        """
        filetypes = [("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"),
                     ("All files", "*.*")]  # Added more image types
        image_path = filedialog.askopenfilename(
            title="Select Image File", filetypes=filetypes
        )
        self.image_path.set(image_path)  # Update the entry field
        if image_path:  # Check if a file was actually selected
            # Enable the convert button
            self.convert_button["state"] = tk.NORMAL
            self.status_label.config(
                text="Image selected", fg="green")  # update status
        else:
            self.status_label.config(text="No image selected", fg="red")

    def convert(self):
        """
        Converts the selected image to a PDF file using Pillow.
        Displays a success/error message using messagebox.
        Opens the converted PDF file using the default viewer.
        """
        image_path = self.image_path.get()
        if not image_path:
            messagebox.showerror("Error", "Please select an image file first.")
            self.status_label.config(text="Error: No image selected", fg="red")
            return

        try:
            # Use Pillow to open the image
            img = Image.open(image_path)
            # Construct the PDF file path
            pdf_path = os.path.splitext(image_path)[0] + ".pdf"
            # Save the image as a PDF
            img.save(pdf_path, "PDF")

            messagebox.showinfo("Success", f"Image converted to {pdf_path}")
            self.status_label.config(text="Conversion successful", fg="green")
            os.startfile(pdf_path)  # Open the PDF
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")
            self.status_label.config(text=f"Error: {e}", fg="red")


if __name__ == "__main__":
    # Create an instance of the converter and start the GUI
    converter = ImageToPDFConverter()
