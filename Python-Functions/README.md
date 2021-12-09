# Functions

## What are functions

DRY = Don't Repeat yourself.
</br>

- Removes repeated code.
- Allows a function to handle data dynamically.
- Breaks down the code into managable / readable blocks.
- Improves efficiency as functions are stored in RAM therefore on another call will run from RAM rather than load the function again.
- Allows for ease of handling data and data manipulation.
</br>
Syntax:

```python
def name_of_function(input):
```

Input is not essential function can have no input

### Returns

A `return` statement is used at the end of a function so that the block that called the function has access to the final value that was modified by the function.
</br>
This allows a variable to be assigned to the function and that variable will store the value returned by that function.
</br>
Example:

```python
def addition(val_1, val_2):
    return val_1 + val_2


print(addition(2, 2))
```

## Best Practices

- Have small block of any function that does one job
- Pseudo coding = one line of explanation
- Create hints in simple bullet points
- Comments regarding your function results

## Tasks

Available: [here](tasks.py)

- Create a multiplication function
- Create a division function
- Create a modulus function
- Create a to the power of function
