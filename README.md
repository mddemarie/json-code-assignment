# JSON Code Assignment

1. In a language and environment of your choice, please build a web service which turns all integers from one to a client-specified number in a JSON array.
2. Now, please write a simple client which queries the web service and prints every other number from the returned array.

## Detailed Task Explanation

#### First Task:
Create a web service as in the example below:

INPUT:

```
6
```

OUTPUT:

```
[ 1, 2, 3, 4, 5, 6 ]
```

#### Second Task:
Write a simple client which takes above returned OUTPUT and prints every 2nd number from that JSON array. Example:

INPUT:

```
[ 1, 2, 3, 4, 5, 6 ]
```

OUTPUT:

```
2
4
6
```

## SETUP

I assume you already installed Python 3.4 or higher and pip.

### Virtual Environment

Install virtualenv via pip:

```
$ pip install virtualenv
```

Create a virtual environment for a project:

```
$ cd this-project
$ virtualenv env
```

To use the virtual environment, you can activate it with:

```
$ source env/bin/activate
```

### Installation

Install the project packages including Django:

```
(env) $ pip install -r requirements.txt
```

### Run server

Only once, you have to export the FLASK_APP:

```
export FLASK_APP=app.py

```

With this command, you can run the server:

```
(venv) $ flask run
```

### In browser:

Run the local server:

```
localhost:8000/
```


