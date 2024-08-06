# my-first-app-inclass-summer-2024

## Setup

Create virtual environment:

```sh
conda create -n ump-env python=3.11
```

Activate the environment:

```sh
conda activate ump-env
```

Install packages:

```sh
#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```

## Usage

Run the script:

```sh
# python app/unemployment.py

# equivalent:
python -m app.unemployment
```

## Testing

Run tests:

```sh
pytest
```
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
