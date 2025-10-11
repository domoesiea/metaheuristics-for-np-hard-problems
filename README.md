# metaheuristics-for-np-hard-problems
Practical optimization framework combining MILP and metaheuristics for NP-hard problems.

🧩 Introduction

Ce projet explore la résolution de problèmes d’optimisation combinatoire NP-difficiles à travers la comparaison et l’hybridation de méthodes exactes (Programmation Linéaire en Nombres Entiers) et de métaheuristiques (Glouton, Algorithme Génétique, Recherche Tabou).

L’objectif est double :
d’une part, modéliser rigoureusement le problème de sélection optimale (clique maximale pondérée) et évaluer les performances des approches existantes ;
d’autre part, concevoir des méthodes hybrides combinant exploration globale et recherche locale pour améliorer la qualité et la robustesse des solutions.

Ce travail illustre la complémentarité entre optimisation mathématique, intelligence artificielle et applications industrielles, et ouvre la voie à l’optimisation pour l’apprentissage automatique, où ces techniques peuvent être appliquées à la recherche d’architectures, au réglage d’hyperparamètres ou à la planification intelligente.

## 1️ Problème étudié

Notre but est de résoudre un problème d’organisation de soirée. On dispose d’un ensemble de N convives 
potentiels. Pour chaque convive potentiel i ∈ {1, .., N }, on définit Vi l’ensemble de ses connaissances, avec 
Vi ⊆ {1, .., N }. Pour tout couple (i, j) ∈ {1, .., N }², si i et j se connaissent, alors i ∈ Vj et j ∈ Vi. Tout convive 
potentiel i a une valeur ci représentant l’intérêt d’avoir cette personne à notre soirée. Pour une instance 
donnée, on cherchera à réunir le plus de personnes intéressantes possibles à condition que toutes se 
connaissent : l’objectif sera donc dépendant du coefficient d’intérêt ci de chacun des convives invités.  

## 🧮 Modélisation mathématique

Soit 𝑥𝑖 une variable de décision tel que : 

$$
x_i =
\begin{cases}
1 & \text{si la personne } i \text{ est invitée} \\
0 & \text{sinon}
\end{cases}
$$

Objectif :

$$
\max \sum_{i=1}^N c_i x_i
$$

Sous les contraintes suivantes :
- Si i est invité et ne connaît pas j alors j ne doit pas être invité  :
  
$$
x_i + x_j \le 1, \quad \forall (i, j)  \quad tel que \quad 𝑖 ∉ 𝑉𝑗 𝑒𝑡 𝑗 ∉ 𝑉i
$$

## 📊 Résultats trouvés avec le solveur GLPK 

| Instances | Score trouvé  | 
|----------|--------------|
| Instance 1 | 73 |
| Instance 2 | 91 |
| Instance 3 | 84 |
| Instance 4 | 83 |
| Instance 5 | 81 |
| Instance 6 | 80 |
| Instance 7 | 81 |
| Instance 8 | 85 |
| Instance 9 | 77 |
| Instance 10 | 91 |

<p align="center">
  <img src="images/convergence_ga_tabou.png" width="450">
</p>


## 📊 Résultats trouvés par l’algorithme glouton
De manière générale, les tests ont été réalisés sur Windows. Pour l’algorithme glouton, nous avons codé 
le même algorithme glouton que dans le sujet. Nous retrouvons correctement les mêmes résultats. 

| Instances | Score trouvé  | Gap |
|----------|--------------|--------|
| Instance 1 | 69 | 0.5 |
| Instance 2 | 90 | 0.01 |
| Instance 3 | 71 | 0.15 |
| Instance 4 | 67 | 0.19 |
| Instance 5 | 80 | 0.01 |
| Instance 6 | 73 | 0.0875 |
| Instance 7 | 61 | 0.25 |
| Instance 8 | 69 | 0.19 |
| Instance 9 | 68 | 0.12 |
| Instance 10 | 72 | 0.21 |

Pour le glouton randomisé, nous masquons aléatoirement une valeur sur deux du jeu de données afin de 
créer de la diversité. 
Pour le glouton qui sert à réparer les solutions, nous masquons toutes les valeurs qui ne sont pas dans 
l’ensemble de connaissances des individus de la solution passée en entrée. 

## 6️⃣ Hybridation : Algorithme génétique + Tabou
