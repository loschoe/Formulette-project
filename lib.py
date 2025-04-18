import math
from mendeleev import element
import re

# Thème 1 : CONSTITUTION ET TRANSFORMATION DE LA MATIÈRE
# La formule de la pression est déjà codée !
def calcul_reciproque_H30():
    """
    Calcule la cencentration en ions oxonium [H30+] à partir du pH.
    Formule : [H₃O⁺] = 10^(-pH)
    
    Entrées :
    - pH : Potentiel hydrogène (sans unité)
    Sortie : 
    - [H₃O⁺] : Concentration en mol/L
    """
    pH = float((input("Entrer le pH : ")))
    assert pH >= 0, "le pH est positif ou nul"

    H3O = 10 ** (-pH)
    print("Voici le calcul : [H₃O⁺] = 10^(-pH)")
    print(f"\n[H₃O⁺] = {H3O:.5e} mol/L\n")

def calcul_ph():
    """
    Calcule le pH d'une solution acide à partir de la concentration en ions H₃O⁺.

    Paramètres :
    - concentration_H3O (float) : Concentration en mol/L

    Retourne :
    - pH (float) : Potentiel hydrogène (sans unité)
    """
    concentration_H3O = int(input("Quelle est la concentration [H₃O⁺]"))
    assert concentration_H3O > 0, "La concentration [H₃O⁺] doit être strictement positive."

    print("Formule : pH = -log₁₀([H₃O⁺])")

    ph = -math.log10(concentration_H3O)
    print(f"\nRésultat : pH = {ph:.2f}\n")

def masse_molaire():
    """
    Calcule la masse molaire d'une molécule.
    
    Entrée :
    - molécule : Formule chimique de la molécule (ex. H2O)
    Sortie :
    - masse molaire en g/mol
    """
    molecule = input("Entrez la formule de la molécule : ").strip()
    pattern = r'([A-Z][a-z]*)(\d*)'
    matches = re.findall(pattern, molecule)
    
    molar_mass = 0.0
    
    for (el, count) in matches:
        elem = element(el)
        
        if elem is None:
            raise ValueError(f"L'élément '{el}' n'existe pas dans le tableau périodique.")
        
        mass = elem.mass
        
        count = int(count) if count else 1
        molar_mass += mass * count
    
    assert molar_mass > 0, "La masse molaire doit être strictement positive."
    
    return molar_mass

def concentration_molaire():
    """
    Calcule la concentration molaire d'une solution.

    Paramètres :
    - n (float) : Quantité de matière en mol
    - V (float) : Volume de la solution en litres (L)

    Retourne :
    - C (float) : Concentration molaire en mol/L
    """
    n = int(input("La quantité de matière en mol : "))
    V = int(input("Le volume de la solution en litre : "))

    assert n >= 0, "La quantité de matière doit être positive ou nulle."
    assert V > 0, "Le volume doit être strictement positif."

    print("Formule : C = n / V")
    C = n / V
    print(f"\nRésultat : C = {C:.4f} mol/L\n")

def calcul_quantite_matiere():
    """
    Calcule la quantité de matière (n) en fonction de la masse et de la masse molaire.
    Formule : n = m / M
    """
    try:
        masse = float(input("Entrer la masse (g) : "))
        molar_mass = masse_molaire()
        
        if molar_mass <= 0:
            raise ValueError("Erreur de calcul : la masse molaire est invalide.")
        
        quantite_matiere = masse / molar_mass
        print(f"\nLa quantité de matière est de {quantite_matiere:.5f} mol.\n")
    
    except ValueError as e:
        print(f"Erreur : {e}")

