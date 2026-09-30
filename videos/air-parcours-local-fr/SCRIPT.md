# Lire les preuves avant de décider

Un dossier d’architecture peut être bien présenté tout en laissant des décisions importantes sans preuve. Ce parcours montre comment AIR rend ces limites visibles, pour que les équipes sachent quoi construire et quoi vérifier ensuite. Nous utilisons trois dossiers entièrement fictifs de la même entreprise : Asteria Industrie.

Le premier concerne le service après-vente. Le deuxième prépare la maintenance connectée d’un atelier. Le troisième organise les arrivées, les mobilités et les départs. Ils partagent un contexte d’entreprise, une plateforme d’identité et une équipe d’intégration.

Cette vidéo est un montage commenté de captures des vues réellement générées par le moteur public zéro point trente-quatre, candidate neuf. Elle ne montre ni une session ChatGPT en direct, ni l’exécution des applications métier futures. Les commentaires expliquent les résultats conservés dans le reçu de démonstration.

# Une installation à la portée du poste

La première cible de déploiement est le poste de chaque architecte. Python suffit à l’installation documentée, avec SQLite et une identité locale par défaut. Docker, un service cloud et un fournisseur d’identité externe ne sont pas obligatoires. Les options PostgreSQL et OIDC répondent à des besoins distincts.

Le kit de réception public télécharge les artefacts de la candidate et vérifie leurs empreintes. Le reçu de la répétition confirme une installation neuve depuis le paquet, une installation hors ligne, une réinstallation qui préserve l’identité et la révision, puis une restauration qui conserve l’empreinte des données et révoque l’ancienne identité.

Ces résultats proviennent d’un environnement séparé sur le même poste Windows, avec Python trois point douze. Ils ne prouvent pas une réception sur une seconde machine physique. Le reçu conserve aussi la mention non exécuté pour la recette d’un client agent natif et pour le parcours public ChatGPT. C’est cette limite précise qui accompagne la distribution.

# D01 / Enregistrer une demande SAV

Ouvrons le dossier du service après-vente. L’exigence demande d’enregistrer une déclaration durable, distincte de toute décision de garantie. La vue relie cette exigence à la fonction Submit Claim, à son contrat, puis au travail de construction et de vérification. La chaîne permet de discuter le même objet avec les métiers et les ingénieurs.

Le tableau suivant décrit trois scénarios à exécuter lors de la réalisation : traiter un dépôt et son doublon, refuser une demande concernant un autre client, puis gérer une indisponibilité sans fabriquer de faux reçu. La colonne d’exécution indique non exécuté. Un résultat attendu ne devient pas un test réussi parce qu’il a été rédigé.

L’inconnue visible porte sur la fiabilité de la clé de déduplication fournie par l’ERP. Dans le reçu calculé, le résultat est UNKNOWN et la porte est bloquée. La suite proposée consiste à obtenir une confirmation sourcée de l’équipe ERP, puis à réviser et vérifier le dossier. Nous ne remplaçons pas cette confirmation par une supposition de l’agent.

# D02 / Proposer une inspection

Le dossier atelier demande de proposer une inspection humaine à partir de mesures fraîches, sans commande physique automatique. La fonction et le contrat portent cette séparation. Le travail prévu concerne la construction et la vérification du service de proposition. Aucune machine réelle n’est pilotée par cette démonstration.

La réception future distingue une mesure nominale, une mesure périmée, puis un collecteur expiré ou une unité incompatible. Les résultats attendus précisent le comportement à développer. Là encore, les trois scénarios restent non exécutés. L’architecte transmet ainsi des critères concrets, sans prétendre que l’application a déjà été construite.

Le contrôle de la démonstration donne VIOLATED pour l’observation périmée et garde la porte bloquée. Ce statut calculé ne doit pas être confondu avec le résultat inconnu prévu pour un futur scénario applicatif. La question ouverte demande quel seuil de fraîcheur rend une observation inutilisable. La suite proposée est de faire approuver ce seuil et de fournir une observation valide, puis de relancer les vérifications concernées.

# D03 / Préparer une révocation

Le troisième dossier concerne les identités. L’exigence demande une révocation traçable, tout en séparant proposition, approbation et exécution. La fonction prépare une proposition. La vue ne fournit aucune autorisation de supprimer un accès dans un système réel.

Les scénarios prévus couvrent un départ nominal, des dates contradictoires et un compte non rapproché. Une contradiction doit conduire à un blocage et à la désignation du responsable de résolution. Une inconnue doit rester visible, sans action automatique sur un autre compte. Ces comportements sont des critères pour la phase d’ingénierie.

Le reçu calculé conserve CONFLICTING et la porte bloquée. Dans la vue, une question demande également qui confirme la date de fin d’un prestataire dont l’échéance est absente. Ces réserves sont distinctes et doivent être traitées avec leurs sources. La suite proposée est un arbitrage documenté entre les responsables concernés, puis une nouvelle révision. Choisir arbitrairement la source la plus commode masquerait le risque au lieu de le résoudre.

# Transmettre un dossier honnête

Les trois vues possèdent une section registre et sources. Les objets y sont rattachés à leurs révisions, et chaque vue identifie sa baseline par une empreinte. Une correction passe par une nouvelle révision et une proposition. Cela permet de conserver le contexte exact utilisé pour produire le dossier, plutôt que de modifier silencieusement son histoire.

Le livrable destiné aux ingénieurs, aux chefs de projet et aux équipes d’exploitation doit inclure les exigences, les contrats, le travail prévu, les scénarios de réception et les questions ouvertes. Dans cette démonstration, neuf tests des futurs systèmes métier restent non exécutés. Les trois portes bloquées sont des résultats utiles : elles indiquent les éléments à résoudre avant d’accorder la réception concernée.

Le moteur et les exemples sont disponibles dans le dépôt public AIR Engine. Le plugin Architecture Workspace fournit les skills d’accompagnement, avec un moteur installé séparément et une connexion propre au projet. La publication dans l’annuaire OpenAI attend une réponse sur cette topologie locale. Cette vidéo documente le parcours local ; la recette publique ChatGPT et la vidéo correspondante restent à effectuer lorsque cette voie sera confirmée.