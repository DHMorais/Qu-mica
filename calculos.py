from collections import defaultdict
from chemparse import parse_formula
from typing import List, Tuple, Dict, DefaultDict
from constantes import CARGAS, COMPOSTOS_IONICOS

def decompor_formula(formula: str) -> List[Tuple[str, int, int]]:
    """
    Decompõe uma fórmula química em seus íons constituintes com cargas e quantidades.
    
    Args:
        formula: Fórmula química a ser decomposta
        
    Returns:
        Lista de tuplas (íon, carga, quantidade)
        
    Raises:
        ValueError: Se a fórmula contiver íons não reconhecidos
    """
    if formula in COMPOSTOS_IONICOS:
        return COMPOSTOS_IONICOS[formula]
    
    elementos = parse_formula(formula)
    resultado = []
    
    for ion, quantidade in elementos.items():
        carga = CARGAS.get(ion)
        if carga is None:
            raise ValueError(f"Ion '{ion}' não reconhecido. Adicione ao dicionário de cargas.")
        resultado.append((ion, carga, quantidade))
    
    return resultado

def calcular_forca_ionica(lista_compostos: List[Tuple[str, float]]) -> float:
    """
    Calcula a força iônica de uma solução a partir dos compostos e concentrações.
    
    Args:
        lista_compostos: Lista de tuplas (fórmula, concentração em mol/L)
        
    Returns:
        Força iônica (µ) em mol/L
    """
    concentracoes: DefaultDict[Tuple[str, int], float] = defaultdict(float)
    
    for formula, conc in lista_compostos:
        ions = decompor_formula(formula)
        for ion, carga, quantidade in ions:
            concentracoes[(ion, carga)] += conc * quantidade
    
    mu = 0.5 * sum(conc * (z**2) for (_, z), conc in concentracoes.items())
    return mu