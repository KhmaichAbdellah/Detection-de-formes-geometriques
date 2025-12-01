from hough_lines import interface_lignes
from hough_circles import interface_cercles
from approximation_polygonale import interface_rectangle


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
    while True:
        choix = afficher_menu()

        if choix == "0":
            print("👋 Fin du programme.")
            break

        elif choix == "1":
            interface_lignes()

        elif choix == "2":
            interface_cercles()

        elif choix == "3":
            interface_rectangle()

        elif choix == "4":
            interface_lignes()
            interface_cercles()
            interface_rectangle()

        else:
            print("❌ Choix invalide, réessayez.")
            continue


if __name__ == "__main__":
    main()
