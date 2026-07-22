# Simple Calculator

A basic command-line calculator built in Python.

## Branch Structure

- **main** — contains Addition (`+`) and Subtraction (`-`) only.
- **staging** — adds Multiplication (`*`) and Division (`/`) on top of main.

This structure demonstrates a common real-world workflow: `main` holds stable,
production-ready code, while `staging` holds new features being tested before
they get merged into `main`.

## How to Run

```bash
python calculator.py
```

Follow the prompts to enter two numbers and an operation.

## Operations

| Branch | Operations Supported |
|--------|------------------------|
| main | `+` `-` |
| staging | `+` `-` `*` `/` |
