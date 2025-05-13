# Image to PDF Converter

## Overview

This is a simple Python application that allows you to convert image files (such as PNG, JPG, JPEG, GIF, and BMP) to PDF files. It provides a graphical user interface (GUI) built with Tkinter for easy image selection and conversion. The application uses the Pillow (PIL) library to handle image processing and PDF creation.

## Features

* **Image to PDF Conversion:** Converts image files to PDF format.
* **GUI Interface:** Provides a user-friendly graphical interface for selecting image files and initiating the conversion process.
* **File Selection:** Uses a file dialog to allow users to easily select the image file they want to convert.
* **Error Handling:** Includes error handling to gracefully manage issues such as invalid file selection or conversion failures, displaying informative error messages to the user.
* **Status updates:** Provides feedback to the user on the status of the image selection and conversion process.

## Technologies Used

* Python
* Tkinter (for the GUI)
* Pillow (PIL) (for image processing)

## Prerequisites

* Python 3.x
* Pillow library. You can install it using pip:

    ```bash
    pip install Pillow
    ```

## How to Use

1.  **Clone the repository (Optional):** If you have the code in a Git repository, clone it to your local machine:

    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Run the script:** Open a terminal or command prompt and navigate to the directory where you saved the Python script (e.g., `image_to_pdf.py`). Then, run the script:

    ```bash
    python image_to_pdf.py
    ```

3.  **Select an image:** The application window will appear. Click the "Browse" button to open a file dialog and select the image file you want to convert.

4.  **Convert to PDF:** After selecting an image, the "Convert to PDF" button will become enabled. Click this button to start the conversion.

5.  **View the PDF:** Once the conversion is complete, the application will display a success message, and the generated PDF file will open in your default PDF viewer.  Any errors during the conversion process will be displayed in an error message box.

## Code Explanation

The core functionality of the script is as follows:

* **Imports:**
    * `tkinter`:  Used to create the graphical user interface.
    * `filedialog`:  Used to open the file dialog for selecting image files.
    * `messagebox`: Used to display dialog boxes, such as error or success messages.
    * `os`: Used to open the converted PDF file with the default viewer.
    * `PIL (Pillow)`: Used for opening, processing, and saving the image as a PDF.
* **`ImageToPDFConverter` Class:**
    * `__init__(self)`:
        * Initializes the Tkinter window and sets up the GUI elements (labels, entry, buttons).
        * The "Convert to PDF" button is initially disabled.
        * The `mainloop()` method starts the Tkinter event loop, making the GUI responsive.
    * `select_image(self)`:
        * Opens a file dialog using `filedialog.askopenfilename()` to allow the user to select an image file.
        * Filters for common image file types (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`).
        * Updates the `image_path` StringVar with the selected file path.
        * Enables the "Convert to PDF" button after a valid image is selected.
    * `convert(self)`:
        * Gets the image file path from the `image_path` StringVar.
        * Opens the image using `PIL.Image.open()`.
        * Constructs the PDF file path by changing the file extension.
        * Saves the image as a PDF using `img.save(pdf_path, "PDF")`.
        * Displays a success message using `messagebox.showinfo()`.
        * Opens the generated PDF file using `os.startfile()`.
        * Handles potential errors (e.g., file errors, conversion issues) with a `try...except` block and displays an error message using `messagebox.showerror()`.
* **`if __name__ == "__main__":` Block:**
    * Ensures that the `ImageToPDFConverter` class is instantiated and the application runs only when the script is executed directly (not when imported as a module).

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Commit your changes.
5.  Push to the branch.
6.  Submit a pull request.

## License

No License
