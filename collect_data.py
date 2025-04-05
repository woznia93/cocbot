# collect_data.py
import os
import time
from PIL import Image
import numpy as np
from capture import grab_screen

# Where to save screenshots
save_dir = "dataset/images/train"
os.makedirs(save_dir, exist_ok=True)

# Number of images to collect
n_images = 50

print("[INFO] Starting screenshot capture...")
for i in range(n_images):
    try:
        frame = grab_screen()  # Capture screen
        if frame is None or frame.shape[0] == 0:
            print(f"[WARNING] Empty screenshot at frame {i}")
            continue

        img = Image.fromarray(frame)
        img.save(f"{save_dir}/img_{i:03}.jpg")
        print(f"[INFO] Saved img_{i:03}.jpg")

        time.sleep(1.5)  # Pause between captures

    except Exception as e:
        print(f"[ERROR] Failed at image {i}: {e}")
