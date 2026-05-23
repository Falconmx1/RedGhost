#!/usr/bin/env python3
# web_interface.py - Interfaz web para RedGhost

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import threading
import json
from datetime import datetime
from network_ai import ai_engine
from deep_network_ai import deep_ai
from scanner import RealScanner
from host_discovery import HostDiscovery
from export_utils import export_utils

app = Flask(__name__)
CORS(app)

# Datos globales para el dashboard
dashboard_data = {
    'estado': 'activo',
    'alertas': [],
    'metricas_tiempo_real': [],
    'hosts_detectados': [],
    'predicciones_ia': {}
}

@app.route('/')
def index():
    """Dashboard principal"""
    return render_template('dashboard.html')

@app.route('/api/status')
def api_status():
    """API de estado del sistema"""
    return jsonify({
        'estado': dashboard_data['estado'],
        'timestamp': datetime.now().isoformat(),
        'ia_entrenada': ai_engine.is_trained,
        'dl_entrenado': deep_ai.is_trained
    })

@app.route('/api/scan', methods=['POST'])
def api_scan():
    """API para escaneo de red"""
    data = request.json
    target = data.get('target', '192.168.1.0/24')
    
    # Ejecutar escaneo en hilo separado
    def scan_thread():
        discovery = HostDiscovery()
        hosts = discovery.escaneo_completo()
        dashboard_data['hosts_detectados'] = hosts
        
        # Exportar resultados
        export_utils.export_scan_results(hosts)
    
    thread = threading.Thread(target=scan_thread)
    thread.start()
    
    return jsonify({'mensaje': 'Escaneo iniciado', 'status': 'running'})

@app.route('/api/hosts')
def api_hosts():
    """API para obtener hosts detectados"""
    return jsonify(dashboard_data['hosts_detectados'])

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API para predicción con Deep Learning"""
    data = request.json
    historial = data.get('historial', [])
    
    prediccion = deep_ai.predecir_trafico_futuro(historial)
    dashboard_data['predicciones_ia'] = prediccion
    
    return jsonify(prediccion)

@app.route('/api/anomaly', methods=['POST'])
def api_anomaly():
    """API para detección de anomalías"""
    data = request.json
    metricas = data.get('metricas', [0, 0, 0, 0])
    
    resultado = deep_ai.detectar_anomalia_dl(metricas)
    
    if resultado['es_anomalia']:
        dashboard_data['alertas'].append({
            'timestamp': datetime.now().isoformat(),
            'tipo': 'anomalia_dl',
            'severidad': resultado['severidad'],
            'error': resultado['error_reconstruccion']
        })
    
    return jsonify(resultado)

@app.route('/api/export', methods=['POST'])
def api_export():
    """API para exportar datos"""
    data = request.json
    tipo = data.get('tipo', 'json')
    datos = data.get('datos', [])
    
    if tipo == 'json':
        archivo = export_utils.export_to_json(datos)
    else:
        archivo = export_utils.export_to_csv(datos)
    
    return jsonify({'archivo': archivo, 'tipo': tipo})

@app.route('/api/metrics/realtime')
def api_realtime_metrics():
    """API para métricas en tiempo real (simuladas)"""
    import random
    
    metrica = {
        'timestamp': datetime.now().isoformat(),
        'throughput': random.uniform(10, 100),
        'packet_loss': random.uniform(0, 5),
        'latency': random.uniform(10, 200),
        'bandwidth_usage': random.uniform(0, 100)
    }
    
    dashboard_data['metricas_tiempo_real'].append(metrica)
    
    # Mantener solo últimas 100 métricas
    if len(dashboard_data['metricas_tiempo_real']) > 100:
        dashboard_data['metricas_tiempo_real'] = dashboard_data['metricas_tiempo_real'][-100:]
    
    return jsonify(metrica)

def start_web_server(port=5000):
    """Inicia el servidor web"""
    print(f"\n🌐 Servidor web iniciado en http://localhost:{port}")
    print("📊 Dashboard disponible en http://localhost:{port}/dashboard")
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

if __name__ == '__main__':
    start_web_server()
