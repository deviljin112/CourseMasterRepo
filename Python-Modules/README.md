# Python Modules

- Built in functions
- PyPi Library
- What is `pip`
  - Package Manager for Python
  - Used to install external packages
- How to use `pip`
  - `pip install <package_name>`
- APIs with Python

## Lesson breakdown

- [OS Module](os_module.py)
- [Math and Random](math_and_random.py)
- [JSON Module](json_module.py)
- [HTTP Requests](http_requests.py)
- [Exception Handling](exception_handling.py)

### Tasks

- [PostCode Task](postcode_task.py)
- [PostCode All Data Task](postcode_alldata.py)
- [Exception Handling and JSON](Exception_handling_task.py)

## PIP

- Package manager for Python that helps us install external packages such as `requests`
- Syntax: pip install <package_name>

## Requests

- Local host makes an API call to a www server
  - To find out if the web is live
  - To handle the user as per the response from the web
  - Meeting the user's expectation

## CRUD

- Create
- Read
- Update
- Delete

## JSON

- Java Script Object Notation
- Dictionary-based language
- Use cases
  - Browser data
  - Key-Value Data
  - Dictionary to Json Encoding / Decoding
  - Persistent data
- Handling / Creating files with python
- Writing to a file
- Reading from a file

## Handling files and premissions

| Mode | Description                                                                    |
| ---- | ------------------------------------------------------------------------------ |
| "r"  | Default mode. Used for just reading files                                      |
| "w"  | Write permissions. Used to Update/Write into a file.                           |
| "x"  | Creates a new file. Fails if exists                                            |
| "a"  | Appends into a file (adds to the end). If file doesn't exist creates a new one |
| "t"  | Text mode. Default mode similar to read                                        |
| "b"  | Binary mode.                                                                   |
| "+"  | This will open the file for reading and writing                                |

## Exception Handling

Used when we expect an error from python interpreter.

- `try:`
  - Attempts to execute the code block
- `except:`
  - If the Try code block raises an error perform this block instead
- `else:`
  - If there is no issue, execute this block after Try:
- `finally:`
  - Regardless of above result execute this block
- `raise Exception("<message>")`
  - Raises a custom error, for controlled error calls

### Iteration 1

Simple error handling, with uninteresting feedback message. Not relevant or specific.

```python
try:
    some_file = open("orders.text")
except:
    print("There was an error!")
```

### Iteration 2

Much more explicit error handling, with specfic error message and handling specific error codes. Lots of user feedback for the user to be able to identify the issue.

```python
# Use try block when we know there might be an error
try:
    file_data = open("orders.text")  # => Error

# Catch the specific error and print a custom message
except FileNotFoundError as error_msg:  # Alias the error message to a variable
    print(f"File does not exist!\n{error_msg}")

# If there is no error do something with that variable
else:
    print(file_data)

# Regardless of the above result, always run this block at the end
finally:
    print("End of function")
```
