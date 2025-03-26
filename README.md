# Autonomous Vehicle System

The system contains object detection and a dialogue chatbox.

## Part 1. Yolo Object Detection

### Set up

1. Create environment using Anaconda
2. Git clone this repo and install necessary packages

```bash
cd yolo7-main
pip install -r requirements.txt 
```

### Dataset

1. Download necessary data and convert into yolov7 format
2. Navigate to the `~\yolov7-main\data` and edit `yolov7.yaml`. Make sure the file paths, number of classes and class name are correct.
3. Navigate to the `~\yolov7-main\cfg\training` and edit `yolov7_voc.yaml`. Make sure the number of classes is correct.

### Training
1. run 
```python
python train.py --workers 4 --device 0 --batch-size 32 --data data/yolov7.yaml --img 640 640 --cfg cfg/training/yolov7_voc.yaml --weights yolov7.pt --name yolov7_output --hyp data/hyp.scratch.custom.yaml
```
‘device’ – 'cpu' or gpu (0,1, etc); ‘name’ indicates the trained output name.\
If there is error, you can try to delete the cache files in the dataset folder.

### Testing
If you wish to run the predictions on a single image/video, just use detect.py, 
and if you want to run the predictions on the complete test dataset, use test.py. \

Again, make sure you are in the ~\yolov7-main directory in the conda 
terminal and enter the command as follows. \

```python
python detect.py --weights best.pt --conf 0.5 --img-size 640 --source <path of the image 
to test>  
```


The output will be available in the `~\yolov7-main\runs\detect\exp\` directory. 


## Part 2. Chatbox
1. Download necessary model in Model file
2. Run Task.py

