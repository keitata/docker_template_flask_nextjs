#!/bin/bash
set -eux

# wait database
timeout 15 bash -c 'while ! >/dev/tcp/postgres/5432; do sleep 1; done'

# TODO : deploy https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/deploy.html
# TODO : --host=0.0.0.0
# TODO : --debug hotreload on
exec flask --app app run --host=0.0.0.0 --debug
