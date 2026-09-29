# AIR — Architecture Workspace

<img src="assets/logo.png" alt="Logo AIR : un A formé de plans structurels reliés" width="128">

Plugin officiel du projet **AIR — Architecture Intermediate Representation**.
**Auteur et développeur officiel : Yannick Huchard.**

- Source publique du plugin : https://github.com/yannickhuchard/air-plugin
- Dépôt du moteur (accès séparé) : https://github.com/yannickhuchard/air-engine
- Identifiant : `air-local` ; version du plugin : **0.1.4**.
- Licence : **Apache-2.0**, confirmée par Yannick Huchard le 28 septembre 2026 ; voir `LICENSE` et `NOTICE`.
- Moteur associé à cette livraison : **0.34.0rc9**, qualifié séparément du plugin.
- Deux skills : installation/connexion locale et travail sur un dossier d'architecture.

Le plugin accompagne un moteur AIR installé par entreprise ou par architecte. Il
ne nécessite aucun hébergement central AIR. SQLite et l'authentification locale
restent les valeurs par défaut ; PostgreSQL et OIDC restent optionnels.

Le nom affiché **AIR — Architecture Workspace** explicite le domaine sans changer
le nom du langage AIR ni l’identifiant stable `air-local`. Le logo représente un A
structurel et un nœud de modèle ; il a été créé pour AIR avec assistance générative.

## Installation et prérequis publics

Le plugin et le moteur sont distribués publiquement, dans des dépôts séparés.
Télécharger le moteur depuis https://github.com/yannickhuchard/air-engine puis suivre
son guide d’installation et les trois dossiers Asteria inclus. Sans moteur installé
et connexion MCP utilisable, le plugin ne peut pas vérifier ni écrire un dossier AIR.

Support : [GitHub Issues](https://github.com/yannickhuchard/air-plugin/issues).
[Confidentialité](https://github.com/yannickhuchard/air-plugin/blob/main/PRIVACY.md) ·
[Conditions et licence](https://github.com/yannickhuchard/air-plugin/blob/main/TERMS.md).

## Installer le paquet

Installer ce dossier comme plugin local avec le gestionnaire de plugins du client.
Il contient un manifeste portable `plugin.json` et le manifeste de compatibilité
Codex `.codex-plugin/plugin.json`. Dans Codex, le skill Plugin Creator peut ajouter
ce dossier à votre marketplace personnelle, sans écraser les autres entrées.
Ouvrir ensuite une nouvelle conversation et demander :

> Utilise AIR Local pour installer ou connecter AIR au référentiel de cette entreprise.

Le skill `air-local-setup` utilise l'installateur Python et `air ide-setup` du dépôt
officiel. Il conserve la connexion MCP au niveau du projet : aucun serveur global,
jeton, identifiant de tunnel ou chemin propre au développeur n'est distribué.
Le moteur n'est pas inclus dans ce petit paquet de skills. La distribution publique du moteur est disponible sans invitation GitHub.
La branche principale peut contenir une version de développement : sélectionner
la version du moteur reçue par l'entreprise, indépendamment de celle du plugin.

## Données et limites

Un freelance utilise un home AIR, une identité et un référentiel distincts par client.
Les installations autonomes ne se synchronisent pas automatiquement.
Le stockage local ne rend pas un modèle cloud local : les contenus transmis à
ChatGPT, Claude ou un autre fournisseur suivent les règles de ce fournisseur et
de l'entreprise. Sélectionner uniquement les données autorisées pour cet usage.

Codex utilise la connexion MCP locale du projet. ChatGPT nécessite sa propre
connexion distante, par exemple un tunnel MCP sécurisé vers le poste. Le plugin
n'installe pas ce tunnel et ne rafraîchit pas automatiquement son catalogue.
La prise en charge du format portable par chaque IDE doit être vérifiée ; ce
paquet n'est pas une certification de tous les clients mentionnés dans AIR.

« Officiel » désigne l'auteur du projet AIR, pas une certification par OpenAI ou
Anthropic. La redistribution suit Apache-2.0. La distribution publique sur GitHub ne signifie pas une approbation ni une présence
dans l’annuaire officiel ChatGPT/Codex. Aucun SLA contractuel n’est fourni. Consulter le dépôt pour le
périmètre G1 local reçu ; le paquet de skills ne qualifie pas une nouvelle version
du moteur. Les preuves P07/P08 restent distinctes de ce plugin.
