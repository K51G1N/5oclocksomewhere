# 5 o'clock somwhere

People always say it's 5 o'clock somewhere, but where is that place?
Well with this app it'll tell you where it's currently in it's 17th hour (between 5pm-5:59pm)
## Introduction

This application combines a React front-end with a Python Flask back-end to provide a unique feature. Users can click the "Get Random Location" button, which then results in a country and time being displayed.

The Flask server, powered by Python, runs an `app.py` script, which leverages the logic from `main.py`. The server's functionality is to select a random location within a timezone corresponding to the 17th hour (5 PM).

## Getting Started

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Prerequisites

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- Flask (installed in your Python environment)
- Other project dependencies (installed using `npm install`)

### Installation

create a virtual environment
```python -m venv .venv```

install the requirements
```> pip install requirements.txt```

In 5oclock_py
```flask run```


Use npm to install the project dependencies:
In 5o_clock_somewhere_ui
```npm install```

get it up and running 
```npm start```