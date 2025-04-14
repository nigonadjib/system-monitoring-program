Voici les commandes pour chaque étape que vous avez mentionnée :

### Étape 1 : Cloner le dépôt
```bash
git clone https://github.com/badiealili/system-monitoring-program.git
```

### Étape 2 : Mettre à jour les fichiers `backup.py` et `system-data.py`
Ouvrez les fichiers avec un éditeur de texte (par exemple, `nano` ou `vim`) et mettez à jour les paramètres de votre email.

```bash
nano /chemin/vers/votre/projet/backup.py
```
```bash
nano /chemin/vers/votre/projet/system-data.py
```
(Remplacez `/chemin/vers/votre/projet/` par le chemin réel vers votre projet.)

### Étape 3 : Ajouter votre mot de passe email au fichier `/etc/environment`
Ouvrez le fichier `/etc/environment` avec des privilèges d'administrateur.

```bash
sudo nano /etc/environment
```
Ajoutez la ligne suivante :
```bash
PASSWORD="votre_mot_de_passe"
```
(Remplacez `votre_mot_de_passe` par votre mot de passe réel.)

### Étape 4 : Mettre à jour la variable de chemin
Vous devrez modifier les fichiers de votre projet pour mettre à jour les chemins. Utilisez un éditeur de texte pour ouvrir chaque fichier et mettre à jour les chemins.

```bash
nano /chemin/vers/votre/projet/backup.py
```
```bash
nano /chemin/vers/votre/projet/system-data.py
```
```bash
nano /chemin/vers/votre/projet/data-visualizer.py
```
(Assurez-vous de mettre à jour tous les chemins nécessaires dans chaque fichier.)

### Étape 5 : Ajouter les lignes à votre crontab
Ouvrez votre crontab pour l'édition.
```bash
crontab -e
```
Ajoutez les lignes suivantes (en remplaçant `your_user_name` et `/path/to/project/dir/` par votre nom d'utilisateur et le chemin vers votre projet) :
```bash
* *   * * * your_user_name /path/to/project/dir/data-collection.sh
0 8   * * 1 /bin/python your_user_name /path/to/project/dir/backup.py
0 8   * * * /bin/python your_user_name /path/to/project/dir/html-parser.py
```

### Étape 6 : Lancer le serveur
Accédez au répertoire de votre projet et lancez le serveur.
```bash
cd /chemin/vers/votre/projet
python server.py
```

### Étape 7 : Configurer les paramètres sur le site web
Ouvrez votre navigateur et accédez à l'URL où votre serveur est en cours d'exécution (par exemple, `http://localhost:5000` ou l'adresse IP de votre serveur).

### Étape 8 : Vérifier que tout fonctionne
Assurez-vous que le système est surveillé et que les alertes fonctionnent comme prévu.

### Remarque
Assurez-vous de remplacer tous les chemins et noms d'utilisateur par ceux qui correspondent à votre configuration.
