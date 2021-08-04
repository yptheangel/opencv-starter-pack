# OpenCV Cheatsheet

### Common functions
Insert Text
```python
cv2.putText(frame, "Hello OpenCV", (300,400), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=(255, 0, 0), thickness=3)
```

Crop ROI(region of interest of a picture, e.g. output from object detection)
```python
# xmin, ymin is top left point, xmax,ymax is bottom right point of object detection bounding box
roi = YOURCVMAT[ymin:ymax,xmin:xmax]
 
# OR you can set range by your points
roi = YOURCVMAT[y:y+h,x:x+w]
```

Resize Image by fixed output dimension
```python
output = cv2.resize(frame, (600,400))
```

Resize Image by scale 0.5
```python
output = cv2.resize(image, None, fx=0.5, fy=0.5)
```


3. Overlay image on image
```python
output = cv2.addWeighted(src1=foreground, alpha=0.3, src2=background, beta=0.7, gamma=0)
```

4. Make portrait mode using external webcam
```python
rotated = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
```

5. Save image to a file
```python
cv2.imwrite('my_picture.jpg', frame)
```