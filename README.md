# 🖼️ Image to PDF Converter

## 📄 Overview

Image to PDF Converter is a simple Python application that lets you convert image files (PNG, JPG, JPEG, GIF, BMP) to PDF. It features a clean, user-friendly GUI built with Tkinter, and leverages the Pillow (PIL) library for image handling and PDF generation.

---

## ✨ Features

- **Image to PDF Conversion** – Quickly convert image files into PDFs.
- **User-Friendly GUI** – Intuitive interface built with Tkinter.
- **File Selection Dialog** – Easily select image files via a file browser.
- **Robust Error Handling** – Handles invalid selections and displays descriptive error messages.
- **Status Updates** – Get real-time feedback during image selection and conversion.

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (GUI)
- Pillow (PIL)

---

## 🔧 Prerequisites

Ensure you have Python 3 installed and install the Pillow library:

```bash
pip install Pillow
```

## 🚀 How to Use
1. **Clone the Repository**

```bash
git clone https://github.com/AbdullahJaveid/img-to-pdf.git
cd img-to-pdf
```

2. **Run the Script**

Open a terminal and run:

On Windows:
```cmd
python main.py
```
On Mac/Linux:
```bash
python3 main.py
```

3. **Convert Images to PDF**

- Use the Browse button to select an image.

- Click Convert to PDF to begin conversion.

- Upon success, the resulting PDF will open automatically.

## 🔍 Code Breakdown

### 📦 Imports

`tkinter`, `filedialog`, `messagebox` – GUI and file interaction.

os – Open PDF with default system viewer.

PIL (Pillow) – Image manipulation and PDF saving.

🧩 `ImageToPDFConverter` **Class**

`__init__()` – Initializes GUI components.

`select_image()` – Allows image selection and updates path.

`convert()` – Converts selected image to PDF and opens it.

### 🔁 Main Execution

```python
if __name__ == "__main__":
    ImageToPDFConverter()
```

Ensures the application runs only when the script is executed directly.

### 🤝 Contributing
Contributions are welcome!

1. Fork the repository.

2. Create a new branch.

3. Make your changes.

4. Commit and push.

5. Submit a Pull Request.
