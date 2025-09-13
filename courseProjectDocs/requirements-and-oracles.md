# Requirements and Test Oracles

## Functional Requirements
1. The tool must let the user choose which types of scans to run (Like find URLs, test for problems or try attacks)
2. It must find common web problems like SQL injection, cross-site scripting and command injection
3. It must be able to scan websites automatically after the user sets the target URL

## Non Functional Requirements
1. The tool must run on Linux and Windows
2. It should run efficiently
3. It should keep user and scan data secure

## Test Oracles
|Requirement    |Description                                                    |Test Oracle
|---------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------
|FR1            |Let the user choose types of scans                             |After selection, only chosen scans run
|FR2            |Find SQL, XSS and command injections bugs                      |Reports know bugs accurately
|FR3            |Scan auto after user sets URL                                  |Scan runs and complete with report
|NFR1           |Runs on Linux and Windows                                      |Install and runs on both OS without erros
|NFR2           |Runs efficiently                                               |Completes scans in reasonable time, no crashes
|NFR3           |Keeps scan data and user information safe                      |No data leaks, encrypts sensitive data