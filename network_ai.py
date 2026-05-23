#!/usr/bin/env python3
# network_ai.py - Modelo de IA para análisis de red con scikit-learn

import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import os
import random

class NetworkAI:
    def __init__(self):
        self.rf_model = None
        self.isolation_forest = None
        self.latency_model = None
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def entrenar_modelos(self):
        """Entrena modelos con datos sintéticos (en producción usar datos reales)"""
        print("[IA] Entrenando modelos de Machine Learning...")
        
        # 1. RandomForest para clasificar tráfico normal vs anomalía
        X_train = np.array([
            [50, 10, 1, 100],    # normal
            [45, 8, 0, 95],      # normal
            [55, 12, 2, 105],    # normal
            [500, 500, 50, 1000], # ataque DDoS
            [1000, 800, 100, 2000], # ataque DDoS
            [2, 500, 80, 50],      # anomalía
        ])
        y_train = [0, 0, 0, 1, 1, 1]  # 0=normal, 1=anomalía
        
        self.rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.rf_model.fit(X_train, y_train)
        
        # 2. Isolation Forest para detección de outliers
        X_outliers = np.array([
            [40, 5, 0, 90],
            [45, 6, 0, 95],
            [44, 5, 0, 92],
            [600, 400, 60, 1500],
            [800, 600, 90, 1800],
        ])
        self.isolation_forest = IsolationForest(contamination=0.2, random_state=42)
        self.isolation_forest.fit(X_outliers)
        
        # 3. Regresión lineal para predicción de latencia
        X_latency = np.array([[10], [20], [30], [50], [100], [150], [200]])
        y_latency = np.array([15, 28, 42, 68, 135, 198, 265])
        self.latency_model = LinearRegression()
        self.latency_model.fit(X_latency, y_latency)
        
        self.is_trained = True
        print("[IA] ✅ Modelos entrenados correctamente")
    
    def clasificar_trafico(self, packet_size, packets_per_sec, tcp_retransmits, total_bytes):
        """Clasifica si el tráfico es normal o anomalía usando RandomForest"""
        if not self.is_trained:
            self.entrenar_modelos()
        
        features = np.array([[packet_size, packets_per_sec, tcp_retransmits, total_bytes]])
        prediccion = self.rf_model.predict(features)[0]
        probabilidad = self.rf_model.predict_proba(features)[0]
        
        return {
            'es_anomalia': bool(prediccion),
            'confianza': float(max(probabilidad)),
            'prob_normal': float(probabilidad[0]),
            'prob_anomalia': float(probabilidad[1])
        }
    
    def detectar_outlier(self, metricas):
        """Detecta outliers usando Isolation Forest"""
        if not self.is_trained:
            self.entrenar_modelos()
        
        # metricas: throughput, packet_loss, jitter, tcp_retransmits
        features = np.array([metricas]).reshape(1, -1)
        resultado = self.isolation_forest.predict(features)[0]
        
        return resultado == -1  # -1 es outlier
    
    def predecir_latencia(self, distancia_km):
        """Predice latencia basada en distancia geográfica aproximada"""
        if not self.is_trained:
            self.entrenar_modelos()
        
        prediccion = self.latency_model.predict([[distancia_km]])[0]
        return max(0, prediccion)
    
    def analizar_patron_tiempo_real(self, historial_paquetes):
        """Analiza patrón de paquetes en tiempo real"""
        if len(historial_paquetes) < 10:
            return {"estado": "insufficient_data", "mensaje": "Necesito más datos"}
        
        medias = np.mean(historial_paquetes, axis=0)
        desviaciones = np.std(historial_paquetes, axis=0)
        
        # Detectar cambios bruscos
        anomalias_detectadas = []
        if desviaciones[1] > 100:  # packets_per_sec muy variable
            anomalias_detectadas.append("Tráfico intermitente detectado")
        if medias[0] > 500:  # packet_size muy grande
            anomalias_detectadas.append("Paquetes de gran tamaño inusuales")
        if medias[2] > 20:  # muchas retransmisiones TCP
            anomalias_detectadas.append("Posible pérdida de paquetes o ataque")
        
        return {
            "estado": "anomalia" if anomalias_detectadas else "normal",
            "alertas": anomalias_detectadas,
            "media_packet_size": float(medias[0]),
            "media_pps": float(medias[1]),
            "media_retransmisiones": float(medias[2])
        }

# Instancia global
ai_engine = NetworkAI()
