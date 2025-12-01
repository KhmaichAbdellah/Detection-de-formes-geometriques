import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

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
# Détection des rectangles
# =========================
def lancer_detection_rectangle(image_path):
    if not image_path:
        messagebox.showerror("Erreur", "Aucune image sélectionnée.")
        return

    # Charger image
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

    # Détection des contours
    edges = cv2.Canny(blur, 50, 150)

    # Trouver tous les contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rectangles = 0
    for cnt in contours:
        # Approximation polygonale
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # Si le polygone a 4 côtés => rectangle
        if len(approx) == 4:
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
            rectangles += 1

    print(f"Nombre de rectangles détectés : {rectangles}")

    cv2.imshow("Detection Rectangles", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# =========================
# Interface Tkinter
# =========================
def interface_rectangle():
    root = tk.Tk()
    root.title("Détection de rectangles - Tkinter + OpenCV")
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
        lancer_detection_rectangle(selected_image.get())

    # Widgets
    tk.Button(root, text="📂 Charger une image", width=25, command=btn_load).pack(pady=35)
    tk.Button(root, text="▶ Lancer la détection", width=25, command=btn_start).pack(pady=15)

    label = tk.Label(root, text="Aucune image sélectionnée.", fg="blue")
    label.pack()

    root.mainloop()

