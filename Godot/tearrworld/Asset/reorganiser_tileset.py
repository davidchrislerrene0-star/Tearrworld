from PIL import Image

BASE = "/home/ben-abdallah-bilel/Bureau/Godot/asset/"
HAUTEUR_BANDE = 992

fichiers = [
    "DP_Interieur.png",
]

for nom in fichiers:
    img = Image.open(BASE + nom)
    largeur, hauteur = img.size
    bandes = []
    y = 0
    while y < hauteur:
        bas = min(y + HAUTEUR_BANDE, hauteur)
        bandes.append(img.crop((0, y, largeur, bas)))
        y += HAUTEUR_BANDE
    base_nom = nom.replace(".png", "")
    part = 1
    i = 0
    while i < len(bandes):
        if i + 1 < len(bandes):
            h = max(bandes[i].size[1], bandes[i+1].size[1])
            sortie = Image.new("RGBA", (largeur * 2, h), (0, 0, 0, 0))
            sortie.paste(bandes[i], (0, 0))
            sortie.paste(bandes[i+1], (largeur, 0))
            i += 2
        else:
            sortie = Image.new("RGBA", (largeur, bandes[i].size[1]), (0, 0, 0, 0))
            sortie.paste(bandes[i], (0, 0))
            i += 1
        sortie.save(BASE + base_nom + "_part" + str(part) + ".png")
        print("OK " + base_nom + "_part" + str(part))
        part += 1
