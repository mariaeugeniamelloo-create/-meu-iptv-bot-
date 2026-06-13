import requests

URLS_FONTES = [
    "https://iptv-org.github.io/iptv/countries/br.m3u",
    "https://raw.githubusercontent.com/GuikiStudio/Playlists/main/PlutoTV.m3u"
]

def atualizar_lista():
    conteudo_final = "#EXTM3U\n"
    print("Iniciando a atualização...")
    for url in URLS_FONTES:
        try:
            resposta = requests.get(url, timeout=15)
            if resposta.status_code == 200:
                linhas = resposta.text.splitlines()
                if linhas and linhas[0].startswith("#EXTM3U"):
                    linhas = linhas[1:]
                conteudo_final += "\n".join(linhas) + "\n"
                print(f"Sucesso: {url}")
        except Exception as e:
            print(f"Erro em {url}: {e}")
            
    with open("minha_lista.m3u", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_final.strip())
    print("Lista gerada!")

if __name__ == "__main__":
    atualizar_lista()
