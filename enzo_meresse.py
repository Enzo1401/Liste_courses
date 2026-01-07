# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py liste_courses.py"

# Variables
liste_course = {
    "pates": 2,
    "sauce tomate": 1,
    "parmesan": 1
}

# Fonctions

def afficher_liste(liste_course):
    print("Votre liste de courses :")
    for index, (product, quantity) in enumerate(liste_course.items()):
            print(f"{index + 1} - {product} : {quantity} produits")

def show_actions():
    print()
    print("1 - Ajouter")
    print("2 - Supprimer")
    print("3 - Modifier")
    print("4 - Voir")
    print("5 - Quitter")


#########################
### Début du programe ###
#########################

user_choice = ""
while user_choice != "5":

    print("Bienvenue dans la liste de courses.\n")
    print("Que voulez vous faire ? \n")
    show_actions()
    list_liste_course = list(liste_course)
    user_choice = input("Saisissez le chiffre correspondant à votre choix : ")

    if user_choice == "1": 
        add_product = str(input("Que souhaitez-vous ajoutez à la liste de courses ? : ")).lower()
        
        #gestion des erreurs de quantité ajouté
        while True:
            add_quantity = input("Combien de produits souhaitez-vous ajoutez ? : ")
            if add_quantity.isdigit():
                break
            print("Veuillez entrer un nombre entier.")

        add_quantity = int(add_quantity)
        liste_course[add_product] = add_quantity
        print()
        afficher_liste(liste_course)
        print()

    elif user_choice == "2":
        for index, product in enumerate(liste_course):
            print(f"{index + 1} - {product}")

        #gestion des erreurs de suppression 
        while True:
            delete_product = input("Quel produit souhaitez-vous supprimer ? (saisissez le numéro) : ")
            if delete_product.isdigit():
                break
            print("Veuillez entrer le nombre entier du produit que vous souhaitez retirer de la liste.")

        delete_product = int(delete_product)
        del liste_course[list_liste_course[delete_product - 1]]
        print()
        afficher_liste(liste_course)
        print()

    elif user_choice == "3":
        for index, product in enumerate(liste_course) :
            print(f"{index + 1} - {product} : {liste_course.get(product)}")

        #gestion des erreurs de sélection du produit et de modification de quantité
        while True :
            modify_product = input("Quel produit souhaitez-vous modifier ? (saisissez le numéro) : ")
            new_quantity = input("Quelle est la nouvelle quantité souhaitée ? : ")
            if modify_product.isdigit() and new_quantity.isdigit():
                break
            print("Veuillez entrer le nombre entier correspondant à votre produit pour pouvoir le modifier.")

        modify_product = int(modify_product)
        new_quantity = int(new_quantity)
        liste_course[list_liste_course[modify_product - 1]] = new_quantity
        print()
        afficher_liste(liste_course)
        print()

    elif user_choice == "4":
        print()
        afficher_liste(liste_course)
        print()

    elif user_choice == "5":
        print("A bientot")
