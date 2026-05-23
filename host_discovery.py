#!/usr/bin/env python3
# host_discovery.py - Descubrimiento de hosts en red local

import subprocess
import socket
import threading
import ipaddress
import time
from scapy.all import ARP, Ether, srp

class HostDiscovery:
    def __init__(self):
        self.hosts_encontrados = []
        
    def get_local_ip(self):
        """Obtiene IP local"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"
    
    def get_network_range(self):
        """Determina el rango de red automáticamente"""
        ip = self.get_local_ip()
        # Asume /24 (máscara 255.255.255.0)
        ip_parts = ip.split('.')
        network = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
        return network
    
    def arp_scan(self, network_range=None):
        """Escaneo ARP para descubrir hosts (rápido y efectivo)"""
        if network_range is None:
            network_range = self.get_network_range()
        
        print(f"[*] Escaneando red: {network_range}")
        
        # Crear paquete ARP
        arp = ARP(pdst=network_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        
        # Enviar paquete y recibir respuestas
        result = srp(packet, timeout=3, verbose=0)[0]
        
        hosts = []
        for sent, received in result:
            hosts.append({
                'ip': received.psrc,
                'mac': received.hwsrc,
                'vendor': self.get_vendor_from_mac(received.hwsrc)
            })
        
        self.hosts_encontrados = hosts
        return hosts
    
    def ping_scan(self, network_range=None):
        """Escaneo ICMP ping sweep complementario"""
        if network_range is None:
            network_range = self.get_network_range()
        
        network = ipaddress.ip_network(network_range)
        hosts = []
        
        def ping_host(ip):
            try:
                result = subprocess.run(
                    ['ping', '-c', '1', '-W', '1', ip],
                    capture_output=True,
                    timeout=2
                )
                if result.returncode == 0:
                    hosts.append({'ip': ip, 'metodo': 'icmp'})
            except:
                pass
        
        hilos = []
        for ip in network.hosts():
            hilo = threading.Thread(target=ping_host, args=(str(ip),))
            hilos.append(hilo)
            hilo.start()
            
            if len(hilos) >= 100:
                for h in hilos:
                    h.join()
                hilos = []
        
        for h in hilos:
            h.join()
        
        return hosts
    
    def get_vendor_from_mac(self, mac):
        """Identifica vendor por MAC (versión simplificada)"""
        mac_prefix = mac[:8].upper()
        vendors = {
            '00:00:0C': 'Cisco',
            '00:14:22': 'Dell',
            '00:16:3E': 'Xen',
            '00:1A:11': 'Samsung',
            '00:1B:21': 'Apple',
            '00:25:9C': 'HP',
            '08:00:27': 'Oracle/VirtualBox',
            'B8:27:EB': 'Raspberry Pi',
            'DC:A6:32': 'Google',
            'F0:18:98': 'Intel'
        }
        
        for prefix, vendor in vendors.items():
            if mac.startswith(prefix):
                return vendor
        return 'Desconocido'
    
    def escaneo_completo(self):
        """Realiza escaneo completo con múltiples métodos"""
        print("\n🔍 Iniciando descubrimiento de hosts...")
        
        # Método 1: ARP scan
        hosts_arp = self.arp_scan()
        print(f"\n📡 ARP Scan: {len(hosts_arp)} hosts encontrados")
        
        # Método 2: Ping sweep complementario
        hosts_ping = self.ping_scan()
        print(f"📡 Ping Sweep: {len(hosts_ping)} hosts encontrados")
        
        # Combinar resultados sin duplicados
        all_ips = set()
        resultado_final = []
        
        for host in hosts_arp:
            if host['ip'] not in all_ips:
                all_ips.add(host['ip'])
                resultado_final.append(host)
        
        for host in hosts_ping:
            if host['ip'] not in all_ips:
                all_ips.add(host['ip'])
                resultado_final.append({'ip': host['ip'], 'mac': 'N/A', 'vendor': 'Desconocido'})
        
        self.hosts_encontrados = resultado_final
        return resultado_final
