# Projet 6 : Classification de Races de Chiens


## Introduction

Ce projet porte sur la classification d'images de races de chiens à partir du **Stanford Dogs Dataset**. Deux approches principales sont explorées : la création et l'entraînement de réseaux de neurones convolutionnels (CNN) et l'utilisation de modèles déjà entraînés via du **Transfer Learning** pour améliorer les perfomances.

## Objectifs

- **Prétraitement des images** : application de techniques spécifiques telles que le _whitening_ et l'_equalization_ pour améliorer la qualité des données d'entrée.
- **Data Augmentation** : utilisation de techniques telles que le _mirroring_, le _cropping_, et d'autres transformations pour enrichir le dataset et compenser le faible nombre d'images de chiens par classe.
- **Création et optimisation de modèles CNN** : développer, entraîner et optimiser des CNN en ajustant divers hyperparamètres liés aux couches du modèle, à la compilation et à l'exécution.
- **Transfer Learning** : implémentation et comparaison des performances de modèles pré-entraînés (VGG16 et MobileNetV1) adaptés à la classification des races de chiens.
- **Comparaison des performances** : évaluer et comparer la précision et le temps d'entraînement des modèles personnalisés et pré-entraînés.

## Dataset

Le dataset utilisé est le **Stanford Dogs Dataset**, qui comprend plus de 20 000 images réparties sur 120 races de chiens. Les images sont d'une grande variété et représentent différents angles, environnements et qualités d'éclairage, ce qui en fait un défi intéressant pour la classification.

## Approche

### 1. Prétraitement des Données
- **Whitening** : ajustement de la distribution des pixels pour faciliter la convergence des modèles.
- **Equalization** : amélioration du contraste des images afin d'uniformiser la luminosité et le contraste.
  
### 2. Data Augmentation
- **Mirroring** (miroir horizontal)
- **Random cropping** (recadrage aléatoire)
- **Rotation**
  
Ces techniques ont permis d’augmenter significativement la taille du dataset tout en améliorant la robustesse des modèles face à des variations dans les images d'entraînement.

### 3. Modèles CNN Personnalisés
- Plusieurs CNN ont été créés en ajustant les architectures (nombre de couches, types de couches) et les hyperparamètres (taux d'apprentissage, optimiseur, etc.).
- Les performances ont été évaluées et optimisées grâce à des techniques comme le **batch normalization** et **dropout** pour éviter l'overfitting.

### 4. Transfer Learning
- **VGG16** et **MobileNetV1** ont été utilisés comme modèles de base. Leurs couches finales ont été modifiées pour s'adapter à la classification multi-classes du dataset.
- Les performances en termes de précision et de temps d'entraînement ont été comparées.

## Résultats

Les résultats montrent que :
- Les modèles pré-entraînés, notamment **MobileNetV1**, offrent un bon compromis entre la précision et le temps d'entraînement.
- Les CNN personnalisés, bien qu'ayant une bonne capacité de généralisation, nécessitent un temps d'entraînement plus long.
- L'utilisation des techniques de **data augmentation** a permis d'améliorer la robustesse des modèles, en particulier dans les classes où le nombre d'images était limité.

## Conclusion

Ce projet a permis de comparer les performances entre des CNN personnalisés et des modèles pré-entraînés pour la classification des races de chiens. Le **Transfer Learning**, notamment avec **MobileNetV1**, a montré des résultats prometteurs en termes de précision et de temps de calcul, tandis que les CNN personnalisés ont nécessité un travail important d'optimisation des hyperparamètres pour obtenir des résultats compétitifs.

## Technologies Utilisées

- **Python** avec **TensorFlow** et **Keras**
- **Python** pour le suivi des expérimentations des différents modèles
- **VGG16**, **MobileNetV1** pour le Transfer Learning
- Techniques de **Data Augmentation** et **Prétraitement d'images**

## Fichiers Manquants

Le fichier frontend.py importe des fichiers situé dans un dossier utils, ce dossier utils contient notamment le modèle et les images du dataset mais ces derniers n'ont pas pu être uploadés sur ce dépôt Github en raison de leur taille.
