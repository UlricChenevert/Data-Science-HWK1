from House import House

def determinePricePerSquareFoot(house : House):
    """Calculate the price-per-square-foot for a single house.

    Args:
        house (House): A `House` object with `Price` and `SquareFoot` attributes.

    Returns:
        float: Price divided by square footage.
    """
    return house.Price / house.SquareFoot 

def determineMedianPrice (houses : list[House]):
    """Compute the median price-per-square-foot for a list of houses.

    This maps each `House` to its price-per-square-foot, sorts the resulting
    list and returns the median value. Works for even and odd lengths.

    Args:
        houses (list[House]): List of `House` objects.

    Returns:
        float: Median price-per-square-foot among the provided houses.
    """
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
    """Return parallel lists of prices and square footage from `houses`.

    Args:
        houses (list[House]): List of `House` objects.

    Returns:
        tuple[list, list]: Tuple of two lists: `(price_list, square_foot_list)`.
    """
    PriceData = map(lambda house: house.Price, houses)
    SquareFootData = map(lambda house: house.SquareFoot, houses)
    return (list(PriceData), list(SquareFootData))