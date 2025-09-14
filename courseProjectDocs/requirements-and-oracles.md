# Requirements and Test Oracles

## Functional Requirements
1. The tool must let the user choose which types of scans to run (Like find URLs, test for problems or try attacks)
2. It must find common web problems like SQL injection, cross-site scripting and command injection
3. It must be able to scan websites automatically after the user sets the target URL
4. The Program shall be given a command for audit plugins and will view, enable or configure those same plugins.
5. The Program shall give detailed reports based on its scans in various formats.
6. The program shall allow the user to save scan and plugin configurations.
7. The program shall support running inside of a Docker container.

## Non Functional Requirements
1. The tool must run on Linux and Windows
2. It should run efficiently
3. It should keep user and scan data secure
4. The Program should be able to scan both small and large web apps
5. It should be reliable, with a low rate of false positives and false negatives

## Test Oracles
|Requirement    |Description                                                    |Test Oracle
|---------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------
|FR1            |Let the user choose types of scans                             |After selection, only chosen scans run
|FR2            |Find SQL, XSS and command injections bugs                      |Reports know bugs accurately
|FR3            |Scan auto after user sets URL                                  |Scan runs and complete with report
|FR4            |Scan an already clean website                                  |Report should have no major vulnerablities
|FR5            |Activate the plugin update system                              |Checks for updates and applies them without errors
|FR6            |Let user save scan and plugin config                           |If a user saves their configuration and reloads, the same scan configuration and plugins are used.
|FR7            |Runs inside of docker                                          |If the scanner is running inside a docker container, behavior is identical to if it was running locally.
|NFR1           |Runs on Linux and Windows                                      |Install and runs on both OS without errors
|NFR2           |Runs efficiently                                               |Completes scans in reasonable time, no crashes
|NFR3           |Keeps scan data and user information safe                      |No data leaks, encrypts sensitive data
|NFR4           |Scans small and large web apps                                 |Behavior is identical and accurate when scanning small and large web apps
|NFR4           |Results are reliable                                           |When testing an app with known vulnerabilities, the known vulnerabilities should be displayed, and non-vulnerabilities should not
