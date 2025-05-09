# Dicionário de cargas
CARGAS = {
    # Cátions
    "Na": +1, "K": +1, "NH4": +1, "H": +1,
    "Ca": +2, "Mg": +2, "Ba": +2, "Fe": +2, "Cu": +2,
    "Al": +3, "Fe3": +3,
    # Ânions
    "Cl": -1, "Br": -1, "I": -1, "NO3": -1, "HCO3": -1,
    "OH": -1, "CH3COO": -1, "CN": -1,
    "SO4": -2, "CO3": -2, "S": -2,
    "PO4": -3
}

# Compostos predefinidos
COMPOSTOS_IONICOS = {
    "NaCl": [("Na", +1, 1), ("Cl", -1, 1)],
    "CaCl2": [("Ca", +2, 1), ("Cl", -1, 2)],
    "Na2SO4": [("Na", +1, 2), ("SO4", -2, 1)],
    "MgCl2": [("Mg", +2, 1), ("Cl", -1, 2)],
    "Al2(SO4)3": [("Al", +3, 2), ("SO4", -2, 3)],
    "FeCl3": [("Fe3", +3, 1), ("Cl", -1, 3)],
    "FeSO4": [("Fe", +2, 1), ("SO4", -2, 1)],
    "Cu(NO3)2": [("Cu", +2, 1), ("NO3", -1, 2)],
    "NaNO3": [("Na", +1, 1), ("NO3", -1, 1)],
    "NaOH": [("Na", +1, 1), ("OH", -1, 1)],
    "NH4Cl": [("NH4", +1, 1), ("Cl", -1, 1)],
    "NH4OH": [("NH4", +1, 1), ("OH", -1, 1)],
}