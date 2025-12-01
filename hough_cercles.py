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
# Détection de cercles 
# =========================
def lancer_detection_cercle(image_path):
    if not image_path:
        messagebox.showerror("Erreur", "Aucune image sélectionnée.")
        return

    # Charger image
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Erreur", "Impossible de charger l'image.")
        return

    # Redimensionner
    max_width = 600
    if img.shape[1] > max_width:
        scale = max_width / img.shape[1]
        img = cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))

    # Prétraitement
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Fenêtre OpenCV
    cv2.namedWindow('Hough Circles')

    # Trackbars
    cv2.createTrackbar('Param1', 'Hough Circles', 100, 500, nothing)
    cv2.createTrackbar('Param2', 'Hough Circles', 30, 200, nothing)
    cv2.createTrackbar('MinRadius', 'Hough Circles', 10, 100, nothing)
    cv2.createTrackbar('MaxRadius', 'Hough Circles', 100, 300, nothing)

    while True:
        param1 = cv2.getTrackbarPos('Param1', 'Hough Circles')
        param2 = cv2.getTrackbarPos('Param2', 'Hough Circles')
        min_radius = cv2.getTrackbarPos('MinRadius', 'Hough Circles')
        max_radius = cv2.getTrackbarPos('MaxRadius', 'Hough Circles')

        output = img.copy()

        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=1,
            minDist=20,
            param1=param1,
            param2=param2,
            minRadius=min_radius,
            maxRadius=max_radius
        )

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)
            print(f"Nombre de cercles détectés : {len(circles[0])}")

        cv2.imshow('Hough Circles', output)

        # ESC pour sortir
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

# =========================
# Interface Tkinter
# =========================
def interface_cercles():
    root = tk.Tk()
    root.title("Détection de cercles - Tkinter + OpenCV")
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
        lancer_detection_cercle(selected_image.get())

    # Widgets
    tk.Button(root, text="📂 Charger une image", width=25, command=btn_load).pack(pady=35)
    tk.Button(root, text="▶ Lancer la détection", width=25, command=btn_start).pack(pady=15)

    label = tk.Label(root, text="Aucune image sélectionnée.", fg="blue")
    label.pack()

    root.mainloop()

