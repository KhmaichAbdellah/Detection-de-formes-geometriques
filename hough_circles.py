import cv2
import numpy as np

def detect_hough_circles(image):
    """
    Détection de cercles avec Hough Circles.
    Méthode : HOUGH_GRADIENT
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)

    circles = cv2.HoughCircles(
        blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,          # résolution accumulatrice
        minDist=30,       # distance min entre cercles
        param1=100,       # seuil Canny haut
        param2=30,        # seuil accumulation Hough
        minRadius=10,
        maxRadius=300
    )

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 2)
            cv2.circle(image, (x, y), 2, (0, 255, 0), 3)

    return image
