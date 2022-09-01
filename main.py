from repertorio import Repertorio
import json

secretsAndKeys = json.load(open('secretsAndKeys.json'))

api = Repertorio(secretsAndKeys['setlistfmAPIKey'])