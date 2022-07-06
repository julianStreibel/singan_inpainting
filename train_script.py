import subprocess


input_names = [
    "image_0007_small_edit.png",
    "image_0004_small_edit.png",
    "image_0006_small_edit.png",
    "image_0015_small_edit.png",
    "image_0011_small_edit.png"
]

# train models
for input_name in input_names:
    p = subprocess.Popen(
        f"python3 main_train.py --inpainting --input_name {input_name}",
        shell=True
    )
    p.wait()

print("done")
