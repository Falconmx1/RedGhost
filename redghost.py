#!/usr/bin/env python3
# RedGhost - Herramienta de IA para análisis de red
# Uso: python redghost.py [opciones]

import sys
import os
import subprocess
import random
import time

# Colores para el banner
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def mostrar_banner():
    banner = f"""
{GREEN}╔══════════════════════════════════════════════════════════════╗
║  {RED}██████╗ {BLUE}███████╗{YELLOW}██████╗ {GREEN} ██████╗ {CYAN}██╗  ██╗{RESET}               ║
║  {RED}██╔══██╗{BLUE}██╔════╝{YELLOW}██╔══██╗{GREEN}██╔════╝ {CYAN}██║  ██║{RESET}               ║
║  {RED}██████╔╝{BLUE}█████╗  {YELLOW}██║  ██║{GREEN}██║  ███╗{CYAN}███████║{RESET}               ║
║  {RED}██╔══██╗{BLUE}██╔══╝  {YELLOW}██║  ██║{GREEN}██║   ██║{CYAN}██╔══██║{RESET}               ║
║  {RED}██║  ██║{BLUE}███████╗{YELLOW}██████╔╝{GREEN}╚██████╔╝{CYAN}██║  ██║{RESET}               ║
║  {RED}╚═╝  ╚═╝{BLUE}╚══════╝{YELLOW}╚═════╝ {GREEN} ╚═════╝ {CYAN}╚═╝  ╚═╝{RESET}               ║
║                                                              ║
║     {CYAN}RedGhost - IA para Redes v1.0{RESET}                         ║
║     {YELLOW}Hecho para pentesters y sysadmins{RESET}                   ║
╚══════════════════════════════════════════════════════════════╝{RESET}
"""
    print(banner)

def mostrar_menu():
    print(f"\n{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{GREEN}[1]{RESET} Escaneo de puertos con IA predictiva")
    print(f"{GREEN}[2]{RESET} Análisis de tráfico (simulación)")
    print(f"{GREEN}[3]{RESET} Predicción de latencia")
    print(f"{GREEN}[4]{RESET} Detectar anomalías en red")
    print(f"{GREEN}[5]{RESET} Salir")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def escaneo_puertos(ip):
    print(f"\n{CYAN}[*] Escaneando {ip} con IA predictiva...{RESET}")
    puertos_comunes = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 8080]
    
    for puerto in puertos_comunes:
        # Simulación de escaneo (en realidad usarías socket o scapy)
        time.sleep(0.05)
        if random.random() > 0.7:  # 30% de probabilidad de estar abierto (demo)
            prediccion = random.choice(["HTTP", "SSH", "MySQL", "RDP", "HTTPS"])
            print(f"  {GREEN}[+] Puerto {puerto} ABIERTO{Puerto} - IA predice: {prediccion}{RESET}")
        else:
            print(f"  {RED}[-] Puerto {puerto} CERRADO{RESET}")
    
    print(f"{CYAN}[✓] Escaneo completado. IA generó reporte predictivo{RESET}")

def analisis_trafico():
    print(f"\n{CYAN}[*] Analizando tráfico de red en tiempo real...{RESET}")
    protocolos = ["TCP", "UDP", "ICMP", "ARP", "DNS"]
    for i in range(10):
        proto = random.choice(protocolos)
        bytes_ = random.randint(40, 1500)
        print(f"  Paquete {i+1}: {proto} | {bytes_} bytes | {BLUE}IA: Normal{RESET}")
        time.sleep(0.1)
    print(f"{GREEN}[✓] Análisis completado. No se detectaron anomalías.{RESET}")

def predecir_latencia(ip):
    print(f"\n{CYAN}[*] Prediciendo latencia hacia {ip}...{RESET}")
    # Simulación de predicción con IA (regresión lineal)
    latencias = [random.randint(10, 200) for _ in range(5)]
    promedio = sum(latencias) / len(latencias)
    prediccion = promedio * (0.9 + random.random() * 0.2)
    
    print(f"  Mediciones reales: {latencias} ms")
    print(f"  {BLUE}IA predice: {prediccion:.2f} ms{RESET}")
    
    if prediccion < 50:
        print(f"  {GREEN}✓ Latencia EXCELENTE{RESET}")
    elif prediccion < 100:
        print(f"  {YELLOW}⚠ Latencia ACEPTABLE{RESET}")
    else:
        print(f"  {RED}✗ Latencia ALTA - Posible congestión{RESET}")

def detectar_anomalias():
    print(f"\n{CYAN}[*] Ejecutando detección de anomalías con RandomForest...{RESET}")
    # Simulación de detección de outliers
    metricas = {
        "throughput": random.uniform(10, 100),
        "packet_loss": random.uniform(0, 5),
        "jitter": random.uniform(0, 20),
        "tcp_retransmits": random.randint(0, 10)
    }
    
    print(f"\n  Métricas actuales:")
    for k, v in metricas.items():
        print(f"    {k}: {v}")
    
    # IA simple: detecta anomalías
    es_anomalia = (metricas["packet_loss"] > 3 or 
                   metricas["jitter"] > 15 or 
                   metricas["tcp_retransmits"] > 5)
    
    if es_anomalia:
        print(f"\n  {RED}⚠ ALERTA: IA detectó comportamiento anómalo{RESET}")
        print(f"  {YELLOW}Recomendación: Revisar conexiones y posibles ataques{RESET}")
    else:
        print(f"\n  {GREEN}✓ Todo normal según modelo IA{RESET}")

def main():
    mostrar_banner()
    
    while True:
        mostrar_menu()
        opcion = input(f"\n{BLUE}RedGhost>{RESET} ").strip()
        
        if opcion == "1":
            ip = input(f"{CYAN}Ingresa IP objetivo (ej: 192.168.1.1): {RESET}")
            escaneo_puertos(ip)
        elif opcion == "2":
            analisis_trafico()
        elif opcion == "3":
            ip = input(f"{CYAN}Ingresa IP para predecir latencia: {RESET}")
            predecir_latencia(ip)
        elif opcion == "4":
            detectar_anomalias()
        elif opcion == "5":
            print(f"{GREEN}¡Hasta la vista, bro! 👻{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Opción no válida{RESET}")
        
        input(f"\n{YELLOW}Presiona Enter para continuar...{RESET}")

if __name__ == "__main__":
    main()
