# System Monitoring Program

Ce projet est un moniteur système minimal qui effectue les tâches suivantes :
- Surveille les changements dans l'utilisation du CPU, l'utilisation de la RAM, l'espace disque disponible, le nombre de processus en cours d'exécution et le nombre d'utilisateurs actifs.
- Affiche les données collectées dans une belle interface web utilisant des graphiques linéaires.
- Envoie une alerte à votre adresse email lorsque certaines limites sont dépassées par le système (les limites sont entièrement configurables via le site web).
- Sauvegarde les données dans la base de données chaque semaine.
- Récupère la dernière alerte CERT et l'affiche chaque jour.

## Usage 

1. Cloner le dépôt via votre terminal :
   ```bash
   git clone https://github.com/nigonadjib/system-monitoring-program.git
   ```

2. Mettre à jour les fichiers `backup.py` et `system-data.py` avec vos paramètres email 

3. Ajouter votre mot de passe email au fichier `/etc/environment` en tant que variable d'environnement `PASSWORD` :
   ```bash
   sudo nano /etc/environment
   ```
   Ajoutez la ligne suivante :
   ```bash
   PASSWORD="votre_mot_de_passe"
   ``` a la place du mot de passe , ecrivez le sienne


5. Ajouter les lignes suivantes à votre crontab :
   ```bash
   crontab -e
   ```
   Ajoutez les lignes suivantes (en remplaçant `your_user_name` et `/path/to/project/dir/` par votre nom d'utilisateur et le chemin vers votre projet) :
   ```bash
   * *   * * * your_user_name /path/to/project/dir/data-collection.sh
   0 8   * * 1 /bin/python your_user_name /path/to/project/dir/backup.py
   0 8   * * * /bin/python your_user_name /path/to/project/dir/html-parser.py
   ```

6. Lancer le serveur :
   ```bash
   cd /chemin/vers/votre/projet
   python server.py
   ```

7. Configurer les paramètres sur le site web en accédant à l'URL où votre serveur est en cours d'exécution (par exemple, `http://localhost:5000`).

8. Et voilà ! Vous pouvez maintenant surveiller votre système.
