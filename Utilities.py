from House import House

def determinePricePerSquareFoot(house : House):
    return house.Price / house.SquareFoot 

def determineMedianPrice (houses : list[House]):
    pricedHouses = list(map(lambda house: determinePricePerSquareFoot(house), houses))
    pricedHouses.sort()

    length = len(pricedHouses)
    even = length % 2 == 0
    odd = not even  
    
    if (even):
        return (pricedHouses[length//2 + 1] + pricedHouses[length//2]) / 2
    if (odd):
        return pricedHouses[(length + 1)//2]

def separateHouseDataIntoTwoAxis(houses : list[House]):
    PriceData = map(lambda house: house.Price, houses)
    SquareFootData = map(lambda house: house.SquareFoot, houses)
    return (list(PriceData), list(SquareFootData))