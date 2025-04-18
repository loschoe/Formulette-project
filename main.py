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
    print("Thème 3 : Énergies")
    print("Thème 4 : Ondes et signaux")
    print("Thème 5 : Notions d'électricité")
    print('Tapez "maths" pour des Théorèmes mathémtatiques')
    print('Tapez "exit" pour quitter' + Style.RESET_ALL)

def affichage():
    title()
    while True :
        menu()
        choix = (input(Fore.BLUE + "\nChoisissez un thème : " + Style.RESET_ALL))

        
# ============================================= THEME 1 ================================================
        if choix == "1" :
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Constitution et transformation de la matière !" + Style.RESET_ALL)
            print(Fore.CYAN + """1. Pression
2. Calcul du pH
3. Calcul de la réciproque [𝐻3𝑂+]
4. Quantité de matière
5. Quantité de matière avec un volume  
6. Concentration molaire
                   
'Tapez "exit" pour quitter'
""")
            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)
            match sous_choix.lower():
                case"1": pression()
                case"2": calcul_ph() 
                case"3": calcul_reciproque_H30()
                case"4": calcul_quantite_matiere()
                case "5": quantite_matiere_volume()
                case"6": concentration_molaire()
                case "exit":
                    print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
                    break
                case _:
                    print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)
                    break
            ()

# ============================================= THEME 2 ================================================     
        elif choix == "2" :
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Mouvement et interaction !" + Style.RESET_ALL)

            print(Fore.CYAN + "2e loi de Newton\n Tapez 'exit' pour quitter")

            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)
            match sous_choix.lower():
                case "1": IIeNewton()
                case "exit":
                    print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
                    break
                case _:
                    print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)
                    break
            ()

# ============================================= THEME 3 ================================================
        elif choix == "3":
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Énergies !\n\n" + Style.RESET_ALL)

            print(Fore.CYAN + """1.  Pression
2.  Équation des gaz parfaits
3.  Premier principe de la thermodynamique\n
4.  Énergie totale
5.  Énergie cinétique
6.  Énergie potentielle\n
7.  Travail et énergie interne
8.  Puissance mécanique et énergétique
9.  Rendement énergétique\n
10. Capacité thermique et variation d’énergie interne
11. Conversion calorie ↔ Joule
12. Flux thermique
13. Résistance thermique
14. Modèle de la loi de Newton\n
'Tapez "exit" pour quitter'
""")
            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)

            match sous_choix.lower():
                case "1": pression()
                case "2": gaz_parfait()
                case "3": premier_principe_thermo()
                case "4": energie_totale()
                case "5": energie_cinetique()
                case "6": energie_potentielle()
                case "7": variation_energie_interne()
                case "8": puissance()
                case "9": rendement()
                case "10": variation_energie_capacite()
                case "11": conversion_cal_joule()
                case "12": flux_thermique()
                case "13": resistance_thermique()
                case "14": modele_Newton()
                case "exit":
                    print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
                    break
                case _:
                    print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)
                    break
            ()

# ============================================= THEME 4 ================================================
        elif choix == "4" : 
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Ondes et signaux !" + Style.RESET_ALL)

            print(Fore.CYAN + """
1. Intensité sonore
2. Niveau d'intensité sonore
3. Atténuation géométrique
4. Atténuation par absorption
5. Effet Doppler\n
6. Diffraction
7. Taille de la tâche centrale\n
8. Lentille convergente
9. Lunette astronomique 
10. Condition pour un grossissement supérieur à 1\n
'Tapez "exit" pour quitter'        
""")

            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)
            match sous_choix.lower():
                case "1": intensite_sonore()
                case "2": niv_intensite_sonore()
                case "3": attenuation_geometrique()
                case "4": attenuation_absorption()
                case "5": effet_doppler()
                case "6": diffraction()
                case "7": tache_centrale()
                # Case 8
                # Case 9
                # Case 10 
                # AJOUT DES AUTRES MENUS 

                case "exit":
                    print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
                    break
                case _:
                    print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)
                    break
            ()

# ============================================= THEME 5 ================================================
        elif choix == "5":
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Notions d'électricité !" + Style.RESET_ALL)

            print(Fore.CYAN + """1. Loi d'Ohm
2. Puissance électrique
3. Énergie électrique 
4. Association de résistance 
5. Loi des nœuds et des mailles (Loi de Kirchhoff)
6. Condensateurs et bobines
                  
'Tapez "exit" pour quitter'        
""")
            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)

            match sous_choix.lower():
                case "1":
                    pass  # ohm()
                case "2":
                    pass  # puissance_electrique()
                case "3":
                    pass  # energie_electrique()
                case "4":
                    pass  # association_resistance()
                case "5":
                    pass  # Kirchhoff()
                case "6":
                    pass  # condensateurs()
                case "exit":
                    print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
                    break
                case _:
                    print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)

# ============================================= THEME maths ================================================
        elif choix == "maths":
            print(Fore.MAGENTA + "\n▶ Vous avez choisi le thème : Théorèmes mathématiques !\n\n" + Style.RESET_ALL)

            print(Fore.CYAN + "1. Pythagore")
            print("2. Thalès")

            sous_choix = input(Fore.BLUE + "\nChoisissez une formule : " + Style.RESET_ALL)

            if sous_choix == "1":
                pythagore()
            elif sous_choix == "2":
                thales()
            elif sous_choix.lower() == "exit":  # Normalisation de la casse
                print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)

        elif choix.lower() == "exit":
            print(Fore.RED + "\nÀ Bientôt 👍\n" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "❌ Option invalide, retour au menu principal.\n" + Style.RESET_ALL)

affichage()