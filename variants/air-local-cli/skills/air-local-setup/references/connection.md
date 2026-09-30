# Exécution locale sans MCP

Le chemin est : agent disposant d'un shell local → CLI AIR → HTTP authentifié sur
127.0.0.1 → moteur Python/SQLite. Il ne nécessite aucun serveur MCP ni backend
partagé. Le service HTTP AIR et ses fichiers de configuration restent nécessaires.
Le CLI consomme les credentials protégés sans les afficher. Le plugin ne les
conserve pas et n'utilise pas de variable de template d'installation.

Les chemins moteur/home, le port et l'identité sont des entrées explicites du
projet. L'installateur du moteur gère les fichiers locaux. Ne pas demander le
contenu d'un secret dans la conversation. Si un prérequis manque, expliquer
comment installer/configurer le moteur officiel ; ne pas basculer vers une
instance distante ou un autre home automatiquement.

Le helper de air-local-design retourne AIR_ENGINE_MISSING,
AIR_CONFIGURATION_MISSING ou AIR_EXECUTION_UNAVAILABLE selon le problème.
Le moteur retourne AIR_UNREACHABLE si le service n'est pas démarré. Les erreurs
d'accès ne sont pas une raison d'accorder automatiquement un rôle plus élevé.

Le support OpenAI recommande de préparer cette variante pour revue spécifique
(cas #16084977). Cela ne confirme pas encore son éligibilité publique ni les
surfaces Codex/ChatGPT Work acceptées. Le ChatGPT sans exécuteur local ne peut
pas utiliser ce parcours. Conserver le brouillon existant pour la migration.
