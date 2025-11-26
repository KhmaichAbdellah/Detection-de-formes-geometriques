import cv2
import numpy as np

def detect_hough_lines(image):
    """
    Détection de lignes avec la transformée de Hough.
    Méthode utilisée : HoughLinesP (probabiliste)
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 1) Réduction du bruit
    blur = cv2.GaussianBlur(gray, (5, 5), 1.5)

    # 2) Détection des contours
    edges = cv2.Canny(blur, 30, 120)

    # 3) Transformée de Hough Probabiliste
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi/180,
        threshold=50,
        minLineLength=20,
        maxLineGap=20
    )

    # 4) Dessin des lignes détectées
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return image
