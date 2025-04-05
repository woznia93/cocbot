# capture.py
import mss
import numpy as np
from PIL import Image

def grab_screen(region=None):
    with mss.mss() as sct:
        monitor = sct.monitors[1] if not region else region
        screenshot = sct.grab(monitor)
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        return np.array(img)

