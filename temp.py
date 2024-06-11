from random import randint
import json
def get_nft_json(i):
    return {
        "name": f"NFT #{i}",
        "description": "the first nft of legendary cybercobra_collection",
        "image": "https://raw.githubusercontent.com/Vladikasik/public/main/cybercobra_collection/src/main.jpeg",
        "attributes": [
            {
            "trait_type": "Head",
            "value": str(randint(0,100))
            },
            {
            "trait_type": "Body",
            "value": str(randint(0,100))
            }
        ]
    }

for i in range(100):
    with open(f'cybercobra_collection/collectibles/{i}.json', 'w') as file:
        file.write(json.dumps(get_nft_json(i), indent=4))
  