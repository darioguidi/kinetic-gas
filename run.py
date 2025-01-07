

from src.calculation.boyle import boyleEquation, boyleEquationCostant, boyleEquationPressures, boyleEquationVolumes

def main():

    volumes = [4, 3, 2]
    costant=10

    pressures=boyleEquationPressures(costant, volumes)
    costant2=boyleEquationCostant(pressures, volumes)

    print(costant2, volumes)

if __name__=="__main__":
    main()