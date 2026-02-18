import matplotlib.pyplot as plot
import Data
from Display import displayPrices
from Utilities import determineMedianPrice, separateHouseDataIntoTwoAxis

scrappedMedian = round(determineMedianPrice(Data.scrapedHouseData), 2)
differenceBetweenOfficialAndScrappedData = round(Data.officialMedian - scrappedMedian, 2)

PriceData, SquareFootData = separateHouseDataIntoTwoAxis(Data.scrapedHouseData)

displayPrices(
    plot, 
    Data.officialMedian, scrappedMedian, differenceBetweenOfficialAndScrappedData, 
    PriceData, SquareFootData
    )