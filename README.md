# AIR · Architecture Workspace

<img src="plugins/air-local/assets/logo.png" alt="Logo AIR" width="112">

**Concevez un dossier d’architecture clair et vérifiable avec votre assistant agentique.**

AIR relie besoins métier, composants, données, décisions et preuves. Ce plugin fournit les skills pour installer le moteur puis faire progresser le dossier, question par question. Créé par **Yannick Huchard**, sous [Apache-2.0](LICENSE).

[Découvrir le moteur](https://github.com/yannickhuchard/air-engine) · [Guide du plugin](plugins/air-local/README.md) · [Vidéos](videos) · [Support](SUPPORT.md)

## Votre premier parcours

1. Installer le [moteur AIR](https://github.com/yannickhuchard/air-engine) avec Python 3.11+ : `python scripts/install.py --start`. Pas de Docker ni cloud obligatoire.
2. Installer ce plugin avec le parcours de votre client ci-dessous.
3. Demander : **« Utilise AIR pour connecter ce projet, puis montre-moi ce qui manque dans le dossier. Pose les questions une par une. »**
4. Lire les sources, décider, vérifier avec AIR et générer les livrables. Les trois exemples Asteria du moteur permettent de découvrir ce cycle.

## Installer dans Codex

```text
codex plugin marketplace add yannickhuchard/air-plugin --ref main
codex plugin add air-local@air-official
```

## Installer dans Claude Code

Dans une session Claude Code :

```text
/plugin marketplace add yannickhuchard/air-plugin
/plugin install air-local@air-official
```

Pour essayer le clone sans installation : `claude --plugin-dir ./plugins/air-local`. Le manifeste et la marketplace sont validés par la CLI Claude Code. Cela ne constitue ni une inscription à la marketplace officielle Anthropic ni une recette native de conception dans Claude. La connexion MCP reste configurée par projet.

## Utiliser avec ChatGPT

Le plugin guide le travail, mais ChatGPT doit pouvoir accéder à votre moteur via une connexion MCP distante autorisée. Il ne peut pas lancer un MCP stdio sur votre poste à travers le chat. L’installation des skills n’accorde aucun accès au référentiel.

La dernière observation de soumission conservée, le **1er octobre 2026**, est **IN_REVIEW pour 0.1.7**, sans publication confirmée. Le paquet source **0.1.8** présenté ici évolue séparément ; un push GitHub ne modifie pas la revue OpenAI.

## Ce que vous pouvez demander

> « Fais le lien entre ce besoin, les parcours concernés et les blocs à réaliser. »
>
> « Explique cette décision et ses conséquences pour l’équipe projet. »
>
> « Vérifie la préparation et régénère le dossier avec ses questions ouvertes. »

Le skill vérifie les outils réellement disponibles. Les fonctions récentes de News et d’actualisation vidéo nécessitent le moteur de développement 0.35 qui les expose ; le moteur public rc9 ne les contient pas. Un atelier vidéo optionnel est nécessaire pour les MP4. Le plugin ne promet aucune connexion ou fonction absente du catalogue.

## Données, versions et contribution

Ce dépôt contient les skills, manifests, logo et guides. Le moteur, ses versions et ses qualifications sont séparés. Aucun identifiant, base entreprise ou endpoint MCP partagé n’est distribué. Les extraits envoyés à un modèle cloud suivent les règles de votre organisation et du fournisseur.

Télécharger le paquet et son manifeste SHA-256 depuis [Releases](https://github.com/yannickhuchard/air-plugin/releases). Pour contribuer : `python scripts/build_plugin.py --output-dir dist/plugin`, puis `python -m pytest -q tests/test_plugin_package.py`. Aucune CI automatique n’est activée.

[Licence](LICENSE) · [Confidentialité](PRIVACY.md) · [Conditions](TERMS.md) · [Distribution](DISTRIBUTION.md) · [Soumission](submission/README.md)

Le format Claude et les commandes de marketplace suivent la [documentation officielle Claude Code](https://code.claude.com/docs/en/plugin-marketplaces). La prise en charge du MCP local diffère entre Code, Cowork et chat : [guide Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).
