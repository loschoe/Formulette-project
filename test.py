from mendeleev import element
import re

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
        
        mass = elem.mass  # Utilisation de elem.mass au lieu de elem.atomic_weight
        
        count = int(count) if count else 1
        molar_mass += mass * count
    
    assert molar_mass > 0, "La masse molaire doit être strictement positive."
    
    return molar_mass

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
        print(f"La quantité de matière est de {quantite_matiere:.5f} mol.")
    
    except ValueError as e:
        print(f"Erreur : {e}")

calcul_quantite_matiere()
