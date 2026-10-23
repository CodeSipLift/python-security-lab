# Learning Log

## Day 1 - Host Reconnaissance Utility
### What I built
Created a Python command-line utility that resolves a hostname to an IPv4 address using the socket module.
### What I learned
- How to import and use Python's built-in `socket` module.
- How to store user input and function return values in variables.
- How to call methods and functions.
- How to handle exceptions with `try`, `except`, and `else`.
- How to use `argparse` to accept command-line arguments.
- How to test success, failure, and missing-input cases.
- How to review changes with `git diff` before committing.
- How to use dictionaries to organize results as key-value pairs.
- How to convert dictionaries into JSON with `json.dumps()`.
- Why structured output makes the results easier for other programs to process.
- How to use the exit codes to signal success (`0`) or failure (`1`).
- How to check exit codes in Windows CMD using `echo %ERRORLEVEL%`.


### Day 2 - Testing command-line behavior
- Verified successful hostname resolution produces JSON and exit code 0.
- Verified an unresolvable hostname produces an error in JSON and exit code 1.
- Verified a missing hostname causes argparse to display a usage error and exit code 2.
- Learned that exit codes let other tools distinguish success from different failures.
