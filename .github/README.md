# The Meh-thematical Calculator

A sarcastic command-line calculator that performs basic math operations
but isn't very nice about it. The calculator responds with snarky and
humorous remarks when you make mistakes.

------------------------------------------------------------------------

## Features

-   Addition
-   Subtraction
-   Multiplication
-   Division (with a special insult for dividing by zero)
-   Power (exponentiation)
-   Error tracking with escalating insults if you provide invalid inputs

------------------------------------------------------------------------

## How It Works

1.  The program greets the user sarcastically.
2.  It asks what operation you want to perform (`add`, `subtract`,
    `multiply`, `divide`, or `power`).
3.  You enter two numbers.
4.  The calculator performs the operation and displays the result.
5.  If you mess up too many times (3 invalid inputs), the calculator
    rage-quits on you.>

------------------------------------------------------------------------

## Flowchart

``` mermaid
flowchart TD
    A[Start Program] --> B[Print Intro]
    B --> C[Ask for Operation]
    C -->|Valid Input| D[Ask for First Number]
    D --> E[Ask for Second Number]
    E --> F{Which Operation?}
    F -->|Add| G[Perform Addition]
    F -->|Subtract| H[Perform Subtraction]
    F -->|Multiply| I[Perform Multiplication]
    F -->|Divide| J[Perform Division]
    F -->|Power| K[Perform Power]

    G --> L[Print Result]
    H --> L
    I --> L
    J --> L
    K --> L

    L --> C

    C -->|Invalid Input| M[Increase Error Count]
    M --> N{Errors < 3?}
    N -->|Yes| O[Print Insult]
    O --> C
    N -->|No| P[Exit Program with Rage]
```

------------------------------------------------------------------------

## Testing
Run this command in the directory of the repo
```bash
pytest
```

## Usage

Run the script with Python:

``` bash
python calculator.py
```

Then follow the on-screen instructions (if you can handle the insults).