
# Poster
![dgm_poster](https://user-images.githubusercontent.com/17069602/177596909-06033766-c56b-463f-a311-24fa39cf90be.jpg)

# Masking
This video shows the creation of the loss mask and the masked image to inject. The local mean color is used for the image mask to create better performance when injecting the image on higher scales. This process can be seen as editing or paint-to-image task. The created loss mask has the same shape as the image mask.



https://user-images.githubusercontent.com/17069602/177621021-fd269e01-088d-47df-8cfe-07ffa451ac7e.mp4




# Inpainting with SinGAN
The SinGAN can be trained on the original image with the masked loss and partial convolution to ignore the unwanted structures. Afterwards the downsampled version of the masked image can be injected into an higher scale generator to start the generation process.



https://user-images.githubusercontent.com/17069602/177617641-44e446e8-5a35-4361-a8ad-aa35f7189efa.mp4



![singan](https://user-images.githubusercontent.com/17069602/177598485-8849222d-efc5-491c-9c4c-7d47b280694d.png)


# Getting Started

```
# install
pip install -r requirements.txt

# masking
python3 masking_app.py

# train models for the five images on the poster
python3 train_script.py

# sample images by injecting the masked image in different scales
python3 paint2image_script.py
```
---

This project is highly inspired by - and uses code from https://github.com/tamarott/SinGAN, https://github.com/antoyang/SinGAN and https://github.com/NVIDIA/partialconv.