def quantite_matiere_volume():
    """
    Calcule la quantité de matière à partir du volume d’un gaz.

    Paramètres :
    - V (float) : Volume du gaz en litres (L)
    - Vm (float) : Volume molaire en L/mol (par défaut : 24.0 L/mol à 25°C)

    Retourne :
    - n (float) : Quantité de matière en moles (mol)
    """
    V = int(input("Le volume du gaz en litre : "))
    Vm = int(input("Le volume molaire en L/mol : "))

    assert V >= 0, "Le volume V doit être positif ou nul."
    assert Vm > 0, "Le volume molaire Vm doit être strictement positif."

    print("Quantité de matière (à partir du volume)")
    print("Formule : n = V / Vm")

    n = V / Vm
    print(f"\nRésultat : n = {n:.4f} mol\n")


# Thème 2 : MOUVEMENT ET INTERACTION 
def IIeNewton():
    """
    Ennonce la deuxième loi de Newton mais n'éffectue pas la calcul.
    Formule : F = m × a
    
    Entrées :
    - m : masse du système en kilogramme (kg)
    - a : accélération en m.s²  
    Sortie : 
    - La force F en N 
    """
    print ("\nÉnnonciation de la 2e loi de Newton : F = m × a\n")

# Thème 3 : ENERGIES 
def pression():
    """
    Calcule la pression en fonction de la force et de la surface.
    Formule : P = F / S
    
    Entrées :
    - F : Force en newtons (N)
    - S : Surface en mètres carrés (m²)
    Sortie :
    - P : Pression en pascals (Pa)
    """

    F = float(input("Entrez la force (N) : "))
    S = float(input("Entrez la surface (m²) : "))
    P = F / S

    assert F > 0, "La force doit être strictement positive."
    assert S > 0, "La surface doit être strictement positive."

    print("Voici le calcul : P = F / S")
    print(f"\nLa pression est de {P} Pa.\n")

R = 8.314  # Constante des gaz parfaits en J/(mol.K)

def gaz_parfait():
    """
    Calcule une valeur manquante dans l'équation des gaz parfaits : P × V = n × R × T.
    L'utilisateur peut laisser une valeur vide pour la calculer.
    
    Entrées :
    - P : Pression en pascals (Pa) (optionnel)
    - V : Volume en mètres cubes (m³) (optionnel)
    - n : Quantité de matière en moles (mol) (optionnel)
    - T : Température en kelvins (K) (optionnel)
    
    Sortie :
    - Affiche la valeur calculée
    """
    
    print("Laissez une valeur vide (appuyez sur Entrée) pour la calculer.")
    P = input("Pression (Pa) : ")
    V = input("Volume (m³) : ")
    n = input("Quantité de matière (mol) : ")
    T = input("Température (K) : ")
    
    assert any([P is None, V is None, n is None, T is None]), "Une seule valeur doit être laissée vide."
    assert all(val is None or val > 0 for val in [P, V, n, T]), "Toutes les valeurs doivent être strictement positives."
    
    P = float(P) if P else None
    V = float(V) if V else None
    n = float(n) if n else None
    T = float(T) if T else None

    if P is None:
        P = (n * R * T) / V
        print(f"\nLa pression est de {P} Pa.\n")
    elif V is None:
        V = (n * R * T) / P
        print(f"\nLe volume est de {V} m³.\n")
    elif n is None:
        n = (P * V) / (R * T)
        print(f"\nLa quantité de matière est de {n} mol.\n")
    elif T is None:
        T = (P * V) / (n * R)
        print(f"\nLa température est de {T} K.\n")
    else:
        print("Il faut laisser une valeur vide pour la calculer.\n")

def energie_totale():
    """
    Calcule l'énergie totale d'un système.
    Formule : Etot = Ec + Ep
    
    Entrées :
    - Ec : Énergie cinétique en joules (J)
    - Ep : Énergie potentielle en joules (J)
    
    Sortie :
    - Etot : Énergie totale en joules (J)
    """
    
    Ec = float(input("Énergie cinétique (J) : "))
    Ep = float(input("Énergie potentielle (J) : "))

    assert Ec >= 0, "L'énergie cinétique doit être positive ou nulle."
    assert Ep >= 0, "L'énergie potentielle doit être positive ou nulle."

    Etot = Ec + Ep

    print(f"\nL'énergie totale est de {Etot} J.\n")

