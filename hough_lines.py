import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

# =========================
# Trackbar callback
# =========================
def nothing(x):
    pass

# =========================
# Sélection d'image
# =========================
def choisir_image():
    filepath = filedialog.askopenfilename(
        title="Choisir une image",
        filetypes=[("Images", "*.jpg *.png *.jpeg *.bmp")]
    )
    return filepath

# =========================
# Détection de lignes
# =========================
def lancer_detection_ligne(image_path):
    if not image_path:
        messagebox.showerror("Erreur", "Aucune image sélectionnée.")
        return

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Erreur", "Impossible de charger l'image.")
        return

    # Redimensionner si nécessaire
    max_width = 600
    if img.shape[1] > max_width:
        scale = max_width / img.shape[1]
        img = cv2.resize(img, (int(img.shape[1]*scale), int(img.shape[0]*scale)))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1.5)

    # Fenêtre OpenCV
    cv2.namedWindow('Hough Lines')

    # Trackbars pour paramètres dynamiques
    cv2.createTrackbar('Threshold', 'Hough Lines', 50, 200, nothing)
    cv2.createTrackbar('MinLineLength', 'Hough Lines', 20, 200, nothing)
    cv2.createTrackbar('MaxLineGap', 'Hough Lines', 20, 100, nothing)
    cv2.createTrackbar('Canny1', 'Hough Lines', 30, 300, nothing)
    cv2.createTrackbar('Canny2', 'Hough Lines', 120, 300, nothing)

    while True:
        # Lire les valeurs des trackbars
        threshold = cv2.getTrackbarPos('Threshold', 'Hough Lines')
        min_line_length = cv2.getTrackbarPos('MinLineLength', 'Hough Lines')
        max_line_gap = cv2.getTrackbarPos('MaxLineGap', 'Hough Lines')
        canny1 = cv2.getTrackbarPos('Canny1', 'Hough Lines')
        canny2 = cv2.getTrackbarPos('Canny2', 'Hough Lines')

        # Détection des contours
        edges = cv2.Canny(blur, canny1, canny2)

        # Détection des lignes
        lines = cv2.HoughLinesP(
            edges,
            rho=1,
            theta=np.pi/180,
            threshold=threshold,
            minLineLength=min_line_length,
            maxLineGap=max_line_gap
        )

        output = img.copy()
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(output, (x1, y1), (x2, y2), (0, 0, 255), 2)

        cv2.imshow('Hough Lines', output)

        # ESC pour quitter
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

# =========================
# Interface Tkinter
# =========================
def interface_lignes():
    root = tk.Tk()
    root.title("Détection de lignes - Tkinter + OpenCV")
    root.geometry("350x200")

    selected_image = tk.StringVar()

    # Bouton charger
    def btn_load():
        img = choisir_image()
        if img:
            selected_image.set(img)
            label.config(text=f"Image sélectionnée :\n{img.split('/')[-1]}")

    # Bouton lancer
    def btn_start():
        lancer_detection_ligne(selected_image.get())

    # Widgets
    tk.Button(root, text="📂 Charger une image", width=25, command=btn_load).pack(pady=35)
    tk.Button(root, text="▶ Lancer la détection", width=25, command=btn_start).pack(pady=15)

    label = tk.Label(root, text="Aucune image sélectionnée.", fg="blue")
    label.pack()

    root.mainloop()


