# Portes Ouvertes 2023

Pour ces portes ouvertes j'ai décidé de présenter une utilisation d'une API à travers une interface. Ce projet utilise la bibliothèque Python d'OpenAI pour utiliser leurs modèles d'IA. Pour l'API j'ai utilisé FastAPI une librairie Python pour créer des API.

## Run locally

Premièrement installez les dépendances si cela n'est pas déjà fait.

```sh
./install.sh
```

Pour configurer le token OpenAI, faites le dans le `.env`:

```
OPENAI_API_KEY=<your_token>
```

Pour run le serveur faites:

```sh
./run.sh
```
