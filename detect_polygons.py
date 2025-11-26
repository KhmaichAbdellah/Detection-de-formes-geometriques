import cv2

def detect_polygons(image):
    """
    Détection de polygones (triangles, rectangles)
    Méthode : Contours + approxPolyDP
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        # Approximatation polygonale (epsilon dépend du périmètre)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        # Dessin et classification
        if len(approx) == 3:
            cv2.drawContours(image, [approx], 0, (0,255,255), 3)
            cv2.putText(image, "Triangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

        elif len(approx) == 4:
            cv2.drawContours(image, [approx], 0, (255,0,0), 3)
            cv2.putText(image, "Rectangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    return image
