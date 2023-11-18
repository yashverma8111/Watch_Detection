# Watch Detection Project

## Overview

This project focuses on real-time watch detection using the YOLO (You Only Look Once) algorithm, implemented with the Ultralytics library. The detection model is trained on a custom dataset containing images of watches.

## Project Structure

The project directory structure is organized as follows:

📁 custom_detection
│
├── configurations.yaml
├── main.py
├── detect.py
│
└── 📁 images
├── 🖼️ Train Images
└── 🖼️ Validation Images

**`configurations.yaml`**: Configuration file specifying the dataset paths, class names, and other training parameters.
- **`main.py`**: Python script for real-time watch detection using the pre-trained YOLO model.
- **`detect.py`**: Python script for detecting watches in live webcam footage.
- **`images`**: Directory containing training and validation images.

## Customization

Adjust training parameters in configurations.yaml for custom datasets and training configurations.
Modify class names and IDs in configurations.yaml to match the classes in your dataset.