def variation_energie_interne():
    """
    Calcule la variation de l'énergie interne d'un système selon le premier principe de la thermodynamique.
    Formule : ΔU = Q + W
    
    Entrées :
    - Q : Transfert thermique en joules (J)
    - W : Travail en joules (J)
    
    Sortie :
    - ΔU : Variation d'énergie interne en joules (J)
    """

    Q = float(input("Transfert thermique Q (J) : "))
    W = float(input("Travail W (J) : "))

    assert isinstance(Q, (int, float)), "Q doit être un nombre."
    assert isinstance(W, (int, float)), "W doit être un nombre."    

    Delta_U = Q + W
    print(f"\nLa variation d'énergie interne est de {Delta_U} J.\n")

def variation_energie_capacite():
    """
    Calcule la variation d'énergie interne d'un système incompressible en fonction de sa capacité thermique.
    Formule : ΔU = C × (Tf - Ti)
    
    Entrées :
    - C : Capacité thermique en J.K⁻¹
    - Ti : Température initiale en kelvins (K)
    - Tf : Température finale en kelvins (K)
    
    Sortie :
    - ΔU : Variation d'énergie interne en joules (J)
    """

    C = float(input("Capacité thermique (J.K-1) : "))
    Ti = float(input("Température initiale (K) : "))
    Tf = float(input("Température finale (K) : "))

    assert C > 0, "La capacité thermique doit être strictement positive."
    assert Tf != Ti, "La température initiale et finale ne doivent pas être égales."

    Delta_U = C * (Tf - Ti)
    print(f"\nLa variation d'énergie interne est de {Delta_U} J.\n")

def conversion_cal_joule():
    """
    Convertit une énergie entre les unités calorie et joule.
    1 calorie = 4.18 joules
    
    Entrées :
    - Choix entre conversion calorie → joule ou joule → calorie
    - Valeur énergétique à convertir
    
    Sortie :
    - Affiche la valeur convertie
    """

    choix = input("1) Calories → Joules : \n2) Joules → Calories ? : ")

    assert choix in ["1", "2"], "Le choix doit être 1 ou 2."
    
    if choix == "1":
        cal = float(input("Entrez l'énergie en calories : "))
        J = cal * 4.18
        print(f"{cal} cal = {J} J")
    elif choix == "2":
        J = float(input("Entrez l'énergie en joules : "))
        cal = J / 4.18
        print(f"\n{J} J = {cal} cal\n")
    else:
        print("Choix invalide.")

