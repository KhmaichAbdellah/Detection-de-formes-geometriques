# 🔷 Détection de Formes Géométriques

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange" alt="Tkinter"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"/>
</p>

> Application Python de détection de formes géométriques dans des images, utilisant les algorithmes de vision par ordinateur d'**OpenCV** : Transformée de Hough (lignes & cercles) et approximation polygonale par contours.

---

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture du projet](#-architecture-du-projet)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Méthodes de détection](#-méthodes-de-détection)
- [Exemples de résultats](#-exemples-de-résultats)
- [Auteur](#-auteur)

---

## 🔍 Aperçu

Ce projet implémente un système de **détection automatique de formes géométriques** dans des images statiques. L'utilisateur sélectionne une image via une interface graphique, puis choisit parmi plusieurs méthodes de détection dans un menu interactif.

Les trois méthodes disponibles reposent sur des algorithmes classiques de traitement d'image :

| Méthode | Formes détectées | Algorithme |
|---------|-----------------|------------|
| Hough Lines | Lignes droites | `HoughLinesP` (probabiliste) |
| Hough Circles | Cercles | `HoughCircles` (gradient) |
| Polygones | Triangles, Rectangles | `findContours` + `approxPolyDP` |

---

## ✨ Fonctionnalités

- 📂 **Sélection d'image** via une boîte de dialogue graphique (Tkinter)
- 📏 **Détection de lignes** avec la Transformée de Hough Probabiliste
- ⭕ **Détection de cercles** avec HoughCircles (méthode du gradient)
- 🔺 **Détection de polygones** : triangles (3 sommets) et rectangles (4 sommets)
- 🔁 **Mode combiné** : application des 3 méthodes simultanément
- 🖼️ **Visualisation** des résultats avec OpenCV (affichage en temps réel)
- 🔄 **Menu interactif** en boucle pour tester plusieurs méthodes sur la même image

---

## 📁 Architecture du projet

```
Detection-de-formes-geometriques/
│
├── main.py               # Point d'entrée – menu interactif & sélection d'image
├── hough_lines.py        # Module : détection de lignes (HoughLinesP)
├── hough_circles.py      # Module : détection de cercles (HoughCircles)
├── detect_polygons.py    # Module : détection de polygones (contours + approxPolyDP)
├── test.py               # Script de test rapide
└── README.md             # Documentation du projet
```

---

## 🛠️ Prérequis

- Python **3.8** ou supérieur
- Les bibliothèques suivantes :

| Bibliothèque | Rôle |
|---|---|
| `opencv-python` | Traitement d'image et algorithmes de détection |
| `numpy` | Calcul matriciel |
| `tkinter` | Interface graphique (dialogue de sélection de fichier) |

> **Note :** `tkinter` est inclus par défaut avec Python sur Windows et macOS. Sur Linux, il peut nécessiter une installation séparée (`sudo apt-get install python3-tk`).

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/KhmaichAbdellah/Detection-de-formes-geometriques.git
cd Detection-de-formes-geometriques
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install opencv-python numpy
```

---

## ▶️ Utilisation

```bash
python main.py
```

**Déroulement :**

1. Une boîte de dialogue s'ouvre → **sélectionnez une image** (JPG, PNG, BMP, TIF)
2. Le menu interactif s'affiche dans le terminal :

```
===== MENU DÉTECTION DE FORMES =====
1 - Détecter les lignes (HoughLinesP)
2 - Détecter les cercles (HoughCircles)
3 - Détecter les rectangles / polygones
4 - Appliquer toutes les méthodes
0 - Quitter
```

3. Entrez le numéro de la méthode souhaitée
4. L'image annotée s'affiche dans une fenêtre OpenCV
5. Appuyez sur **n'importe quelle touche** pour revenir au menu

---

## 🧠 Méthodes de détection

### 1. 📏 Détection de Lignes — `hough_lines.py`

Utilise la **Transformée de Hough Probabiliste** (`HoughLinesP`) :

1. Conversion en niveaux de gris
2. Flou gaussien (réduction du bruit)
3. Détection des contours (Canny — seuils : 30/120)
4. Application de `HoughLinesP` (rho=1, theta=π/180, threshold=50)
5. Tracé des lignes détectées en **rouge**

### 2. ⭕ Détection de Cercles — `hough_circles.py`

Utilise **HoughCircles** avec la méthode du gradient :

1. Conversion en niveaux de gris
2. Flou médian (réduction du bruit de sel & poivre)
3. Application de `HoughCircles` (dp=1.2, minDist=30, param1=100, param2=30)
4. Tracé des cercles détectés en **vert**

### 3. 🔷 Détection de Polygones — `detect_polygons.py`

Utilise la détection de contours et l'approximation polygonale :

1. Conversion en niveaux de gris
2. Détection des contours (Canny — seuils : 50/150)
3. Extraction des contours (`findContours`)
4. Approximation avec `approxPolyDP` (epsilon = 2% du périmètre)
5. Classification selon le nombre de sommets :
   - **3 sommets** → Triangle (couleur **cyan**)
   - **4 sommets** → Rectangle (couleur **bleu**)

---

## 📊 Exemples de résultats

| Méthode | Couleur d'annotation | Formes |
|---|---|---|
| Lignes (Hough) | 🔴 Rouge | Segments de droites |
| Cercles (Hough) | 🟢 Vert | Cercles & ellipses |
| Polygones (Contours) | 🔵 Bleu / 🩵 Cyan | Rectangles / Triangles |

---

## 👤 Auteur

**Khmaich Abdellah**

- 🐙 GitHub : [@KhmaichAbdellah](https://github.com/KhmaichAbdellah)

---

## 📄 Licence

Ce projet est distribué sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

<p align="center">
  Fait avec ❤️ et OpenCV 🔬
</p>
