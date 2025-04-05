# cocbot

## ML-Based Clash of Clans Bot

A Python-powered automation and machine learning project designed to interact with **Clash of Clans**. The bot captures screen data, detects game elements using YOLOv5, decides what action to take, and automates gameplay using tools like `pyautogui`.

---

## Features
- Screen capturing using `mss`
- Object detection using YOLOv5 (gold mines, elixir collectors, etc.)
- Smart action decision logic (collect, train, deploy)
- Automated game interaction (mouse clicking)
- Extensible for reinforcement learning and battle strategy

---

## How it Works
1. Captures emulator screen
2. Detects objects with YOLOv5
3. Decides actions with simple logic (can be replaced with ML policies)
4. Executes clicks using `pyautogui`

---

## Getting Started

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Capture Training Images (Optional)
```bash
python collect_data.py
```
Or manually use Snipping Tool to take screenshots into `dataset/images/train`

### 3. Label Your Dataset
- Use [LabelImg](https://github.com/heartexlabs/labelImg) or [Label Studio](https://labelstud.io/)
- Save annotations in YOLO format to `dataset/labels/train/`

### 4. Train YOLOv5
Clone YOLOv5:
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```
Train:
```bash
python train.py --img 640 --batch 16 --epochs 50 --data ../data.yaml --weights yolov5s.pt
```

### 5. Run the Bot
```bash
python main.py
```

---

## 🛠 Technologies Used
- Python
- PyTorch / YOLOv5
- OpenCV, PIL, NumPy
- pyautogui (automation)
- mss (screen capture)

---

## Future Improvements
- Reinforcement learning with Stable-Baselines3
- Smarter troop deployment logic
- Real-time base layout adaptation

---

## Disclaimer
This project is for **educational purposes only**. Do not use it on your main Clash of Clans account. Automation may violate the game’s terms of service and lead to account bans.

---

## Preview
_(Add GIF or screenshot of bot in action here)_

