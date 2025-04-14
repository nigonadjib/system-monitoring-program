#!/bin/bash

# Définir le répertoire courant
script_dir="$(dirname "$0")"

# Exécuter les scripts sans utiliser de chemin absolu
python "$script_dir/system-data.py"
bash "$script_dir/network-data.sh"
