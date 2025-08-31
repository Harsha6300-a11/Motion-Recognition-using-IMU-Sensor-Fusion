This project implements a **real-time gesture recognition system** using an **Inertial Measurement Unit (IMU)** on a **Raspberry Pi 4 with Sense HAT**. It leverages accelerometer and gyroscope data to classify gestures with a lightweight **TensorFlow Lite** model, enabling efficient deployment on embedded devices.

## Features

* Data Collection – Captured IMU readings (accelerometer + gyroscope) at 50 Hz, stored with NumPy.
* Model Training – Built and trained a **Feedforward Neural Network** in TensorFlow on Google Colab.
* Edge Deployment – Converted trained model to **TensorFlow Lite** for on-device inference.
* Real-Time Prediction – Integrated live classification with Sense HAT LED matrix feedback.
* Extendable – Can be upgraded with LSTM/CNN models for sequential gesture recognition.

## Tech Stack

* **Hardware**: Raspberry Pi 4, Sense HAT (IMU: accelerometer, gyroscope)
* **Languages**: Python
* **Libraries**: TensorFlow, TensorFlow Lite, NumPy
* **Tools**: Google Colab, SSH/SCP

## Gestures Classified

* Circle
* Shake
* Twist
* None

## Results

* Successfully deployed a **gesture recognition model** on Raspberry Pi.
* Achieved real-time predictions with minimal latency.

## Future Improvements

* Add wireless feedback/alerts via MQTT or ROS 2.
* Extend model to support complex multi-step gestures.
* Integrate with autonomous robot control for gesture-based navigation.

---
