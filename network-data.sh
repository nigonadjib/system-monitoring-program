#!/bin/bash

# Récupérer l'adresse IP publique
public_ip=$(curl -s ifconfig.me)

# Récupérer l'adresse MAC
mac_address=$(ifconfig wlan0 | grep -o -E '([0-9a-fA-F]{2}:){5}([0-9a-fA-F]{2})')

# Nom de la table
table_name="Sondes"

# Définir le répertoire courant
DB_DIR="$(dirname "$0")"
DB_FILE="$DB_DIR/data.db"

# Requête SQL pour mettre à jour la base de données
QUERY="UPDATE \"$table_name\" SET Public_IP_Address = \"$public_ip\", MAC_Address = \"$mac_address\" WHERE Timestamp = (SELECT MAX(Timestamp) FROM \"$table_name\");"

# Exécuter la requête SQL
sqlite3 "$DB_FILE" "$QUERY"
