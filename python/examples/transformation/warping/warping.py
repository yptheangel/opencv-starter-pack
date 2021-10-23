import cv2
import numpy as np

# read your picture and store into variable "frame"
frame = cv2.imread('picture.jpg')

# selecting points for transformation. make sure these numbers falls under the dimensions of your image.
p1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
p2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]]) 

# generating transformation matrix
matrix = cv2.getPerspectiveTransform(p1, p2) 
# getting final results
result = cv2.warpPerspective(frame, matrix, (500, 600))

# Example 2: Create a triangle warp
warp_triangle = 255 * np.ones(frame.shape, dtype = frame.dtype)
tri1 = np.float32([[[360,200], [60,250], [450,400]]])
tri2 = np.float32([[[400,200], [160,270], [400,400]]])

# Find bounding box
r1 = cv2.boundingRect(tri1) 
r2 = cv2.boundingRect(tri2)

# Offset points by left top corner of the respective rectangles
tri1_cropped = []
tri2_cropped = []
    
for i in range(0, 3):
    tri1_cropped.append(((tri1[0][i][0] - r1[0]),(tri1[0][i][1] - r1[1])))
    tri2_cropped.append(((tri2[0][i][0] - r2[0]),(tri2[0][i][1] - r2[1])))

# Crop input image
input_cropped = frame[r1[1]:r1[1] + r1[3], r1[0]:r1[0] + r1[2]]

# Given a pair of triangles, find the affine transform.
warp_mat = cv2.getAffineTransform(np.float32(tri1_cropped), np.float32(tri2_cropped) )

# Apply the Affine Transform just found to the src image
warp_triangle_cropped = cv2.warpAffine( input_cropped, warp_mat, (r2[2], r2[3]), None, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101 )

# Get mask by filling triangle
mask = np.zeros((r2[3], r2[2], 3), dtype = np.float32)
cv2.fillConvexPoly(mask, np.int32(tri2_cropped), (1.0, 1.0, 1.0), 16, 0);

warp_triangle_cropped = warp_triangle_cropped * mask
    
# Copy triangular region of the rectangular patch to the output image
warp_triangle[r2[1]:r2[1]+r2[3], r2[0]:r2[0]+r2[2]] = warp_triangle[r2[1]:r2[1]+r2[3], r2[0]:r2[0]+r2[2]] * ( (1.0, 1.0, 1.0) - mask )
warp_triangle[r2[1]:r2[1]+r2[3], r2[0]:r2[0]+r2[2]] = warp_triangle[r2[1]:r2[1]+r2[3], r2[0]:r2[0]+r2[2]] + warp_triangle_cropped

# displaying original and transformed image
cv2.imshow('Original', frame)
cv2.imshow('Warped', result)
cv2.imshow('Warped Triangle', warp_triangle)

# waiting for a key to be pressed
cv2.waitKey(0)
# destroying all windows
cv2.destroyAllWindows() 