def flux_thermique():
    """
    Calcule le flux thermique Φ à partir du transfert thermique Q et de la durée Δt.
    Formule : Φ = Q / Δt
    
    Entrées :
    - Q (float) : Transfert thermique en joules (J)
    - Δt (float) : Durée du transfert en secondes (s)
    
    Sortie :
    - Affiche le flux thermique en watts (W), où 1 W = 1 J/s
    """
    try:
        Q = float(input("Transfert thermique (J) : "))
        Δt = float(input("Durée du transfert (s) : "))

        assert Δt > 0, "La durée du transfert doit être strictement positive."

        Φ = Q / Δt
        print("Φ = Q / Δt")
        print(f"\nLe flux thermique est de : {Φ} W\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except AssertionError as e:
        print(f"Erreur : {e}")

def resistance_thermique():
    """
    Calcul de la résistance thermique Rth à partir de la différence de température ΔT et de la puissance thermique P.
    Formule : Rth = ΔT / P

    Entrées : 
    - ΔT (float) : Différence de température en Kelvin (K) (doit être ≥ 0)
    - P (float) : Puissance thermique en watt (W) (doit être > 0)

    Sortie :
    - Affiche la résistance thermique en (K.W⁻¹)
    """

    ΔT = float(input("Différence de température (K) : "))
    P = float(input("Puissance thermique (W) : "))

    assert ΔT >= 0, "Erreur : La différence de température doit être positive ou nulle."
    assert P > 0, "Erreur : La puissance thermique doit être strictement positive."

    Rth = ΔT / P
    print(f"Rth = ΔT / P")
    print(f"\nLa résistance thermique est de : {Rth:.2f} K.W⁻¹\n")

def modele_Newton():
    """
    Calcul du flux thermique Φ grâce au modèle de la loi de Newton.
    Formule : Φ = h × S × (θe - θ)

    Entrées :
    - h (float) : Coefficient d’échange convectif (W.m⁻².K⁻¹)
    - S (float) : Surface d’échange thermique (m²) 
    - θe (float) : Température du thermostat (K)
    - θ (float) : Température du fluide (K)

    Sortie :
    - Affiche le flux thermique en Watt (W).
    """

    h = float(input("Coefficient d’échange convectif (W.m⁻².K⁻¹) : "))
    S = float(input("Surface d’échange thermique (m²) : "))
    θe = float(input("Température du thermostat (K) : "))
    θ = float(input("Température du fluide (K) : "))

    assert h > 0, "Erreur : Le coefficient d’échange convectif doit être strictement positif."
    assert S > 0, "Erreur : La surface d’échange thermique doit être strictement positive."

    Φ = h * S * (θe - θ)

    print(f"Φ = h × S × (θe - θ)")
    print(f"\nLe flux thermique est de : {Φ:.2f} W\n")

def puissance():
    """
    Calcul de la puissance mécanique et énergétique avec le travail ou énergie W (J) et le temps t (s)
    Formule : P = W/t
    
    Entrées : 
    - W (float) : Travail ou énergie en joule (J) (doit être positif ou nul)
    - t (float) : Durée en seconde (s) (doit être strictement positif)
    
    Sortie : 
    - Affiche la puissance en watt (W)
    """
    W = float(input("Travail ou énergie en joule (J) : ").strip())
    t = float(input("Durée en seconde (s) : ").strip())

    assert W >= 0, "Erreur : Le travail ou l'énergie doit être positif ou nul."
    assert t > 0, "Erreur : La durée doit être strictement positive."

    P = W / t

    print("P = W / t")
    print(f"\nLa puissance mécanique et énergétique est de : {P:.2f} W\n")

def rendement():
    """
    Calcul du rendement énergétique.
    Formule : η = E_utile / E_reçue
    
    Entrées : 
    - E_utile (float) : Énergie utile en joules (J)
    - E_reçue (float) : Énergie reçue en joules (J) (doit être strictement positive)

    Sortie :
    - Affiche le rendement en pourcentage (%)
    """
    try:
        E_utile = float(input("Énergie utile (J) : ").strip())
        E_reçue = float(input("Énergie reçue (J) : ").strip())

        assert E_utile >= 0, "Erreur : L'énergie utile doit être positive ou nulle."
        assert E_reçue > 0, "Erreur : L'énergie reçue doit être strictement positive."

        η = E_utile / E_reçue
        η_pourcentage = η * 100  # Conversion en %

        print("η = E_utile / E_reçue")
        print(f"\nLe rendement énergétique est de : {η_pourcentage:.2f} %\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

def energie_cinetique():
    """
    Calcul de l'énergie cinétique d'un objet avec sa masse m (kg) et sa vitesse v (m/s)
    Formule : Ec = (1/2) × m × v²

    Entrées : 
    - m (float) : Masse de l'objet en kilogrammes (kg)
    - v (float) : Vitesse de l'objet en mètres par seconde (m/s)

    Sortie : 
    - Affiche l'énergie cinétique de l'objet en joules (J)
    """ 

    try:
        m = float(input("Masse de l'objet (kg) : ").strip())
        v = float(input("Vitesse de l'objet (m/s) : ").strip())

        assert m > 0, "Erreur : La masse doit être strictement positive."
        assert v >= 0, "Erreur : La vitesse ne peut pas être négative."

        Ec = 0.5 * m * (v ** 2)

        print("Ec = 1/2 × m × v²")
        print(f"\nL'énergie cinétique de l'objet est de : {Ec:.2f} J\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

G = 9.81  # Intensité de pesanteur en m/s² sur Terre
def energie_potentielle():
    """
    Calcul de l'énergie potentielle gravitationnelle d'un objet avec sa masse m (kg), sa hauteur h (m)
    et l'intensité de pesanteur g (m/s²).

    Formule : Ep = m × g × h

    Entrées : 
    - m (float) : Masse de l'objet en kilogrammes (kg)
    - h (float) : Hauteur par rapport à un niveau de référence en mètres (m)

    Sortie : 
    - Affiche l'énergie potentielle de l'objet en joules (J)
    """

    try:
        m = float(input("Masse de l'objet (kg) : ").strip())
        h = float(input("Hauteur par rapport à un niveau de référence (m) : ").strip())

        assert m > 0, "Erreur : La masse doit être strictement positive."
        assert h >= 0, "Erreur : La hauteur ne peut pas être négative."

        Ep = m * G * h

        print("Ep = m × g × h")
        print(f"\nL'énergie potentielle de l'objet est de : {Ep:.2f} J\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

def premier_principe_thermo():
    """
    Application du premier principe de la thermodynamique :
    La variation d’énergie interne d’un système est égale à la chaleur reçue moins le travail fourni.

    Formule : ΔU = Q - W

    Entrées :
    - Q (float) : Chaleur échangée avec le système en joules (J)
    - W (float) : Travail fourni par le système en joules (J)

    Sortie :
    - Affiche la variation de l’énergie interne ΔU en joules (J)
    """

    try:
        Q = float(input("Chaleur échangée avec le système (J) : ").strip())
        W = float(input("Travail fourni par le système (J) : ").strip())

        ΔU = Q - W

        print("ΔU = Q - W")
        print(f"\nLa variation de l'énergie interne du système est de : {ΔU:.2f} J\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

# Thème 4 ONDES ET SIGNAUX : 
def intensite_sonore():
    """
    Calcul de l'intensité sonore avec la puissance de la source P (W), la surface de propagation S (m²)
    Formule : I = P / S 

    Entrées : 
    - P (float) : Puissance de la source en watt (W)
    - S (float) : Surface de propagation en mètre carré (m²)

    Sortie : 
    - Affiche l'intensité sonore I (W.m⁻²)
    """
    try:
        P = float((input("Puissance de la source sonore (W) : ")))
        S = float((input("Surface de propagation (m²) : ")))
    
        assert P >= 0, "Erreur : la puissance ne peut pas être négative"
        assert S > 0, "Erreur : la surface de propagation doit être stricement positive"

        I = P / S

        print("I = P / S")
        print(f"\nL'intenisté sonore est de : {I:.2f} W.m⁻²\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

I0 = 1,0*10**-12 # Seuil d'audibilité 
def niv_intensite_sonore():
    """
    Calcul du niveau de l'intensité sonore avec l'intensité I (W.m⁻²), le seuil d'audibilité I0 (W.m⁻²)
    Formule : L = 10 * log(I/I0)  

    Entrée : 
    - I (float) : Intenisté sonore (W.m⁻²)

    Sortie : 
    - Affiche le niveau d'intensité sonore L (dB)
    """
    try:
        I = float(input("Intensité sonore (W.m⁻²) : "))

        assert I > 0, "Erreur : l'intensité doit être strictement positive."

        L = 10 * math.log10(I/I0)

        print("L = 10 * log(I/I0)")
        print(f"\nLe niveau d'intensité sonore est de : {L:.2f} dB\n")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

def attenuation_geometrique():
    """
    Calcul de l'atténuation gémométrique avec le niveau sonore proche Lp (dB), le niveau sonore éloigné Le (dB)
    Formule : A = Lp - Le 

    Entrée : 
    - Lp (float) : Niveau d'intensité sonore proche Lp (dB)
    - Le (float) : Niveau d'intensité sonore éloigné Le (dB)

    Sortie : 
    - Affiche l'atténuation géométrique A en décibels (dB)
    """
    try:
        Lp = float(input("Niveau d'intensité sonore proche (dB) : "))
        Le = float(input("Niveau d'intensité sonore éloigné (dB) : "))

        assert Lp >= 0, "Erreur : Le niveau sonore proche doit être positif."
        assert Le >= 0, "Erreur : Le niveau sonore éloigné doit être positif."
        assert Lp >= Le, "Erreur : Le niveau sonore proche doit être supérieur ou égal au niveau sonore éloigné."

        A = Lp - Le

        print("A = Lp - Le")
        print(f"\nl'atténuation géométrique est de : {A:.2f} dB\n")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except AssertionError as e:
        print(e)

def attenuation_absorption():
    """
    Calcul de l'atténuation par absorption avec le niveau sonore incident Li (dB), 
    le niveau sonore transmis Lt (dB).
    
    Formule : A = Li - Lt 

    Entrée : 
    - Li (float) : Niveau d'intensité sonore incident (dB)
    - Lt (float) : Niveau d'intensité sonore transmis (dB)

    Sortie : 
    - Affiche l'atténuation par absorption A en décibels (dB)
    """
    try:
        Li = float(input("Niveau d'intensité sonore incident (dB) : "))
        Lt = float(input("Niveau d'intensité sonore transmis (dB) : "))

        assert Li >= 0, "Erreur : Le niveau sonore incident doit être positif."
        assert Lt >= 0, "Erreur : Le niveau sonore transmis doit être positif."
        assert Li >= Lt, "Erreur : Le niveau sonore incident doit être supérieur ou égal au niveau sonore transmis."

        A = Li - Lt

        print("A = Li - Lt")
        print(f"\nL'atténuation par absorption est de : {A:.2f} dB\n")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except AssertionError as e:
        print(e)

def effet_doppler():
    """
    Calcul de la fréquence reçue avec l'effet Doppler, pour un observateur fixe et un émetteur mobile.

    Formule : 
    - Si la source se rapproche : f_R = f_E * (v / (v - v_S))
    - Si la source s'éloigne   : f_R = f_E * (v / (v + v_S))

    Entrée :
    - f_E (float) : Fréquence émise (Hz)
    - v (float) : Vitesse du son dans le milieu (m/s)
    - v_S (float) : Vitesse de la source sonore (m/s)
    - direction (str) : "rapproche" ou "eloigne"

    Sortie :
    - Affiche la fréquence reçue f_R (Hz)
    """
    try:
        f_E = float(input("Fréquence émise (Hz) : "))
        v = float(input("Vitesse du son dans le milieu (m/s) : "))
        v_S = float(input("Vitesse de la source sonore (m/s) : "))
        direction = input("La source se rapproche ou s'éloigne ? (rapproche/eloigne) : ").strip().lower()

        assert f_E > 0, "Erreur : La fréquence émise doit être strictement positive."
        assert v > 0, "Erreur : La vitesse du son doit être strictement positive."
        assert 0 <= v_S < v, "Erreur : La vitesse de la source doit être positive et inférieure à la vitesse du son."
        assert direction in ["rapproche", "eloigne"], "Erreur : Veuillez entrer 'rapproche' ou 'eloigne'."

        if direction == "rapproche":
            f_R = f_E * (v / (v - v_S))
        else:  # direction == "eloigne"
            f_R = f_E * (v / (v + v_S))

        print("f_R = f_E * (v / (v ± v_S))")
        print(f"\nLa fréquence reçue est de : {f_R:.2f} Hz\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except AssertionError as e:
        print(e)

def diffraction():
    """
    Calcul de l'angle de diffraction avec la longueur d'onde λ (m) et la largeur de l'ouverture a (m)
    Formule : θ ≈ λ / a

    Entrée : 
    - λ (float) : longueur d'onde λ (m)
    - a (float) : largeur de l'ouverture a (m)

    Sortie : 
    - Affiche le demi-angle de diffraction θ en radian (rad)
    """
    try:
        λ = float(input("Longueur d'onde λ (m) : "))
        a = float(input("Largeur de l'ouverture a (m) : "))

        assert λ > 0, "Erreur : La longueur d'onde doit être strictement positive."
        assert a > 0, "Erreur : La largeur de l'ouverture doit être strictement positive."

        θ = λ / a

        print("θ ≈ λ / a")
        print(f"\nLe demi-angle de diffraction est de : {θ:.2e} rad\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except AssertionError as e:
        print(e)

def tache_centrale():
    """
    Calcul de la largeur de la tache centrale en diffraction.

    Formule : L = 2 * λ * D / a

    Entrées : 
    - λ (float) : longueur d'onde (m)
    - a (float) : largeur de l'ouverture (m)
    - D (float) : distance ouverture-écran (m)

    Sortie : 
    - Affiche la largeur de la tache centrale L (m)
    """
    try:
        λ = float(input("Longueur d'onde λ (m) : "))
        a = float(input("Largeur de l'ouverture a (m) : "))
        D = float(input("Distance ouverture-écran D (m) : "))

        assert λ > 0, "Erreur : La longueur d'onde doit être strictement positive."
        assert a > 0, "Erreur : La largeur de l'ouverture doit être strictement positive."
        assert D > 0, "Erreur : La distance ouverture-écran doit être strictement positive."

        L = (2 * λ * D) / a

        print("\nRésultat :")
        print("L = 2 * λ * D / a")
        print(f"\nLa largeur de la tache centrale est de : {L:.2e} m\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except AssertionError as e:
        print(e)

# Thème 5 ÉLÉCTRICITÉ 

# Thème MATHS : 
def pythagore():
    """
    Applique le théorème de Pythagore pour calculer un côté ou l'hypoténuse.
    
    Entrées :
    - Deux longueurs connues d'un triangle rectangle (float)
    
    Sortie :
    - Affiche la longueur du côté manquant
    """
    
    print("\nThéorème de Pythagore : c² = a² + b²")

    choix = input("Voulez-vous calculer l'hypoténuse (h) ou un côté (c) ? (h/c) : ").lower()
    
    if choix == "h":
        a = float(input("Longueur du premier côté (a) : "))
        b = float(input("Longueur du deuxième côté (b) : "))
        
        assert a > 0 and b > 0, "Les longueurs doivent être positives."
        
        c = math.sqrt(a**2 + b**2)
        print(f"L'hypoténuse mesure : {c:.2f} unités")

    elif choix == "c":
        c = float(input("Longueur de l'hypoténuse (c) : "))
        b = float(input("Longueur de l'autre côté connu (b) : "))
        
        assert c > 0 and b > 0 and c > b, "L'hypoténuse doit être plus grande qu'un côté et positive."
        
        a = math.sqrt(c**2 - b**2)
        print(f"L'autre côté mesure : {a:.2f} unités")

    else:
        print("❌ Option invalide, retour au menu.")

def thales():
    """
    Applique le théorème de Thalès pour calculer une longueur inconnue.
    
    Entrées :
    - Trois longueurs connues parmi les segments proportionnels (float)
    
    Sortie :
    - Affiche la longueur manquante
    """
    
    print("\nThéorème de Thalès : AB / A'B' = AC / A'C' = BC / B'C'")

    known_values = []
    for i in range(3):
        val = input(f"Entrez la {i+1}ᵉ valeur connue (ou '?' pour l'inconnue) : ")
        known_values.append(val)

    try:
        # Trouver l'élément inconnu
        if '?' in known_values:
            index = known_values.index('?')
            known_values.remove('?')

            assert all(v.replace('.', '', 1).isdigit() for v in known_values), "Les valeurs doivent être des nombres positifs."
            
            # Convertir en float
            known_values = [float(v) for v in known_values]
            
            # Trouver la valeur manquante avec la règle de trois
            missing_value = (known_values[0] * known_values[1]) / known_values[2]
            print(f"La valeur inconnue est : {missing_value:.2f} unités")

        else:
            print("❌ Vous devez indiquer une inconnue avec '?'")

    except Exception as e:
        print(f"Erreur : {e}")