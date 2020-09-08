import cv2

# This example overlays a green box which is 50% transparent on the background image
background = cv2.imread('picture.jpg')
foreground = background.copy()
print(f"Height X Width: {background.shape[:2]}")

# topleft point consists of xmin = origin 0 ,ymin is 80% of ymax
# bottomright point is xmax,ymax
topleft_point = (0, int(background.shape[0] * 0.8))
bottomright_point = (background.shape[1], background.shape[0])

foreground = cv2.rectangle(foreground, topleft_point, bottomright_point, (0, 255, 0), -1)
output = cv2.addWeighted(src1=foreground, alpha=0.3, src2=background, beta=0.7, gamma=0)

cv2.imshow('Hello World!', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
