<H1> Openfoodfact - Site Web </H1>

<p>Ce document a pour but de vous aider à paramétrer et utiliser le programme. Vous devez importer les différentes bibliothèques
nécessaires à l'aide du fichier requirements.txt présent dans le dépot git.

<a> https://github.com/Nyarlathotepss/OpenFoodFacts-is-back.git

<H2> Mise en place de la bdd postgres </H2>

<p>Installation de postgresql
<p>Création de la base
<p>Parametrage du fichier setting.py du projet Django pour lier votre base au projet
<p>Executer la migration des models de Django dans la base de données avec la commande: python manage.py migrate
<p>Executer le fichier initdb pour injecter les données dans votre base avec la commande: python manage.py initdb

<H2> Fonctionnement du site </H2>

<H3> Le site doit pouvoir proposer des alternatives de meilleures qualités nutritionelle que le produit
saisie dans le champ recherche</H3>

<p> Lancer le serveur localement avec la commande suivante: python manage.py runserver</p>
<p> Saisie d'un produit dans champ recherche
<p> Le site vous propose differentes alternatives qu'il sera possible de sauvegarder si vous êtes indentifié.

<h4> Information supplémentaire </h4>

<p>Les commandes se lance a la racine du projet Django au même niveau que votre fichier manage.py</p>
