
# Forklift and Human Pose Estimation for Safety and Risk Analysis in Industrial Environments

This project focuses on training and evaluating pose recognition models for human and forklift detection in industrial environments. It involves using real and synthetic data to train YOLO-based models, evaluate their performance, and generate synthetic datasets for better generalization. The project includes tools for training, testing, and benchmarking the models, as well as generating annotated 3D scenes in Blender for synthetic data.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Model Training](#model-training)
4. [Benchmarking](#benchmarking)
5. [Synthetic Data Generation](#synthetic-data-generation)

---

## Installation

### Prerequisites
Ensure that you have the following installed:
- Python 3.x
- Blender (for synthetic data generation)
- YOLOv8 (via the `ultralytics` library)

### Steps to Install

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download Blender from https://www.blender.org/ and set it up on your system. Blender is used for generating synthetic data and creating 3D scenes.

---

## Usage

### Training a Model
To train a pose detection model using your dataset:

1. **Prepare your dataset**: Update the paths in `data.yaml` and `data_forklift.yaml` to point to your training data.

2. **Run the training script**:
   ```bash
   python train.py
   ```

   This will train a model using the YOLOv8 architecture and save the trained model in the specified directory.

### Testing the Model
After training, you can test your model using the `test.py` script:
```bash
python test.py
```

This will load the trained model and evaluate its performance on the test set, saving the results for further analysis.

---

## Model Training

### Training Configuration
The training process uses the YOLOv8 framework and allows you to choose different configurations:
- `yolov8m.pt` for medium-sized models (higher accuracy).
- `yolov8n.pt` for smaller, faster models (lower accuracy but better for real-time applications).

You can modify the training parameters in the `train.py` script to set the number of epochs, batch size, and learning rate.

---

## Benchmarking

The **benchmark_multiple_models.py** script is used to evaluate and compare the performance of different models. It logs the benchmark results for various models, including:
- mAP (mean Average Precision)
- Pose mAP
- Keypoint Precision and Recall

### Example Usage:
```bash
python benchmark_multiple_models.py
```

This will run a benchmark for each model and save the results in a CSV file.

---

## Synthetic Data Generation

To improve model generalization, synthetic data is generated using Blender and a custom pipeline. The **automatic_blender_scene.py** script creates a 3D scene with forklifts and background images, generating annotated datasets with various poses and occlusions.

### Running the Script
```bash
python automatic_blender_scene.py
```

This will prepare the Blender scene, including textures, lighting, and poses for both humans and forklifts.


