# Event Registration Validator – Ant Build Lab

## Overview

In this laboratory you will explore how **build automation tools** help developers automate repetitive tasks such as:

- running applications
- executing tests
- validating data
- generating artifacts
- packaging software

You will work with **Apache Ant** to automate the build process of a small Python application that validates event attendees.

---

# Project Structure

```
ant-python-event-app/
│
├── build.xml
├── README.md
│
├── src/
│   ├── app.py
│   └── validator.py
│
├── tests/
│   └── test_validator.py
│
├── data/
│   └── attendees.json
│
└── dist/
```



# Step 1 — Run the Application Manually

Before using a build tool, developers usually execute programs manually.

Run the application with:

```bash
python3 src/app.py
```

The application will:

1. Load the attendee data from `data/attendees.json`
2. Validate each attendee
3. Print the validation results
4. Show a summary of valid and invalid records

Example output:

```
[VALID] Laura
[INVALID] Pedro: ['Invalid email']

Summary
Valid attendees: 1
Invalid attendees: 1
```

---

# Step 2 — Run the Unit Tests

Unit tests verify that the validation logic behaves correctly.

Execute the tests using:

```bash
python3 -m unittest discover -s tests
```

Expected output:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

The tests validate functions defined in `validator.py`.

---

# Step 3 — Using Ant

Ant automates repetitive development tasks such as testing and packaging.

The project contains a `build.xml` file that defines several **targets**.

A **target** represents a task in the build process.

---

## Run the Tests with Ant

Instead of running tests manually:

```bash
ant test
```

Ant will execute the same command automatically.

---

## Run the Application with Ant

```bash
ant run
```

This executes the Python application defined in the `run` target.

---

## Package the Project

```bash
ant package
```

This target will:

1. clean the output directory
2. run unit tests
3. create a `.zip` package inside the `dist/` folder

---

# Exercise

You will now extend the application and the build process.


---

# 1. Add a User Identifier Validation

Each attendee must now include a **registration identifier**.

The identifier must follow this format:

```
EV-XXXX
```

Where:

- `EV-` is a fixed prefix
- `XXXX` represents **exactly four digits**

### Valid examples

```
EV-1023
EV-0001
EV-9876
```

### Invalid examples

```
EV1023
EV-12
EV-ABCDE
AB-1234
```

### Task

Modify the file:

```
src/validator.py
```

Add validation logic for:

```
registration_code
```

If the identifier is invalid, the system must return the error:

```
Invalid registration code
```

---

# 2. Add a New Unit Test

Update the file:

```
tests/test_validator.py
```

Add at least **one new test case** that verifies:

- a valid registration code
- an invalid registration code

Example cases:

```
EV-1234  → valid
EV-12    → invalid
```

Run the tests again:

```bash
python3 -m unittest discover -s tests
```

or

```bash
ant test
```

All tests should pass.

---

# 3. Generate a Validation Report with Ant

We now want the build system to generate a **report file** containing the validation results.

### Task

Modify the file:

```
build.xml
```

Create a new target called:

```
report
```

This target must:

1. create the `dist/` directory if it does not exist
2. execute the application
3. save the output into a file called

```
dist/report.txt
```

### Expected behavior

Running:

```bash
ant report
```

should generate:

```
dist/report.txt
```

containing the validation results produced by the application.

---

# Expected Workflow

After completing the exercise, the following commands should work.

Run tests

```bash
ant test
```

Run the application

```bash
ant run
```

Generate validation report

```bash
ant report
```

Package the project

```bash
ant package
```


# Bonus Challenge (Optional)

Modify the `package` target so that the generated `report.txt` file is included in the final `.zip` package.

g++ -Wall -Wextra -std=c++17 -c src/main.cpp -o bin/main.o
g++ -Wall -Wextra -std=c++17 -c src/ticket.cpp -o bin/ticket.o
g++ -Wall -Wextra -std=c++17 -c src/validator.cpp -o bin/validator.o
g++ bin/main.o bin/ticket.o bin/validator.o -o bin/ticket_validator