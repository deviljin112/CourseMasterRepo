# MVC-with-Flask

MVC = Model View Controller

## Tools

- HTML = Hypertext Markup Language
- CSS = Cascading Style Sheet
- JS = JavaScript
- Bootstrap = Framework

## Building our API

Display data from Python Flask to specifc API call / URL / End point

## Why Flask

- Flask is a web app framework
- Very powerful to interact with DB and user interface/browsers
- Flask can be used to create an API
- It allows us to integrate with HTML, CSS and JS
- It allows us to map HTTP Requests to Python
- It allows us to set the API path as URL to view in the browser

## How to run Flask

`pip install Flask`

- Ensure flask is installed
- How to run flask app

`flask run`

### Code Example

Importing flask into a project.

`from flask import Flask`

Initialising flask application in the project.

`app = Flask(__name__)`

Wrapping the run function.

```python
if __name__ == "__main__":
    # Runs the application
    app.run()
```

## Interacting with HTML

- Naming conventions are essential
- We need to create templates folder in our dir
- Flask looks for a templates folder and anything inside the folder
- We will create index.html inside our templates folder

## Task

- create a base.html file in templates folder
- copy index.html to base.html
- google how to extend code from base.html to index.html
- Create text boxes for login form
- search and find out syntax to write a for loop in index.html
