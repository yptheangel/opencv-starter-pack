import glob
import os
from datetime import datetime
import cv2

# isResize = False
isResize = True # change this to False, if resize is not required

images = []
image_src_folder = "images"
files = glob.glob(image_src_folder+"/*")

for file in files:
    print(f"Processing: {os.path.basename(file)}")
    if file.endswith(".jpg") or file.endswith(".png"):
        image = cv2.imread(file)
        print(f"original image dimension: {image.shape}") # image shape is displayed as height,width, channel
        if isResize:
            resize_scale = 0.45
            image = cv2.resize(image, None, fx=resize_scale, fy=resize_scale, interpolation=cv2.INTER_AREA) # resize by scale
            # image = cv2.resize(image, (640,480), interpolation=cv2.INTER_AREA) # resize by fixed output dimension
        print(f"new image dimension: {image.shape}")
        images.append(image)

# if your stitch don't go well, try the STITCHER_SCANS
stitcher = cv2.Stitcher.create(mode=cv2.STITCHER_PANORAMA)
# stitcher = cv2.Stitcher.create(mode=cv2.STITCHER_SCANS)
ret, stitched = stitcher.stitch(images)

if ret == cv2.STITCHER_OK:

    output_fn = f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'

    cv2.imshow('Panorama', stitched)
    cv2.imwrite(output_fn, stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error during Stitching")
