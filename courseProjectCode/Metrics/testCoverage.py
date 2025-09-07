import unittest
import coverage
import warnings
import io

warnings.filterwarnings("ignore", category=SyntaxWarning)

def count_tests_and_suites():
    loader = unittest.TestLoader()
    suite = loader.discover("../w3af")

    num_cases = suite.countTestCases()

    classes = set()
    def findSuites(suite):
        for test in suite:
            if isinstance(test, unittest.TestSuite):
                findSuites(test)
            else:
                classes.add(test.__class__)

    findSuites(suite)

    num_suites = len(classes)

    return num_cases, num_suites


def run_coverage():
    cov = coverage.Coverage()
    cov.start()

    buf = io.StringIO()
    runner = unittest.TextTestRunner(stream=buf, verbosity=2)
    result = runner.run(unittest.defaultTestLoader.discover("../w3af"))

    cov.stop()
    cov.save()

    total_percent = cov.report(show_missing=False, skip_covered=True, file=io.StringIO())

    print("Test Coverage: " + str(total_percent)[0:5] + "%")


if __name__ == "__main__":
    num_cases, num_suites = count_tests_and_suites()
    print("Number of Unit tests: " + str(num_cases))
    print("Number of Test suites: " + str(num_suites))

    run_coverage()
    print()
