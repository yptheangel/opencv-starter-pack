# example by "harshgtm01"

import cv2
import matplotlib.pyplot as plt

# read the image
image = cv2.imread(r'../../../../../assets/original.jpg')

# convert it to grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Using canny edge detector to detect image edges
edges = cv2.Canny(gray, 30, 100)        # changing the threshold values to get better result for your frames
                                        # The smallest value between threshold1 and threshold2 is used for edge linking.
                                        # The largest value is used to find initial segments of strong edges.

# show the detected edges
plt.imshow(edges, cmap="gray")
plt.show()
