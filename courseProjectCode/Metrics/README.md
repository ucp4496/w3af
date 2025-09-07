# **Project W3AF metrics**

Inside the folder coursePorjectCode/Metrics we will find all the necessary scripts to run the project metrics.

# Code Structure

## Lines of code
1. Open your terminal or command prompt.
2. Navigate to the folder:
3. Run the script:

- If you are using **Windows**:

  ```
  python numberOfLines.py
  ```

- If you are using **macOS** or **Linux**:

  ```
  python3 numberOfLines.py
  ```

> Replace `numberOfLines.py` with the actual script name if different.

## Comment density
1. Open your terminal or command prompt.
2. Navigate to the folder:
3. Run the script:

- If you are using **Windows**:

  ```
  python quantityOfComments.py
  ```

- If you are using **macOS** or **Linux**:

  ```
  python3 quantityOfComments.py
  ```

> Replace `quantityOfComments.py` with the actual script name if different.


## Cyclomatic complexity
1. Make sure Python and pip are installed on your system.
2. Open your command prompt or terminal.
3. Install Radon by running:

  ```
  pip install radon
  ```

4. After the installation, run Radon to get the cyclomatic complexity metric:

  ```
  radon cc ./w3af -a
  ```

5. Run the above command **outside** the root project folder `w3af`.

>Radon provides many code metrics, and here we use it to calculate cyclomatic complexity.

# Test Coverage

1. Make sure you have Python and pip installed.
2. Open your terminal or command prompt.
3. Install the coverage library by running:

  ```
  pip install coverage
  ```

4. Navigate to the root directory of your project.
5. Run the coverage script with this command:

  ```
  python courseProjectCode/Metrics/testCoverage.py
  ```

> Replace `python` with `python3` if you are on macOS or Linux and your system requires it.