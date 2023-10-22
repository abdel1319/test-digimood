### 1. What is the complexity of your algorithm (in big O notation)?
O(50) pour la flotte mais comme c'est constant c'est équivalent à O(1)

Pour trouver les positions, on parcourt  au maximum 4 directions à partir de chaque navire
donc au pire des cas 4 itérations pour chaque SupportCraft et donc O(25 * 4) équivalent à O(1)

Comme les deux parties sont contantes, la complexité de l'algo est donc O(1)

### 2. How would you improve your algorithm?
On peut optimiser ce code en utiliser l'algorithme de Djiskra ou bellman ford pour trouver la position la plus proche.

### 3
On doit mettre un tableau à 3 dimensions. Pour trouver la positions adjacentes, il faut vérifier au pire 6 directions au lieu de 4. Donc la compléxité va passer à O(n)