# hand-detection-retrain-yolo3
How I use Yolo3 (Tensorflow and Keras implementation) to train a model for hand detection.
# Use TensorFlow and Keras to train Yolo3 for hand detection 
------
## 1. Introduction
- This project documented how I used Yolo3 (Tensorflow and Keras implementation) to train a model for hand detection. Hope this demo can help get your own yolo3 model for your dataset.
- I recorded the implementation based on my understanding, train and test practice, while inspired by many others' work (see references).

## 2. How to run this project
- `git clone https://github.com/zengh100/hand-detection-retrain-yolo3.git`
- Download yolo3.weight from [this](https://pjreddie.com/media/files/yolov3.weights), and put it in the **hand-detection-retrain-yolo3** folder.
- Convert yolov3.cfg and yolov3.weights to a Keras model with TF backend. Before converting, open yolov3.cfg to edit 3 variables: filters, classes, and random in all places within the file.
  * filters = 3x(5+len(classes))
  * classes = len(classes)
  * random = 0
```
python convert.py yolov3.cfg yolov3.weights model_data/yolo_weights.h5
```
- Annotate and label your images: one of the many tools is [LabelImg](https://github.com/tzutalin/labelImg)
- Organize your annotation in file train.txt
```
Row format: image_file_path box1 box2 ... boxN
Box format: x_min,y_min,x_max,y_max,class_id (no space)
```
Here is an example:
```
path/to/image1.jpg 50,100,150,200,0 30,50,200,120,3
path/to/image2.jpg 120,300,250,600,2
```
- `python train.py`
   train.py will read the following files
```
    training data: train.txt
    classes: model_data/voc_classes.txt (each row has a class name)  
    anchors: model_data/yolo_anchors.txt
    keras yolo3 model: model_data/yolo_weights.h5
    log folder: logs/000/
```
## 3. Others:
The above steps can train various Datasets as long as train.txt is orgainzed correctly, the number of classes matches with files *yolo3.cfg and voc_classes.txt*. 

[![Video](video/test-results.gif)]

##Reference

https://github.com/Cw-zero/Retrain-yolo3.git

https://github.com/qqwweee/keras-yolo3
