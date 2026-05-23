#!/usr/bin/env python3
# RedGhost - Herramienta de IA REAL para análisis de red

import sys
import time
import random
import subprocess
from colorama import init, Fore, Style
from network_ai import ai_engine
from scanner import RealScanner

init(autoreset=True)

# Colores
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

def mostrar_banner():
    banner = f"""
{GREEN}╔═══════════════════════════════════════════════════════════════════════╗
║  {RED}██████╗ {BLUE}███████╗{YELLOW}██████╗ {GREEN} ██████╗ {CYAN}██╗  ██╗{MAGENTA} ███████╗{RESET}                    ║
║  {RED}██╔══██╗{BLUE}██╔════╝{YELLOW}██╔══██╗{GREEN}██╔════╝ {CYAN}██║  ██║{MAGENTA}██╔════╝{RESET}                    ║
║  {RED}██████╔╝{BLUE}█████╗  {YELLOW}██║  ██║{GREEN}██║  ███╗{CYAN}███████║{MAGENTA}█████╗  {RESET}                    ║
║  {RED}██╔══██╗{BLUE}██╔══╝  {YELLOW}██║  ██║{GREEN}██║   ██║{CYAN}██╔══██║{MAGENTA}██╔══╝  {RESET}                    ║
║  {RED}██║  ██║{BLUE}███████╗{YELLOW}██████╔╝{GREEN}╚██████╔╝{CYAN}██║  ██║{MAGENTA}███████╗{RESET}                    ║
║  {RED}╚═╝  ╚═╝{BLUE}╚══════╝{YELLOW}╚═════╝ {GREEN} ╚═════╝ {CYAN}╚═╝  ╚═╝{MAGENTA}╚══════╝{RESET}                    ║
║                                                                           ║
║     {CYAN}RedGhost - IA para Redes v2.0 (Real ML){RESET}                             ║
║     {YELLOW}RandomForest | IsolationForest | Scapy{RESET}                            ║
╚═══════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(banner)

def menu_principal():
    print(f"\n{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{GREEN}[1]{RESET} Escaneo de puertos REAL con Scapy + IA predictiva")
    print(f"{GREEN}[2]{RESET} Análisis de tráfico en tiempo real (RandomForest)")
    print(f"{GREEN}[3]{RESET} Predicción de latencia (Regresión Lineal)")
    print(f"{GREEN}[4]{RESET} Detección de anomalías (Isolation Forest)")
    print(f"{GREEN}[5]{RESET} Análisis de patrón de paquetes")
    print(f"{GREEN}[6]{RESET} Entrenar modelos IA con nuevos datos")
    print(f"{GREEN}[7]{RESET} Salir")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def escaneo_real_con_ia():
    ip = input(f"{CYAN}🌐 Ingresa IP objetivo: {RESET}")
    if not ip:
        print(f"{RED}❌ IP inválida{RESET}")
        return
    
    print(f"{YELLOW}🤖 Inicializando IA para escaneo predictivo...{RESET}")
    scanner = RealScanner(ip)
    
    # Escaneo real
    resultados = scanner.escanear_puertos()
    
    # Predicciones IA sobre los puertos encontrados
    print(f"\n{CYAN}🧠 Analizando resultados con IA...{RESET}")
    for puerto in scanner.puertos_abiertos:
        servicio_predicho = scanner.servicio_predicho(puerto)
        print(f"  {GREEN}✓ Puerto {puerto}{RESET} → {YELLOW}{servicio_predicho}{RESET}")
        
        # Recomendación IA
        if puerto in [22, 3389, 5900]:
            print(f"    {BLUE}🤖 IA: Alto riesgo si está expuesto a internet{RESET}")
        elif puerto in [80, 443, 8080]:
            print(f"    {BLUE}🤖 IA: Servicio web - recomienda WAF{RESET}")
    
    print(f"\n{GREEN}✅ Escaneo completado. {len(scanner.puertos_abiertos)} puertos abiertos encontrados.{RESET}")

def analisis_trafico_ia():
    print(f"{YELLOW}📡 Capturando tráfico simulado para análisis...{RESET}")
    
    # Simular métricas de red reales
    metricas = []
    for _ in range(20):
        metricas.append({
            'packet_size': random.randint(40, 1500),
            'packets_per_sec': random.randint(1, 500),
            'tcp_retransmits': random.randint(0, 30),
            'total_bytes': random.randint(100, 5000)
        })
    
    print(f"\n{CYAN}🧠 Ejecutando RandomForest Classifier...{RESET}")
    for i, m in enumerate(metricas[:5]):  # Mostrar primeras 5
        resultado = ai_engine.clasificar_trafico(
            m['packet_size'], m['packets_per_sec'], 
            m['tcp_retransmits'], m['total_bytes']
        )
        
        estado = f"{RED}⚠ ANOMALÍA{RESET}" if resultado['es_anomalia'] else f"{GREEN}✓ NORMAL{RESET}"
        print(f"  Muestra {i+1}: {estado} (confianza: {resultado['confianza']*100:.1f}%)")
    
    # Estadísticas generales
    anomalias = sum(1 for m in metricas if ai_engine.clasificar_trafico(
        m['packet_size'], m['packets_per_sec'], m['tcp_retransmits'], m['total_bytes']
    )['es_anomalia'])
    
    print(f"\n{BLUE}📊 Reporte IA:{RESET}")
    print(f"  Total muestras: {len(metricas)}")
    print(f"  Anomalías detectadas: {anomalias}")
    print(f"  Tasa de anomalía: {(anomalias/len(metricas))*100:.1f}%")

def predecir_latencia_ia():
    print(f"{CYAN}📡 Predicción de latencia usando Regresión Lineal{RESET}")
    print(f"{YELLOW}Ingresa distancia aproximada al servidor (km):{RESET}")
    
    try:
        distancia = float(input(f"{CYAN}> {RESET}"))
        latencia_predicha = ai_engine.predecir_latencia(distancia)
        
        print(f"\n{BLUE}🤖 IA Predice:{RESET}")
        print(f"  Distancia: {distancia} km")
        print(f"  Latencia estimada: {latencia_predicha:.1f} ms")
        
        if latencia_predicha < 30:
            print(f"  {GREEN}✅ Excelente - Ideal para gaming/streaming{RESET}")
        elif latencia_predicha < 100:
            print(f"  {YELLOW}⚠ Aceptable - Navegación web normal{RESET}")
        else:
            print(f"  {RED}❌ Mala - Posible congestión o satélite{RESET}")
    except ValueError:
        print(f"{RED}❌ Ingresa un número válido{RESET}")

def deteccion_anomalias_ia():
    print(f"{YELLOW}🔍 Ejecutando Isolation Forest para detección de outliers...{RESET}")
    
    # Simular métricas de red
    metricas_ejemplo = [
        [50, 2, 5, 100],    # normal
        [45, 1, 3, 95],     # normal
        [55, 3, 4, 110],    # normal
        [600, 400, 60, 2000], # outlier (posible ataque)
        [800, 600, 90, 3000], # outlier
        [48, 2, 3, 102],    # normal
        [1000, 500, 150, 5000] # outlier severo
    ]
    
    for i, m in enumerate(metricas_ejemplo):
        es_outlier = ai_engine.detectar_outlier(m)
        if es_outlier:
            print(f"  {RED}🚨 Muestra {i+1}: OUTLIER DETECTADO{RESET}")
            print(f"     Valores: packet_size={m[0]}, pps={m[1]}, retrans={m[2]}, bytes={m[3]}")
        else:
            print(f"  {GREEN}✓ Muestra {i+1}: Normal{RESET}")

def analisis_patron_paquetes():
    print(f"{YELLOW}📊 Analizando patrón de paquetes en tiempo real...{RESET}")
    
    # Simular historial de paquetes
    historial = []
    for _ in range(30):
        historial.append([
            random.randint(40, 1500),  # packet_size
            random.randint(1, 300),     # packets_per_sec
            random.randint(0, 15),      # tcp_retransmits
            random.randint(50, 2000)    # total_bytes
        ])
    
    # Insertar algunas anomalías
    historial[5] = [1400, 500, 50, 5000]
    historial[12] = [800, 400, 30, 3000]
    
    resultado = ai_engine.analizar_patron_tiempo_real(historial)
    
    print(f"\n{BLUE}📈 Análisis de patrón:{RESET}")
    print(f"  Estado: {resultado['estado'].upper()}")
    print(f"  Tamaño promedio de paquete: {resultado['media_packet_size']:.1f} bytes")
    print(f"  Paquetes por segundo promedio: {resultado['media_pps']:.1f}")
    print(f"  Retransmisiones TCP promedio: {resultado['media_retransmisiones']:.1f}")
    
    if resultado['alertas']:
        print(f"\n{RED}⚠ ALERTAS:{RESET}")
        for alerta in resultado['alertas']:
            print(f"  - {alerta}")
    else:
        print(f"\n{GREEN}✅ Patrón normal - No se detectaron anomalías{RESET}")

def entrenar_modelos():
    print(f"{YELLOW}🧠 Reentrenando modelos de IA con nuevos datos...{RESET}")
    ai_engine.entrenar_modelos()
    print(f"{GREEN}✅ Modelos actualizados y guardados{RESET}")

def main():
    # Entrenar IA al inicio
    if not ai_engine.is_trained:
        ai_engine.entrenar_modelos()
    
    mostrar_banner()
    
    while True:
        menu_principal()
        opcion = input(f"\n{CYAN}RedGhost>{RESET} ").strip()
        
        if opcion == "1":
            escaneo_real_con_ia()
        elif opcion == "2":
            analisis_trafico_ia()
        elif opcion == "3":
            predecir_latencia_ia()
        elif opcion == "4":
            deteccion_anomalias_ia()
        elif opcion == "5":
            analisis_patron_paquetes()
        elif opcion == "6":
            entrenar_modelos()
        elif opcion == "7":
            print(f"{GREEN}👻 ¡Hasta la vista, bro! RedGhost se retira...{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}❌ Opción no válida{RESET}")
        
        input(f"\n{YELLOW}Presiona Enter para continuar...{RESET}")

if __name__ == "__main__":
    # Verificar permisos (scapy necesita root para algunos escaneos)
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}⚠ Interrupción detectada. Saliendo...{RESET}")
        sys.exit(0)
