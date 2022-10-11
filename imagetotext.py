
import cv2
from pytesseract import pytesseract, Output
  
# Defining paths to tesseract.exe
# and the image we would be using
# path_to_tesseract = "/Library/Frameworks/Python.framework/Versions/3.9/bin/pytesseract"
image_path = "https://xkcd.com/s/5bef6b.png"
pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

  
# Opening the image & storing it in an image object
img = cv2.imread(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
# pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])