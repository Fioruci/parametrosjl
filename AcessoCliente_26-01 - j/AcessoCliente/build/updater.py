import time
import json
from urllib.request import urlopen
import requests


def pegaChave(url):
    urla = "https://api.npoint.io/a5fb1c4c89523f3fb24f/"
    resposta = urlopen(urla)
    tkeya = json.loads(resposta.read())
    print("Procurando atualizações...")

    # link_api = tkeya["KEY_SISTEMAS"][url]["LINK"]
    keyx_api = tkeya["KEY_SISTEMAS"][url]["KEYX"]
    
    with open("build\\assets\\parametros.json", 'r') as f:
        keyx_prma = json.load(f)
        keyx_prm = keyx_prma[url]["KEYX"]
        f.close()

    if (keyx_api != keyx_prm):
        print("\n\nATUALIZAÇÃO ENCONTRADA!")
        # download_url = f"https://api.npoint.io/a5fb1c4c89523f3fb24f/KEY_SISTEMAS/{url}/LINK"
        t = requests.get("http://fioruci.atwebpages.com/parametros/" + url.lower() + ".html")

        print("\n\ATUALIZAÇÃO BAIXADA.")
        open("build\\" + url.lower() + ".py", "wb").write(t.content)

        with open("build\\assets\\parametros.json", 'r') as f1:
            data = json.load(f1)

            data[url]["KEYX"] = keyx_api
        
        with open("build\\assets\\parametros.json", "w") as f2:
            json.dump(data, f2, indent=4)

        print("\nINSTALAÇÃO CONCLUÍDA.")
    # return tkeya

# pegaChave("MAIN")