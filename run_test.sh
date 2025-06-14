#!/usr/bin/env bash

. .venv/bin/activate

echo "Activated virtual environment"

pytest --webdriver Firefox

return $?