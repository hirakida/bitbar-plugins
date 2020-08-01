#!/bin/bash

PLUGINS_DIR="$HOME"/bitbar

PLUGINS=(livedoor-weather.3h.py)
for plugin in "${PLUGINS[@]}"; do
  ln -fs "$PWD"/plugins/"$plugin" "$PLUGINS_DIR"/
done
