# SoftDesk
**_Projet réalisé lors de ma formation de Développeur d'application Python à OpenClassrooms_**

_**L'API SoftDesk dispose de deux applications codées en Python avec Django Rest framwork:**_
1. userAccount
1. helpdesk

_**Les données sont enregistrées dans la base de données db.sqlite3**_

## Installation

* Python 3.9.1 doit être installé.
* Téléchargez le package d'application depuis github, décompressez-le et stockez-le dans un nouveau répertoire.
* Ouvrez un nouveau terminal  dans ce répertoire avec la commande.
* Créer un environnement virtuel `python -m venv env`
* Activer l'environnement virtuel `env\Scripts\activate.bat`
* Installez la dernière version de pip `python -m pip install --upgrade pip`
* Installez les packages Python externes avec `pip install -r requirements.txt`

## Utilisation

* Activer l'environnement virtuel `env\Scripts\activate.bat`
* Exécutez le serveur de fichiers `python manage.py runserver`
* Dans votre  navigateur web, accédez à l'API à l'URL `http:/127.0.0.1:8000`
* L'application a été testée avec Postman.
* Créez un compte pour pouvoir vous connecter.
* Le mot de passe doit contenir au moins 8 caractères, chiffres dans le désordre et lettres. Ça ne doit pas être courant.
* Accédez à la gestion de la base de données d'administration `http://127.0.0.1:8000/admin`


* Pour créer un nouveau compte administrateur `python manage.py createsuperuser`

Postman documentation : https://documenter.getpostman.com/view/19526082/UVsJvmDu


