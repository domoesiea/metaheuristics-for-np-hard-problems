# metaheuristics-for-np-hard-problems
Practical optimization framework combining MILP and metaheuristics for NP-hard problems.

🧩 Introduction

Ce projet explore la résolution de problèmes d’optimisation combinatoire NP-difficiles à travers la comparaison et l’hybridation de méthodes exactes (Programmation Linéaire en Nombres Entiers) et de métaheuristiques (Glouton, Algorithme Génétique, Recherche Tabou).

L’objectif est double :
d’une part, modéliser rigoureusement le problème de sélection optimale (clique maximale pondérée) et évaluer les performances des approches existantes ;
d’autre part, concevoir des méthodes hybrides combinant exploration globale et recherche locale pour améliorer la qualité et la robustesse des solutions.

Ce travail illustre la complémentarité entre optimisation mathématique, intelligence artificielle et applications industrielles, et ouvre la voie à l’optimisation pour l’apprentissage automatique, où ces techniques peuvent être appliquées à la recherche d’architectures, au réglage d’hyperparamètres ou à la planification intelligente.

## 1️⃣ Problème étudié

🎯 Objectif

Trouver le meilleur sous-ensemble de convives à inviter à une soirée,
maximisant un score d’intérêt total tout en garantissant que tous se connaissent mutuellement.

🔹 Données

## 2️⃣ Méthode exacte : MILP

🧮 Outil

Solveur utilisé : GLPK (ou scipy.optimize.milp pour version Python).

Permet d’obtenir la solution optimale garantie, mais uniquement pour de petites instances.

🧠 Implémentation


📊 Résultats

## 3️⃣ Méthode heuristique : algorithme glouton

🧩 Principe

Construire progressivement une solution réalisable en ajoutant à chaque étape le convive le plus “intéressant”, selon un critère local.

🔹 Critère de sélection


## 4️⃣ Métaheuristique : Algorithme Génétique (GA)
🧬 Principe

## 5️⃣ Métaheuristique : Algorithme à liste tabou
🧠 Idée

Utiliser la recherche locale améliorée en évitant de revisiter les mêmes solutions grâce à une liste de mouvements interdits (tabou).

## 6️⃣ Hybridation : Algorithme génétique + Tabou
