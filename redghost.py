#!/usr/bin/env python3
# RedGhost - Herramienta completa con IA, Deep Learning, Web y Exportación

import sys
import time
import json
from colorama import init, Fore, Style
from network_ai import ai_engine
from deep_network_ai import deep_ai
from scanner import RealScanner
from host_discovery import HostDiscovery
from export_utils import export_utils
from web_interface import start_web_server
import threading

init(autoreset=True)

# Colores
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

def mostrar_banner():
    banner = f"""
{GREEN}╔═══════════════════════════════════════════════════════════════════════╗
║  {RED}██████╗ {BLUE}███████╗{YELLOW}██████╗ {GREEN} ██████╗ {CYAN}██╗  ██╗{RESET}                         ║
║  {RED}██╔══██╗{BLUE}██╔════╝{YELLOW}██╔══██╗{GREEN}██╔════╝ {CYAN}██║  ██║{RESET}                         ║
║  {RED}██████╔╝{BLUE}█████╗  {YELLOW}██║  ██║{GREEN}██║  ███╗{CYAN}███████║{RESET}                         ║
║  {RED}██╔══██╗{BLUE}██╔══╝  {YELLOW}██║  ██║{GREEN}██║   ██║{CYAN}██╔══██║{RESET}                         ║
║  {RED}██║  ██║{BLUE}███████╗{YELLOW}██████╔╝{GREEN}╚██████╔╝{CYAN}██║  ██║{RESET}                         ║
║  {RED}╚═╝  ╚═╝{BLUE}╚══════╝{YELLOW}╚═════╝ {GREEN} ╚═════╝ {CYAN}╚═╝  ╚═╝{RESET}                         ║
║                                                                           ║
║     {CYAN}RedGhost v3.0 - Ultimate AI Network Toolkit{RESET}                      ║
║     {YELLOW}RandomForest | LSTM | Autoencoder | Flask | Scapy{RESET}               ║
╚═══════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(banner)

def menu_principal():
    print(f"\n{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{GREEN}[1]{RESET} Escaneo de puertos REAL (Scapy)")
    print(f"{GREEN}[2]{RESET} Descubrimiento de hosts en red")
    print(f"{GREEN}[3]{RESET} Análisis de tráfico (RandomForest)")
    print(f"{GREEN}[4]{RESET} Predicción de latencia (Regresión Lineal)")
    print(f"{GREEN}[5]{RESET} Detección de anomalías (Isolation Forest)")
    print(f"{GREEN}[6]{RESET} Predicción con Deep Learning (LSTM)")
    print(f"{GREEN}[7]{RESET} Detección profunda (Autoencoder)")
    print(f"{GREEN}[8]{RESET} Exportar resultados (JSON/CSV)")
    print(f"{GREEN}[9]{RESET} 🌐 Iniciar interfaz web (Flask)")
    print(f"{GREEN}[10]{RESET} Salir")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def escaneo_puertos():
    ip = input(f"{CYAN}🌐 IP objetivo: {RESET}")
    scanner = RealScanner(ip)
    resultados = scanner.escanear_puertos()
    
    # Preguntar si exportar
    if input(f"{YELLOW}¿Exportar resultados? (s/n): {RESET}").lower() == 's':
        export_utils.export_scan_results([{'ip': ip, 'puertos_abiertos': list(resultados.keys())}])
    
    input(f"{YELLOW}Enter para continuar...{RESET}")

def descubrimiento_hosts():
    discovery = HostDiscovery()
    hosts = discovery.escaneo_completo()
    
    print(f"\n{GREEN}📡 Hosts encontrados: {len(hosts)}{RESET}")
    for host in hosts[:10]:  # Mostrar primeros 10
        print(f"  🖥️ {host['ip']} - {host['mac']} ({host['vendor']})")
    
    if len(hosts) > 10:
        print(f"  ... y {len(hosts) - 10} más")
    
    if input(f"{YELLOW}¿Exportar resultados? (s/n): {RESET}").lower() == 's':
        export_utils.export_scan_results(hosts)

def prediccion_dl():
    print(f"{CYAN}🧠 Predicción con LSTM...{RESET}")
    
    # Simular historial
    historial = [[50 + i * 2, 30 + i, i % 10, 1500 + i * 10] for i in range(20)]
    
    prediccion = deep_ai.predecir_trafico_futuro(historial)
    print(f"\n{BLUE}Predicción LSTM:{RESET}")
    print(json.dumps(prediccion, indent=2))

def deteccion_autoencoder():
    print(f"{CYAN}🔍 Detección con Autoencoder...{RESET}")
    
    metricas = [500, 200, 50, 2000]  # Datos sospechosos
    resultado = deep_ai.detectar_anomalia_dl(metricas)
    
    if resultado['es_anomalia']:
        print(f"{RED}🚨 ANOMALÍA DETECTADA!{RESET}")
        print(f"  Severidad: {resultado['severidad']}")
        print(f"  Error: {resultado['error_reconstruccion']:.3f}")
    else:
        print(f"{GREEN}✅ Tráfico normal{RESET}")

def iniciar_web():
    print(f"{GREEN}🌐 Iniciando servidor web...{RESET}")
    print(f"{YELLOW}Dashboard disponible en: http://localhost:5000{RESET}")
    print(f"{YELLOW}Presiona Ctrl+C para detener{RESET}")
    
    try:
        start_web_server()
    except KeyboardInterrupt:
        print(f"\n{RED}Servidor detenido{RESET}")

def main():
    # Entrenar IA
    if not ai_engine.is_trained:
        ai_engine.entrenar_modelos()
    
    if not deep_ai.is_trained:
        deep_ai.entrenar_con_datos_reales()
    
    mostrar_banner()
    
    while True:
        menu_principal()
        opcion = input(f"\n{CYAN}RedGhost>{RESET} ").strip()
        
        if opcion == "1":
            escaneo_puertos()
        elif opcion == "2":
            descubrimiento_hosts()
        elif opcion == "3":
            from redghost_old import analisis_trafico_ia
            analisis_trafico_ia()
        elif opcion == "4":
            from redghost_old import predecir_latencia_ia
            predecir_latencia_ia()
        elif opcion == "5":
            from redghost_old import deteccion_anomalias_ia
            deteccion_anomalias_ia()
        elif opcion == "6":
            prediccion_dl()
        elif opcion == "7":
            deteccion_autoencoder()
        elif opcion == "8":
            if input(f"{YELLOW}Exportar hosts o escaneo? (h/e): {RESET}") == 'h':
                descubrimiento_hosts()
            else:
                escaneo_puertos()
        elif opcion == "9":
            iniciar_web()
        elif opcion == "10":
            print(f"{GREEN}👻 ¡Hasta la vista, bro!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}❌ Opción inválida{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}⚠ Interrupción detectada{RESET}")
        sys.exit(0)
