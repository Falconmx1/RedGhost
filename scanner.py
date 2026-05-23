#!/usr/bin/env python3
# scanner.py - Escaneo de puertos real con Scapy

import socket
import threading
import time
from scapy.all import IP, TCP, sr1, conf

conf.verb = 0  # Modo silencioso

class RealScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.puertos_abiertos = []
        
    def scan_port_tcp(self, port, timeout=2):
        """Escaneo TCP SYN real"""
        try:
            # SYN packet
            pkt = IP(dst=self.target_ip)/TCP(dport=port, flags="S")
            respuesta = sr1(pkt, timeout=timeout, verbose=False)
            
            if respuesta and respuesta.haslayer(TCP):
                if respuesta.getlayer(TCP).flags == 0x12:  # SYN-ACK
                    return True, "Abierto"
                elif respuesta.getlayer(TCP).flags == 0x14:  # RST
                    return False, "Cerrado"
            return False, "Filtrado"
        except Exception:
            return False, "Error"
    
    def escanear_puertos(self, puertos=None, max_hilos=50):
        """Escanea múltiples puertos con hilos"""
        if puertos is None:
            puertos = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 
                       993, 995, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443]
        
        print(f"[*] Escaneando {len(puertos)} puertos en {self.target_ip}...")
        
        resultados = {}
        
        def scan_worker(port):
            estado, desc = self.scan_port_tcp(port)
            if estado:
                resultados[port] = desc
                print(f"  [+] Puerto {port} - {desc}")
            else:
                print(f"  [-] Puerto {port} - {desc}")
        
        # Hilos para escaneo rápido
        hilos = []
        for port in puertos:
            hilo = threading.Thread(target=scan_worker, args=(port,))
            hilos.append(hilo)
            hilo.start()
            
            # Control de hilos máximos concurrentes
            if len(hilos) >= max_hilos:
                for h in hilos:
                    h.join()
                hilos = []
        
        # Esperar hilos restantes
        for h in hilos:
            h.join()
        
        self.puertos_abiertos = list(resultados.keys())
        return resultados
    
    def servicio_predicho(self, puerto):
        """Predice servicio basado en puerto usando IA"""
        servicios = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S", 1723: "PPTP",
            3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC", 6379: "Redis",
            8080: "HTTP-Alt", 8443: "HTTPS-Alt"
        }
        return servicios.get(puerto, "Desconocido")
