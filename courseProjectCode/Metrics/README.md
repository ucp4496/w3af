Project W3AF metrics

Inside the folder coursePorjectCode/Metrics we will find all the necessary scripts to run the project metrics.

# Code Structure

## Lines of code
- To run the script to obtain the results for this metrics. You need to position yourself in /courseProjectCode/Metrics then do python (if you are using a windows) or python3 (if you are using a mac or linux) followed of the name of the script "numberOfLines.py" (e.g python numberOfLines.py)

## Comment density
- To run the script to obtain the results for this metrics. You need to position yourself in /courseProjectCode/Metrics then do python (if you are using a windows) or python3 (if you are using a mac or linux) followed of the name of the script "quantityOfComments.py" (e.g python quantityOfComments.py)

## Cyclomatic complexity
- For this metrics we need to install a library called radon. Which is a library that provide us with a lot of different metrics. In this case we are just going to use it to obtain the cyclomatic complexity. For this we need to have python previously installed with pip. We open our command prompt and then we install the library with the next command pip install radon. Once installed we can use this command to obtain the metric radon cc ./w3af -a (For this to work we need to be outside the root project)

# Test Coverage

- To run the script to obtain the results from the code coverage. For this we will install the library coverage running this command pip install coverage. Then we will position ourselves in the root directory and run python courseProjectCode/Metrics/testCoverage.py
