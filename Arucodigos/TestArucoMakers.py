import cv2

# Load the predefined dictionary for Aruco markers
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Load the input image and resize it to 600x600 pixels
img = cv2.imread("arucodigos.jpg")

if img is None:
    raise Exception("Could not read the input image.")


rezize = cv2.resize(img, (600, 600))

# Convert the image to grayscale
gray = cv2.cvtColor(rezize, cv2.COLOR_BGR2GRAY)

# Create the Aruco detector with default parameters
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

# Detect the Aruco markers in the image
corners, ids, rejected_candidates = detector.detectMarkers(gray)

# Draw the detected markers on the output image
output = rezize.copy()
cv2.aruco.drawDetectedMarkers(output, corners, ids)

# Save the output image
cv2.imwrite("outputaruco.jpg", output)