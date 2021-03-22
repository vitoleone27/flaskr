# Flaskr

The basic blog app built in the [Flask tutorial](https://flask.palletsprojects.com/tutorial/)


## Install

Create a virtualenv and activate it

```
python3 -m venv .venv
source .venv/bin/activate
```

## Install Flaskr

```
pip install -e .
```

## Run

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask init-db
flask run
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.
