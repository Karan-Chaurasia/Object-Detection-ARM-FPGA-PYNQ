# Real-Time Object Detection using ARM + FPGA on PYNQ-Z2

## Overview

This implements a hardware-accelerated object detection system using:

* YOLOv8m Deep Learning Model
* ARM Cortex-A9 Processor (PS)
* FPGA CNN Accelerator (PL)
* PYNQ-Z2 Board

The system performs real-time object detection using the laptop camera and accelerates convolution operations on FPGA.

## System Architecture

Camera → Python (ARM) → FPGA CNN Accelerator → YOLOv8 Detection → Display Output

## Hardware Used

* PYNQ-Z2 (Zynq-7020 SoC)
* FPGA Accelerator via Vitis HLS
* AXI DMA Communication

## Software Stack

* Python + OpenCV
* Ultralytics YOLOv8m
* Vivado + Vitis HLS
* PYNQ Framework

## Key Features

✔ Hardware-software co-design
✔ Real-time inference
✔ FPGA accelerated CNN
✔ DMA memory transfer
✔ Embedded AI deployment

## How to Run

1. Copy bitstream to PYNQ
2. Run overlay load script
3. Execute camera_inference.py

## Results

The system successfully performs real-time object detection using FPGA acceleration with reduced CPU load.

## Author

B.Tech CSE — Embedded AI & FPGA
