import tkinter as tk
from tkinter import ttk
import os
from masking import mask_image
import time
import subprocess


class Application(tk.Frame):
    def __init__(self,
                 master=None,
                 input_masking_path="../SinGAN_antyang/Input/Images",
                 input_training_path="../SinGAN_antyang/Input/Images",
                 output_mask_path="../SinGAN_antyang/Input/Inpainting",
                 input_model_path="../SinGAN_antyang/TrainedModels"
                 ):
        super().__init__(master)
        self.master = master
        self.input_masking_path = input_masking_path
        self.output_mask_path = output_mask_path
        self.input_training_path = input_training_path
        self.input_model_path = input_model_path
        # masking
        self.input_masking_option_list = os.listdir(input_masking_path)
        self.picked_input_masking = tk.StringVar(
            self)
        self.picked_input_masking.set(self.input_masking_option_list[0])

        # training
        self.input_training_option_list = os.listdir(input_training_path)
        self.picked_input_training = tk.StringVar(
            self)
        self.picked_input_training.set(self.input_training_option_list[0])

        # inpainting
        self.picked_input_inpainting = tk.StringVar(
            self)
        self.picked_input_inpainting.set(self.input_masking_option_list[0])

        self.input_inpainting_models_option_list = os.listdir(input_model_path)
        self.picked_input_inpainting_model = tk.StringVar(
            self)
        self.picked_input_inpainting_model.set(
            self.input_inpainting_models_option_list[0])

        self.pack()
        self.create_widgets()

    def run_train(self):
        p = subprocess.Popen(
            f"python3 main_train.py --inpainting --input_name {self.picked_input_training.get()}", shell=True)
        self.pb.start()
        while p.poll() is None:
            self.pb.update()
        self.pb.stop()

    def run_mask_image(self):
        mask_image(
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

        # training
        self.input_training_label = tk.Label(
            self, text="Training", font=('Helvetica', 20))
        self.input_training_label.pack(side="top")

        self.input_training_dropdown = tk.OptionMenu(
            self,
            self.picked_input_training,
            *self.input_training_option_list)
        self.input_training_dropdown.config(width=90, font=('Helvetica', 12))
        self.input_training_dropdown.pack(side="top")

        self.training_button = tk.Button(self)
        self.training_button["text"] = "Train"
        self.training_button["command"] = self.run_train
        self.training_button.pack(side="top")

        self.pb = ttk.Progressbar(self, mode="indeterminate")
        self.pb.pack(side="top")

        # inpainting
        self.input_inpainting_label = tk.Label(
            self, text="Inpainting", font=('Helvetica', 20))
        self.input_inpainting_label.pack(side="top")

        #   input
        self.input_inpainting_dropdown = tk.OptionMenu(
            self,
            self.picked_input_inpainting,
            *self.input_masking_option_list)
        self.input_inpainting_dropdown.config(width=90, font=('Helvetica', 12))
        self.input_inpainting_dropdown.pack(side="top")

        #   model
        self.input_inpainting_dropdown = tk.OptionMenu(
            self,
            self.picked_input_inpainting_model,
            *self.input_inpainting_models_option_list)
        self.input_inpainting_dropdown.config(width=90, font=('Helvetica', 12))
        self.input_inpainting_dropdown.pack(side="top")

        self.inpainting_button = tk.Button(self)
        self.inpainting_button["text"] = "Inpaint"
        self.inpainting_button["command"] = lambda: print("inpaint")
        self.inpainting_button.pack(side="top")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
