# Thème 3 Energies : 
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
    print(f"La pression est de {P} Pa.")

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
        print(f"La pression est de {P} Pa.")
    elif V is None:
        V = (n * R * T) / P
        print(f"Le volume est de {V} m³.")
    elif n is None:
        n = (P * V) / (R * T)
        print(f"La quantité de matière est de {n} mol.")
    elif T is None:
        T = (P * V) / (n * R)
        print(f"La température est de {T} K.")
    else:
        print("Il faut laisser une valeur vide pour la calculer.")

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

    print(f"L'énergie totale est de {Etot} J.")

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
    print(f"La variation d'énergie interne est de {Delta_U} J.")

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
    print(f"La variation d'énergie interne est de {Delta_U} J.")

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
        print(f"{J} J = {cal} cal")
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
        print(f"Le flux thermique est de : {Φ} W")  # J/s = W

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
    print(f"La résistance thermique est de : {Rth:.2f} K.W⁻¹")

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
    print(f"Le flux thermique est de : {Φ:.2f} W")

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
    print(f"La puissance mécanique et énergétique est de : {P:.2f} W")

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
        print(f"Le rendement énergétique est de : {η_pourcentage:.2f} %")

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
        print(f"L'énergie cinétique de l'objet est de : {Ec:.2f} J")

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
        print(f"L'énergie potentielle de l'objet est de : {Ep:.2f} J")

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
        print(f"La variation de l'énergie interne du système est de : {ΔU:.2f} J")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

# Thème maths : 
import math

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