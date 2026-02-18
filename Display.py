import matplotlib


def displayPrices(plot : matplotlib.pyplot, officialMedian : int, scrappedMedian : int, difference : int, priceData : list[int], squareFootDat : list[int]):
    """Render a scatter plot of house prices vs. square footage.

    Creates a figure, adds a summary text showing official and scraped medians
    plus their difference, then plots `priceData` vs `squareFootDat` as red
    markers and shows the plot window.

    Args:
        plot (matplotlib.pyplot): The pyplot module (usually imported as ``plot``).
        officialMedian (int): Official median price-per-square-foot.
        scrappedMedian (int): Median computed from scraped data.
        difference (int): Difference between official and scraped medians.
        priceData (list[int]): Prices for the x-axis.
        squareFootDat (list[int]): Square feet for the y-axis.
    """
    fig, axis = plot.subplots()
    fig.text(0.05, 0.9, f"Official Median: {officialMedian} Scrapped Median: {scrappedMedian} \nDifference: {difference}", fontsize=12)
    axis.scatter(priceData, squareFootDat, facecolor = 'r') 
    axis.set_xlabel('Prices')
    axis.set_ylabel('Square Feet')
    plot.show()