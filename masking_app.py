import tkinter as tk
import os
from masking import Mask_Operator
import subprocess


class Application(tk.Frame):
    def __init__(self,
                 master=None,
                 input_masking_path="input/images",
                 input_training_path="input/images",
                 output_mask_path="input/editing",
                 input_model_path="models"
                 ):
        super().__init__(master)
        self.master = master
        self.master.title("Masking App")
        self.input_masking_path = input_masking_path
        self.output_mask_path = output_mask_path
        self.input_training_path = input_training_path
        self.input_model_path = input_model_path
        # masking
        self.input_masking_option_list = os.listdir(input_masking_path)
        self.picked_input_masking = tk.StringVar(
            self)
        self.picked_input_masking.set(self.input_masking_option_list[0])

        self.pack()
        self.create_widgets()

    def run_mask_image(self):
        Mask_Operator(
            self.input_masking_path,
            self.output_mask_path,
            self.picked_input_masking.get())
        self.input_masking_option_list = os.listdir(self.input_masking_path)
        self.input_training_option_list = os.listdir(self.input_training_path)
        self.input_inpainting_models_option_list = os.listdir(
            self.input_model_path)

    def create_widgets(self):

        # masking
        self.input_masking_label = tk.Label(
            self, text="Masking", font=('Helvetica', 20))
        self.input_masking_label.pack(side="top")

        self.input_masking_dropdown = tk.OptionMenu(
            self,
            self.picked_input_masking,
            *self.input_masking_option_list)
        self.input_masking_dropdown.config(width=90, font=('Helvetica', 12))
        self.input_masking_dropdown.pack(side="top")

        self.create_mask_button = tk.Button(self)
        self.create_mask_button["text"] = "Create Mask"
        self.create_mask_button["command"] = self.run_mask_image
        self.create_mask_button.pack(side="top")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
