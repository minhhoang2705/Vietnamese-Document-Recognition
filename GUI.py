import tkinter as tk
from tkinter import filedialog
from tools.infer.predict_func import *
from PIL import Image, ImageTk
import cv2


# Define the main application window
class OCRApp:
    def __init__(self, root):
        """
        Initialize the OCR Application GUI.

        Parameters:
        root (tk.Tk): The root window of the application.

        Returns:
        None
        """
        self.root = root
        root.title("OCR Application")
        root.geometry("1920x1000")
        # Set up the GUI layout
        self.frame = tk.Frame(root)
        self.frame.grid(pady=10)

        self.label = tk.Label(self.frame, text="Select an Image to Apply OCR")
        self.label.grid()

        # Create two labels for original and OCR images
        self.original_image = tk.Label(self.frame, text="Original Image", borderwidth=2, relief="groove")
        self.ocr_image = tk.Label(self.frame, text="OCR Image", borderwidth=2, relief="groove")

        # Arrange the labels side by side
        self.original_image.grid(row=1, column=0, padx=10, pady=10)
        self.ocr_image.grid(row=1, column=1, padx=10, pady=10)

        # Create and pack the "Select Image" button
        self.select_button = tk.Button(
            self.frame, text="Select Image", command=self.select_image
        )
        self.select_button.grid(row=2, column=0, pady=10)
        # Create and pack the "Process Image" button
        self.process_button = tk.Button(
            self.frame, text="Process Image", command=self.process_image
        )
        self.process_button.grid(row=2, column=1, pady=10)

    # Open a dialog to select an image
    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.load_and_display_image(self.original_image, file_path)

    def load_and_display_image(self, label, image_path):
        image = Image.open(image_path)
        image = image.resize((500, 500))
        photo = ImageTk.PhotoImage(image)

        label.config(image=photo)
        label.image = photo

        
    def process_image(self):
        if hasattr(self, 'image_path'):
            output_path = './inference_results'
            img = run(self.image_path, output_path)
            self.display_image(self.ocr_image, Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
            tk.messagebox.showinfo("OCR Application", "OCR Completed Successfully!")
        else:
            tk.messagebox.showerror("OCR Application", "Please select an image first!")
            


    def display_image(self,label, image):
        # image = Image.open(image_path)
        image = image.resize((500, 500))
        photo = ImageTk.PhotoImage(image)

        label.config(image=photo)
        label.image = photo

# Main function to run the application
def main():
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
