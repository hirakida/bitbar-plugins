#!/bin/bash

PLUGINS_DIR="$HOME"/bitbar

cp "$PWD"/.bitbarrc "${PLUGINS_DIR}"/.bitbarrc

PLUGINS=(ip.3h.py livedoor-weather.3h.py)
for plugin in "${PLUGINS[@]}"; do
  ln -fs "$PWD"/plugins/"$plugin" "$PLUGINS_DIR"/"$plugin"
done
