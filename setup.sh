#!/bin/bash

PLUGINS_DIR="$HOME"/bitbar

#cp -n "$PWD"/.bitbarrc "${PLUGINS_DIR}"/.bitbarrc

PLUGINS=(py/livedoor-weather.3h.py)
for plugin in "${PLUGINS[@]}"; do
  ln -fs "$PWD"/plugins/"$plugin" "$PLUGINS_DIR"/
done
