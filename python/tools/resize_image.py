import cv2

# Specify your desired resize scale factor
# e.g. If you want to resize your image to 50% smaller, scale = 0.5,
# e.g  Else if you want to resize to 50% bigger, scale = 1.5
scale = 0.15

IMAGE_NAME = "IMG_20181011_073044.jpg"
OUTPUT_NAME = IMAGE_NAME[:-4] + "_resized.jpg"

frame = cv2.imread(IMAGE_NAME)
height, width, channels = frame.shape
print("Frame height: {0}".format(height))
print("Frame weight: {0}".format(width))
print("Number of channels of image: {0}".format(channels))

output_width = int(scale * float(width))
output_height = int(scale * float(height))

output_size = (output_width, output_height)

# Hard code your desired output iamge size
# output_size=(200,600)

output = cv2.resize(frame, output_size)
cv2.imwrite(OUTPUT_NAME, output)

cv2.waitKey(0)
cv2.destroyAllWindows()
