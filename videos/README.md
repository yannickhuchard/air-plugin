# Vidéos AIR — Architecture Workspace

Deux vidéos en français, avec voix de synthèse locale, sous-titres incrustés et
fichiers SRT/VTT séparés. Développeur officiel : **Yannick Huchard**.

Publication YouTube publique confirmée le 30 septembre 2026 :

- [Playlist AIR — Architecture de solutions avec les outils agentiques](https://www.youtube.com/playlist?list=PLc6Fk84UAiYc)
- [Présentation AIR](https://youtu.be/NV3DxBdulro)
- [Trois dossiers Asteria, du besoin aux preuves](https://youtu.be/6V9c3qvojU8)

Les descriptions incluent les liens des dépôts et du white paper
[Enterprise Morphogenesis](https://yannickhuchard.github.io/enterprise-morphogenesis/).
Les intégrations futures et la revue OpenAI y sont distinguées des fonctions reçues.

| Vidéo | Durée de composition | Contenu |
| --- | --- | --- |
| `air-presentation-fr` | 2 min 01 s | Valeur d’AIR, chaîne de conception, trois alertes Asteria, installation autonome et distribution |
| `air-parcours-local-fr` | 6 min 43 s | Reçu local, dossiers SAV/atelier/identités, critères de réception et provenance |

Téléchargements de la livraison du 30 septembre 2026 :

- [Présentation AIR — MP4](https://github.com/yannickhuchard/air-plugin/releases/download/air-local-v0.1.4/air-presentation-fr-20260930.mp4)
- [Parcours local Asteria — MP4](https://github.com/yannickhuchard/air-plugin/releases/download/air-local-v0.1.4/air-parcours-local-fr-20260930.mp4)
- [Kit complet : vidéos, sources, narration et sous-titres](https://github.com/yannickhuchard/air-plugin/releases/download/air-local-v0.1.4/air-videos-kit-20260930.zip)
- [Reçu de vérification](https://github.com/yannickhuchard/air-plugin/releases/download/air-local-v0.1.4/videos-validation-20260930.json)

Ces assets supplémentaires ne remplacent pas le ZIP du plugin 0.1.4.

Le parcours est un **montage commenté de captures des vues HTML réellement
générées**, avec un extrait éditorial du reçu. Il ne constitue pas un enregistrement
continu d’exécution des commandes, ni une session de recette avec ChatGPT.
Les résultats UNKNOWN, VIOLATED et CONFLICTING et les portes BLOCKED sont conservés.
Les neuf tests des futurs systèmes métier restent NOT_EXECUTED.

## Périmètre

Moteur public `0.34.0rc9`, plugin `0.1.4`. Données entièrement fictives Asteria.
Le reçu est celui d’une répétition dans un environnement séparé sur le même poste
Windows/Python 3.12. Il n’atteste ni un second poste physique, ni une nouvelle recette
native, ni le parcours public ChatGPT. Les vidéos ne changent pas ces statuts.
La vidéo de soumission sur la connexion publique OpenAI reste à réaliser lorsque
la voie supportée sera établie ; voir [le guide](../submission/demo-runbook.md).

## Sources et reproduction

Chaque dossier contient son brief, sa direction graphique, son storyboard, son
script, les durées de narration mesurées, les chapitres et les sous-titres.
Les captures proviennent des HTML inchangés dans
`air-parcours-local-fr/assets/source/`. `asset-provenance.json` conserve les empreintes.
La voix synthétique utilise Kokoro `ff_siwis` ; aucune imitation de personne réelle.
Les sous-titres sont distribués par phrase sur les durées mesurées des paragraphes ;
leur timing n’est pas présenté comme un alignement vocal mot à mot.

Ces outils sont **uniquement des dépendances de production vidéo**. AIR continue
de s’installer avec Python seul. Pour reconstruire les vidéos : Node 22+, Python,
FFmpeg/FFprobe, HyperFrames 0.8.95 et le moteur vocal local Kokoro. Le premier usage
peut télécharger outils, modèle et polices ; aucun compte HeyGen n’est nécessaire.

Depuis ce dépôt, sur Windows :

```powershell
python videos/prepare_audio.py
python videos/build_videos.py
```

Puis, dans chacun des deux projets :

```powershell
npm run check -- --snapshots
npx --yes hyperframes@0.8.95 preview --background
npm run render -- --fps 24 --quality high --output renders/<nom-du-projet>.mp4
```

Le kit inclut les WAV déjà générés. Pour les réutiliser sans nouvelle synthèse,
exécuter seulement `build_videos.py`, qui prépare aussi la dépendance GSAP épinglée.

`verify_videos.py` exige Pillow et vérifie décodage complet, durée, dimensions,
pistes audio/vidéo, niveaux sonores et images de chaque chapitre. La vérification
visuelle du montage reste nécessaire. Les résultats finaux sont dans `validation.json`.
Les MP4 et fichiers audio sont distribués comme artefacts, hors historique Git.

Licence des scripts, graphismes AIR, captures et exemples : Apache-2.0 du dépôt.
Les dépendances et polices conservent leurs licences respectives ; GSAP 3.14.2,
Montserrat et IBM Plex Mono ne sont pas réattribués à AIR.
