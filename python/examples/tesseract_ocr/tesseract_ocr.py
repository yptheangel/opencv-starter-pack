import pytesseract
import cv2

if __name__ == "__main__":
    # Reading the image.
    image = cv2.imread("picture.png")
    
    # Converting image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Thresholding the image to reduce noise.
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    # Extracting text from image using tesseract and printing results to console.
    print(pytesseract.image_to_string(gray))