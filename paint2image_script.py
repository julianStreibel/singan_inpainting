import subprocess


input_names = [
    "image_0007_small_edit.png",
    "image_0004_small_edit.png",
    "image_0006_small_edit.png",
    "image_0015_small_edit.png",
    "image_0011_small_edit.png"
]


# predict on every scale
for input_name in input_names:
    for scale in range(1, 10):
        p = subprocess.Popen(
            f"python3 paint2image.py --input_name {input_name} --ref_dir Input/Images --ref_name {input_name} --paint_start_scale {scale}", # --quantization_flag
            shell=True
        )
        p.wait()

print("done")
