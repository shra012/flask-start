#!/bin/bash
#set -x
if [[ -z "${VIRTUAL_ENV}" ]]; then
    source /Users/hiruzen/.local/share/virtualenvs/flask-start-1xhaTWo_/bin/activate
fi
export FLASK_APP=app.py
export FLASK_ENV=development
export OAUTHLIB_INSECURE_TRANSPORT=True
export OAUTHLIB_RELAX_TOKEN_SCOPE=True
flask run