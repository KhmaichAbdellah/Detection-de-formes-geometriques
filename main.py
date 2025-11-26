import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

from hough_lines import detect_hough_lines
from hough_circles import detect_hough_circles
from detect_polygons import detect_polygons

print("Fenêtre ouverte ! Choisissez une image...")
def choisir_image():
    """Ouvre une boîte de dialogue pour choisir une image."""
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename(
        title="Choisir une image",
        filetypes=[
            ("Images", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"),
            ("Tous les fichiers", "*.*")
        ]
    )
    return filepath


def afficher_menu():
    print("\n===== MENU DÉTECTION DE FORMES =====")
    print("1 - Détecter les lignes (HoughLinesP)")
    print("2 - Détecter les cercles (HoughCircles)")
    print("3 - Détecter les rectangles / polygones")
    print("4 - Appliquer toutes les méthodes")
    print("0 - Quitter")
    
    choix = input("\n👉 Entrez votre choix : ")
    return choix


def main():
    # Sélection de l'image
    path = choisir_image()

    if not path:
        messagebox.showerror("Erreur", "Aucune image sélectionnée !")
        return

    image = cv2.imread(path)

    if image is None:
        messagebox.showerror("Erreur", "Impossible de charger l'image.")
        return

    while True:
        choix = afficher_menu()

        if choix == "0":
            print("👋 Fin du programme.")
            break

        elif choix == "1":
            img = detect_hough_lines(image.copy())
            cv2.imshow("Détection des lignes", img)

        elif choix == "2":
            img = detect_hough_circles(image.copy())
            cv2.imshow("Détection des cercles", img)

        elif choix == "3":
            img = detect_polygons(image.copy())
            cv2.imshow("Détection des polygones", img)

        elif choix == "4":
            img1 = detect_hough_lines(image.copy())
            img2 = detect_hough_circles(image.copy())
            img3 = detect_polygons(image.copy())

            cv2.imshow("Lignes", img1)
            cv2.imshow("Cercles", img2)
            cv2.imshow("Polygones", img3)

        else:
            print("❌ Choix invalide, réessayez.")
            continue

        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
