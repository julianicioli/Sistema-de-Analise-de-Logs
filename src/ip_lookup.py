import requests

def get_ip_info(ip):
    try:
        response = requests.get(
            f"https://ipinfo.io/{ip}/json",
            timeout=5
        )
        data = response.json()
        print(data)

        return{
            "ip": ip,
            "city": data.get("city", "Desconhecida"),
            "region": data.get("region", "Desconhecida"),
            "country": data.get("country", "Desconhecida"),
            "org": data.get("org", "Desconhecida")
        }
    except Exception as error:
        print(f"Erro ao consultar IP {ip}: {error}")
        return None