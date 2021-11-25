# une variable dois etre définie avant d'être utilisée
"""
Commentaire sur plusieures lignes

"""
NB_PERSONNES = 4


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom ? : ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est ton age ? :")
        try:
            age_int = int(age_str)  # int transforme une valeur str en int
        except ValueError:  # peut prendre un type d'erreur a prendre en charge, ici ValueError
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


def demander_taille(nom_personne):
    size = 0
    while size == 0:
        size = input(nom_personne + " quel est ta taille ? :")
    return size


def print_nom_age(nom, age, taille=0):
    print("Tu t'apelle " + nom + ", tu as " + str(age) + "ans.")
    print("l'an prochain tu auras " + str(age + 1) + " ans.")  # str transforme une valeur int en str

    if age == 17:
        print("Vous êtes presque majeur.")
    elif 12 <= age < 18:
        print("Vous êtes adolescent.")
    elif age == 18:
        print("Vous êtes tout juste majeur, félicitation !")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé.")
    elif age < 10:
        print("Vous êtes enfant.")
    elif age >= 60:
        print("Vous êtes sénior")
    elif age > 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")

    if not taille == 0:
        print("Et tu meusure " + str(taille) + " m.")


for i in range(0, NB_PERSONNES):
    nom = demander_nom()
    age = demander_age(nom)
    taille = demander_taille(nom)
    print_nom_age(nom, age, taille)
