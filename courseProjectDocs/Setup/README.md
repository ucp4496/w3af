# Explanation on how to run the tests
We have tried multiple approaches to run the project. The first was attempting to install the dependencies on Linux environments like Kali and Ubuntu. Due to library errors, incompatibilities, and the deprecation of many essential dependencies for w3af, running the project using this method proved impossible.

The second approach involved using the various Dockerfiles provided within the project to run a Docker image. According to the documentation, there was an option to run a pre-built Docker image included in the project. However, this image also failed to work. Docker returned an error indicating that the image owner needs to update the image because it is no longer compatible or usable.

The third method was to build a Docker image directly from the project source. Again, this was unsuccessful due to library incompatibilities—particularly with the lxml and paperclip dependencies. The lxml package was the primary source of problems because even the latest version made for Python 2 (3.4.4) is outdated and incompatible with newer Python 2 versions and system libraries. Additionally, while the project was originally developed targeting Linux, much of the code still uses Python 2, which is deprecated.

We attempted numerous combinations of dependency versions to get the project running, but despite all efforts, it was not possible. Through further research, we discovered that the project itself is deprecated. A successor project called w4af now aims to continue its development.

# Document enviroment setup
There are many ways to run the project but none of them work:
## Enviroments and tools must needed to run the project
- A Linux enviroment
- Python2 (2.7.18)
- All the dependencies which are going to be provided later

1. First path
    - Clone the project ```git clone https://github.com/andresriancho/w3af.git```
    - Position yourself in ```cd w3af```
    - Run the project by doing ```./w3af_console```
    - If there is a error this is normal. By reading it is going to tell you that it generate a bash file with the dependencies that are missing
    - The file should be located in ```/tmp/w3af_dependency_install.sh``` you need to be located there (In case it isn't use the route provided by the error in the step before)
    - Run the bash file using ```./w3af_dependency_install.sh```
    - Go back to the folder w3af and run the command ```./w3af_console```
    - After that the project should run. In case this is not the case review the dependencies compatibility with python2

2. Second path
    - Inside the folder w3af is a folder called extras. We will ```cd extras```
    - Once there we are going to see another folder called scripts which will contain w3af_console_docker
    - With this file we are going to attemp to run the project directly in docker without installing any dependencies
    - Run ```./w3af_console_docker```
    - This will create the docker container which will run the w3af

3. Thrid path
    - Inside w3af there is a folder called extras, inside this folder we will find another file called docker
    - It will contain bash scripts which will create directly the whole container with everything needed for w3af
    - We will run this command ```./docker-build-local.sh```

* Note: None of these paths work to run the project. Because of this problems it was impossible to run the code coverage. Despite this problem we try to analyze the project by reading the code (This is just an aproximation)

## w3af test suite (Aproximate)
- Unit tests: These cover individual functions and classes within the core modules and plugins, mainly to validate plugin and utility functions
- Interagration tests: These test the interaction between multiple modules or plugins, ensuring that data flows correctly during scans
- System tests: Simulated or partial real scans that check end to end functionality of the scanner pipeline and reporting
- UI Test: Minimal or none, since w3af's primary interfaces are console based and basic GUI with little automated UI coverage (I think here is a based UI version but we couldn't provide information because it was not possible to run the project)

## Test coverage metrics (Aproximate)
- Number of tests: Using pytest we found 518 tests.
- Test passed: None
- Test failed: 100% of the tests did not pass due to failed deployment. Additionally, we speculate that many of the tests would fail because the project has been unmaintained for a long time.
- Coverage summary: None

# Observations
- The project is deprecated, obsolete, and abandoned.
- It was not possible to run the tests, but an approximation and analysis were performed by reading several test code files.
- Information was also gathered about the modules used to generate these tests to understand the testing scope intended by the w3af developers.
- The official project documentation does not explicitly state that the project is deprecated, however, the repository has not been updated for many years.
- Additionally, all tools used, including Python 2 and dependencies, have been deprecated or updated to Python 3.
- Many companies and projects are migrating to Python 3 in 2025 due to security risks and end-of-life of Python 2, which was discontinued in 2019-2020.
- This causes severe security issues and risks due to abandoned and unsupported code.
- This project should not be used in production environments.
- Other reasons why running w3af is currently very difficult or impossible:
    - Dependencies and environment settings are incompatible with modern systems.
    - Running tests or the framework itself is dependent on legacy configurations and external services.
    - The only feasible way to run it is via Docker, but recent Docker versions do not support the legacy Dockerfiles designed for w3af.