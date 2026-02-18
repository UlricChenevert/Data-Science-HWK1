import matplotlib


def displayPrices(plot : matplotlib.pyplot, officialMedian : int, scrappedMedian : int, difference : int, priceData : list[int], squareFootDat : list[int]):
    fig, axis = plot.subplots()
    fig.text(0.05, 0.9, f"Official Median: {officialMedian} Scrapped Median: {scrappedMedian} \nDifference: {difference}", fontsize=12)
    axis.scatter(priceData, squareFootDat, facecolor = 'r') 
    axis.set_xlabel('Prices')
    axis.set_ylabel('Square Feet')
    plot.show()   