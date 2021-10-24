example contributed by `harshgtm01`

# Edge Detection using Canny edge detector
An edge detector accepts discrete, digitized images as input and produces an edge map as output. The edge map of some detectors includes explicit information about the position and strength of edges, their orientation, and the scale.  
Changing the threshold values in the code can improve the resulting edge detected image.

### Requirements:
```python
pip install opencv-python
pip install matplotlib
```

### Running edge_detector.py
Provide the path of the image you want to use edge detection on and run the code. The threshold values required for different images can be different so changing the threshold values in the code can improve the resulting edge detected image for a given image.

### Running live_edge_detector.py
Instead of providing an image, it detects edges of a video. In the `VideoCapture()` function either provide the path to the file or use camera to detect live feed. 
Press q to stop the program.

Video are nothing but continous frames, it reads continuous frames apply edge detection on them and return continous edge detected frames


