class House:
    """Simple data container representing a house.

    Attributes:
        SquareFoot (int): Size of the house in square feet.
        Price (float): Price of the house in currency units.
    """
    def __init__(self, SquareFoot : int, Price: float):
        """Initialize a `House` instance.

        Args:
            SquareFoot (int): The house's square footage.
            Price (float): The house's price.
        """
        self.SquareFoot = SquareFoot
        self.Price = Price
