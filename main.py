from collections import defaultdict             #importa a biblioteca defaultdict para criar um dicionário que retorna um valor padrão para chaves inexistentes
from src.ip_lookup import get_ip_info

failed_attempts = defaultdict(int)

with open ("logs/sample.log", "r", encoding="utf-8") as file:
    logs = file.readlines()

for log in logs:
    log = log.strip()       #retira espaços em branco no início e no final de cada linha do log

    if "LOGIN_FAIL" in log:             #detecção de falhas
        timestamp, event, ip = log.split(" | ")
        failed_attempts[ip] += 1

for ip, attempts in failed_attempts.items():
    print(f"{ip}: {attempts} tentativas de login falhadas")

    if attempts >= 5:
        print(f"Alerta🔴: Cuidado! O IP {ip} teve {attempts} tentativas de login falhadas. Possível ataque de força bruta.")
    elif attempts >= 4:
        print(f"Alerta🟠: Atenção! O IP {ip} teve {attempts} tentativas de login falhadas. Possível ataque de força bruta.")
    elif attempts >= 3:
        print(f"Alerta🟡: O IP {ip} teve {attempts} tentativas de login falhadas. Possível ataque de força bruta.")

# RELATÓRIO DE FALHAS DE LOGIN

with open("reports/report.txt", "w", encoding="utf-8") as report:
    for ip, attempts in failed_attempts.items():
        report.write(f"{ip}: {attempts} tentativas falhas\n")
        if attempts >= 5:
            report.write(f"Alerta🔴: Cuidado! O IP {ip} teve {attempts} tentativas de login falhadas. Possível ataque de força bruta.\n")
        elif attempts >= 4:
            report.write(f"Alerta🟠: Atenção! O IP {ip} teve {attempts} tentativas de login falhadas. Possível ataque de força bruta.\n")
        elif attempts >= 3:
            report.write(f"Alerta🟡: O IP {ip} teve {attempts} tentativas de login falhadas. Possível ataque de força bruta.\n")
        
# GEOLOCALIZAÇÃO

for ip in failed_attempts.keys():
    info = get_ip_info(ip)

    if info:
        print("\n Informações do IP:")

        print(f"IP: {info['ip']}")
        print(f"Cidade: {info['city']}")
        print(f"Região: {info['region']}")
        print(f"País: {info['country']}")
        print(f"Organização: {info['org']}")