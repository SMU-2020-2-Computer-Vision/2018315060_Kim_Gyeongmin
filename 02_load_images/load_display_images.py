import cv2
import os

# Get the path to the current file
# cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
# os.chdir(cwd)

# Loadd an imdd
# age
img = cv2.imread('apple.jpg')

if img is None:
    print("error")

else:

    # Display the image in a window
    cv2.imshow('image', img)


    # Wait for a key to be pressed
    cv2.waitKey(0)

    # Destroy all windows
    cv2.destroyAllWindows()