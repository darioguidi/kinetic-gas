from src.calculation.boyle import boyleEquationCostant,boyleEquationPressures,boyleEquation

def main():
    pressures = [10, 20, 30]
    volumes = [4, 3, 2]

    costant=10

    print(boyleEquationCostant(pressures, volumes))

    print(boyleEquationPressures(costant, volumes))
    
    print(boyleEquationCostant(boyleEquationPressures(costant, volumes), volumes))

if __name__=="__main__":
    main()