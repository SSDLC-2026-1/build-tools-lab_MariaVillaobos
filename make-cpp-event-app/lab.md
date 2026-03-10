# Event Ticket Validator – Make Build

## Overview


In this excercise you will work with **Make**, a widely used build tool originally designed for C and C++ projects.

The application provided is a small **event ticket validator** written in C++ that reads ticket information from a CSV file and validates whether the tickets are correct.

---

# What is Make?

**Make** is a build automation tool that helps developers compile programs efficiently.

Instead of manually compiling each file, Make uses a configuration file called a **Makefile** that defines:

- how files depend on each other
- how to compile them
- how to run additional tasks

One key advantage of Make is **incremental compilation**.

If only one file changes, Make recompiles **only the necessary files**, instead of recompiling the entire project.

---

# Project Structure

```
make-cpp-event-app/
│
├── Makefile
│
├── src/
│   ├── main.cpp
│   ├── ticket.h
│   ├── ticket.cpp
│   ├── validator.h
│   └── validator.cpp
│
├── data/
│   └── tickets.csv
│
└── bin/
```

### Description

| Folder | Purpose |
|------|------|
| src | C++ source code |
| data | input dataset containing tickets |
| bin | compiled binaries and generated files |
| Makefile | build automation configuration |

---

# Step 1 — Compile the Project

Run the following command:

```bash
make
```

Make will:

1. compile each `.cpp` file
2. generate object files (`.o`)
3. link them into the final executable

After compilation you should see:

```
bin/ticket_validator
```

---

# Step 2 — Run the Application

Execute the program using:

```bash
make run
```

Example output:

```
[VALID] TK001
[INVALID] TK002: Ticket is not active |
[VALID] TK003
[INVALID] TK004: Invalid ticket type |
[INVALID] TK005: Invalid ticket type | Ticket is not active |
[VALID] TK006

Summary
Valid tickets: 3
Invalid tickets: 3
```

---

# Step 3 — Generate a Report

The project also includes a target that generates a report file.

Run:

```bash
make report
```

This command will:

1. execute the application
2. save the output to

```
bin/report.txt
```

---

# Step 4 — Clean the Project

To remove compiled files:

```bash
make clean
```

This deletes the `bin` directory and all compiled artifacts.

---

# Lab Exercise

You will now extend the system by modifying both the **C++ code** and the **Makefile**.

The exercise contains two mini-challenges.

---

# Mini-Challenge 1 — VIP Ticket Validation

The event organizers introduced a new rule:

> VIP tickets must have a ticket number **greater than TK500**.

### Examples

Valid VIP ticket:

```
TK600,vip,active
```

Invalid VIP ticket:

```
TK200,vip,active
```

### Task

Modify the file:

```
src/validator.cpp
```

Add a validation rule that checks the numeric portion of the ticket code.

If a VIP ticket number is **500 or lower**, return the error:

```
VIP tickets must have code greater than TK500
```

### Hint

The ticket number can be extracted from the code:

```
TK123
```

Example approach:

- remove the `TK` prefix
- convert the remaining value to an integer
- compare the value

Example snippet:

```cpp
int number = stoi(ticket.code.substr(2));

if (ticket.type == "vip" && number <= 500) {
    errors.push_back("VIP tickets must have code greater than TK500");
}
```

After modifying the code, run:

```bash
make
```

Observe that **Make recompiles only the necessary files**.

---

# Mini-Challenge 2 — Create a New Make Target

We want to extend the build system with a new automation task.

Create a new target in the **Makefile** called:

```
stats
```

This target must print:

- total number of tickets in the dataset
- number of active tickets

The dataset is located in:

```
data/tickets.csv
```

### Expected behavior

Running:

```bash
make stats
```

should produce output similar to:

```
Total tickets: 6
Active tickets: 4
```

### Hint

You may use standard Linux commands such as:

```
cat
wc
grep
```

Example commands that may help:

```
cat data/tickets.csv
grep active data/tickets.csv
wc -l
```

---

# Expected Workflow

After completing the exercise the following commands should work:

Compile the project

```bash
make
```

Run the program

```bash
make run
```

Generate validation report

```bash
make report
```

Show ticket statistics

```bash
make stats
```

Clean the project

```bash
make clean
```

---

# Reflection Questions

1. Why is Make useful compared to compiling each file manually?
2. What happens if only `validator.cpp` changes?
3. Why might teams add custom targets such as `report` or `stats` to a Makefile?

---

# Bonus Challenge (Optional)

Modify the `report` target so that it also prints the report summary to the console while saving it to `report.txt`.