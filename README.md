# hand-detection-retrain-yolo3
How I use Yolo3 (Tensorflow and Keras implementation) to train a model for hand detection.
# Use TensorFlow and Keras to train Yolo3 for hand detection 
------
## 1. Introduction
- This project documented how I used Yolo3 (Tensorflow and Keras implementation) to train a model for hand detection. So if you are interested, this demo can gelp you get your own yolo3 model for your dataset.
- I recorded the implementation process based on my understanding while inspired many others' work (see references).

## 2. How to run this project
- a. `git clone https://github.com/zengh100/hand-detection-retrain-yolo3.git`
- b. Download yolo3.weight from [this](https://pjreddie.com/media/files/yolov3.weights), and put it in the **hand-detection-retrain-yolo3** folder.
- c. `python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5`
- d. Prepare your Dataset
```
1.New several folders in VOC2007 folder, the final structure like that:

VOC2007
├── Annotations
├── ImageSets
|   ├── Layout
|   ├── Main
|   ├── Segmentation
├── JPEGImages
├── SegmentationClass
├── SegmentationObject
└── test.py

2.Copy your all images to JPEGImages
```
- e.Use [LabelImg](https://github.com/tzutalin/labelImg) to annotate and label your images,and the outputs saved in  **Annotations** folder.
- d.cd to VOC2007, `python test.py`
- e.cd to Retrain-yolo3, `python voc_annotation.py`
- f.cd to Retrain-yolo3, `python train.py`

## 3. Others:
The above steps can only train VOC Dataset, if you want to change the number of classes, you also need to modify *voc_annotation.py, yolo3.cfg and voc_classes.txt*. I will update this part on blog and here as soon as possible.

Reference

https://github.com/Cw-zero/Retrain-yolo3.git

https://github.com/qqwweee/keras-yolo3
