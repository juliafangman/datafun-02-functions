"""

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------
# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)


import statistics
import sys

# Descriptive: Univariant Data..................................

# univariant data (one variable, many readings)

# wins of Djokovic from the year 2023 - 2008
uni_data = [
    41,
    42,
    55,
    41,
    54,
    53,
    32,
    65,
    82,
    61,
    74,
    75,
    70,
    61,
    78,
    64
]
logger.info("uni_data = " + str(uni_data))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)

# TODO: change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var    =  {var:.2f}")
logger.info(f"stdev  =  {stdev:.2f}")
logger.info(f"lowest =  {lowest:.2f}")
logger.info(f"highest=  {highest:.2f}")


# Descriptive: Univariant Time Series Data.........................

# describe relationships
# univariant time series data (one variable over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
yvalues = [41, 42, 55, 41, 54, 53, 32, 65, 82, 61, 74, 75, 70, 61, 78, 64]

# if the lists are not the same size,
# log an error and quit the program
if len(xtimes) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xtimes)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the new correlation function from the statistics module
xx_corr = statistics.correlation(xtimes, xtimes)
xy_corr = statistics.correlation(xtimes, yvalues)

# log the information
logger.info("Here's some time series data:")
logger.info(f"xtimes:{xtimes}")
logger.info(f"yvalues:{yvalues}")
logger.info(f"correlation between xtimes and xtimes = {xx_corr:.2f}")
logger.info(f"correlation between xtimes and yvalues = {xy_corr:.2f}")

# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)

arrayX = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
arrayY = [41, 42, 55, 41, 54, 53, 32, 65, 82, 61, 74, 75, 70, 61, 78, 64]

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayX, arrayY)

# Choose an x value off in the future (future x)
future_x = 2025

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{arrayX}")
logger.info(f"y:{arrayY}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")
