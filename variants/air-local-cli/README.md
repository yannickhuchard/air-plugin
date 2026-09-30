# AIR — Architecture Workspace : variante CLI 0.1.5

Paquet de préparation pour la revue spécifique d'exécution locale OpenAI.
Même identité `air-local`, développeur Yannick Huchard, Apache-2.0.
Il ne s'agit pas d'un second listing ni d'une publication approuvée.

Deux skills utilisent la CLI du moteur AIR public installé séparément, Python
3.11+, le service HTTP local authentifié, le home et les fichiers du projet.
Aucun serveur MCP n'est déclaré ni requis par cette variante. Aucun moteur ou
secret n'est inclus. Le profil testé sera décrit dans le reçu de recette ; ne
pas assimiler la présence d'un shell à une éligibilité publique OpenAI.

La distribution MCP 0.1.4 reste dans `plugins/air-local`. Cette variante se prépare
avec `python scripts/build_plugin.py --variant cli` depuis le dépôt du plugin.
Voir `submission/cli-review.md` pour la recette et les points ouverts du support.
