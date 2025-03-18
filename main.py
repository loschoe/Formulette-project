# Les importations de modules : 
from lib import *
from pyfiglet import *
from colorama import Fore, Style

# Définition du menu principale : 
def title():
    titre = figlet_format("Formulette", font="slant")
    print(Fore.CYAN + titre + Style.RESET_ALL)

def menu():
    print(Fore.YELLOW + "=" * 40)
    print(" " * 10 + "MENU PRINCIPALE")
    print("=" * 40 + Style.RESET_ALL)
    print(Fore.GREEN + "Thème 1 : Constitution et transformation de la matière")
    print("Thème 2 : Mouvement et interaction")
    print("Thème 3 : Energies")
    print("Thème 4 : Ondes et signaux")
    print("Thème 5 : Notions d'électricité")
    print('Tapez "maths" pour des Théorèmes mathémtatiques')
    print('Tapez "exit" pour quitter' + Style.RESET_ALL)

def affichage():
    title()
    while True :
        menu()
        choix = (input(Fore.BLUE + "\nChoisissez un thème : " + Style.RESET_ALL))

        if choix == "1" :
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Constitution et transformation de la matière !" + Style.RESET_ALL)






        elif choix == "2" :
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Mouvement et interaction !" + Style.RESET_ALL)






        elif choix == "3":
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Energies !\n\n" + Style.RESET_ALL)

            print(Fore.CYAN + """1.  Pression
32.  Equation des gaz parfaits
33.  Premier principe de la thermodynamique\n
34.  Energie totale
35.  Energie cinétique
36.  Energie potentielle\n
37.  Travail et énergie interne
38.  Puissance mécanique et énergétique
39.  Rendement énergétique\n
310. Capacité thermique et variation d’énergie interne
311. Conversion calorie ↔ Joule
312. Flux thermique
313. Résistance thermique
314. Modèle de la loi de Newton\n
3'Tapez "exit" pour quitter'
3""")

            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)
            try:
                if sous_choix == "1":
                    pression()
                elif sous_choix == "2":
                    gaz_parfait()
                elif sous_choix == "3":
                    premier_principe_thermo()
                elif sous_choix == "4":
                    energie_totale()
                elif sous_choix == "5":  # Ajout des guillemets
                    energie_cinetique()
                elif sous_choix == "6":  # Ajout des guillemets
                    energie_potentielle()
                elif sous_choix == "7":
                    variation_energie_interne()
                elif sous_choix == "8":
                    puissance()
                elif sous_choix == "9":
                    rendement()
                elif sous_choix == "10":
                    variation_energie_capacite()
                elif sous_choix == "11":
                    conversion_cal_joule()
                elif sous_choix == "12":
                    flux_thermique()
                elif sous_choix == "13":
                    resistance_thermique()
                elif sous_choix == "14":  # Correction du "!"" en ":"
                    modele_Newton()
                elif sous_choix.lower() == "exit":
                    print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)
                break
            except:pass



        elif choix == "4" : 
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Ondes et signaux !" + Style.RESET_ALL)



        elif choix == "maths":
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Théorèmes mathématiques !\n\n" + Style.RESET_ALL)

            print(Fore.CYAN + "1. Pythagor")
            print("2. Thalèse")

            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)

            if sous_choix == "1":
                pythagore()
            elif sous_choix == "2":
                thales()
            elif sous_choix.lower() == "exit":  # Normalisation de la casse
                print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
            else:
                print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)
            break

        elif choix == "exit":
            print(Fore.RED + "\nÀ Bientot 👍\n" + Style.RESET_ALL)
            break

        else : print(Fore.RED + "❌ Option invalide, retour au menu principale.\n" + Style.RESET_ALL)
affichage()