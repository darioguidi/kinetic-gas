

def boyleEquation(p,v):
    k=p*v
    return k

def boyleEquationCostant(pressures,volumes):
    """
    Calculate Boyle's constants k for lists of pressures and volumes.
    
    Args:
        pressures (list): List of pressures.
        volumes (list): List of volumes.
        
    Returns:
        list: List of k values or raises a ValueError if inputs are invalid.
    """

    k=[]
    if len(pressures) == len(volumes):
        for i in range(len(pressures)):  
            k.append(pressures[i] * volumes[i])  
    else:
        return "Liste non valide"
    
    return k

def boyleEquationPressures(costant,volumes):
    """
    Calculate the pressures for a given Boyle's constant and a list of volumes.

    La funzione dimostra come,per una data constante K, all'aumentare del Volume diminuisce la Pressione, e viceversa

    Args:
        constant (float): The Boyle's law constant (k), calculated as pressure × volume.
        volumes (list): List of volumes for which the corresponding pressures need to be calculated.

    Returns:
        dict: A dictionary where keys start from 1, representing the index, 
              and values are the calculated pressures for each volume.

    Raises:
        ZeroDivisionError: If any volume in the list is zero.
    """

    P=[]
    for i in range(len(volumes)):
        P.append(costant/volumes[i])
    
    return P

def boyleEquationVolumes(costant,pressures):
    """
    Calculate the pressures for a given Boyle's constant and a list of volumes.

    La funzione dimostra come,per una data constante K, all'aumentare del Volume diminuisce la Pressione, e viceversa

    Args:
        constant (float): The Boyle's law constant (k), calculated as pressure × volume.
        volumes (list): List of volumes for which the corresponding pressures need to be calculated.

    Returns:
        dict: A dictionary where keys start from 1, representing the index, 
              and values are the calculated pressures for each volume.

    Raises:
        ZeroDivisionError: If any volume in the list is zero.
    """

    V=[]
    for i in range(len(pressures)):
        V.append(costant/pressures[i])
    
    return V