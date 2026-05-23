#!/usr/bin/env python3
# export_utils.py - Exportación de resultados

import json
import csv
import os
from datetime import datetime

class ExportUtils:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def export_to_json(self, data, filename=None):
        """Exporta datos a JSON"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"redghost_export_{timestamp}.json"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Exportado a JSON: {filepath}")
        return filepath
    
    def export_to_csv(self, data, filename=None):
        """Exporta datos a CSV"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"redghost_export_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        if isinstance(data, list) and len(data) > 0:
            # Asumimos que es lista de diccionarios
            fieldnames = data[0].keys()
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        else:
            # Datos planos
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for row in data:
                    writer.writerow(row)
        
        print(f"✅ Exportado a CSV: {filepath}")
        return filepath
    
    def export_scan_results(self, scan_results):
        """Exporta resultados de escaneo en múltiples formatos"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON
        json_file = self.export_to_json(scan_results, f"scan_{timestamp}.json")
        
        # CSV
        if isinstance(scan_results, list) and len(scan_results) > 0:
            csv_file = self.export_to_csv(scan_results, f"scan_{timestamp}.csv")
        
        # También guardar resumen en TXT
        txt_file = os.path.join(self.output_dir, f"scan_{timestamp}.txt")
        with open(txt_file, 'w') as f:
            f.write(f"RedGhost Scan Report - {datetime.now()}\n")
            f.write("="*50 + "\n\n")
            f.write(json.dumps(scan_results, indent=2))
        
        print(f"✅ Exportado resumen a TXT: {txt_file}")
        
        return {
            'json': json_file,
            'csv': csv_file if 'csv_file' in locals() else None,
            'txt': txt_file
        }

# Instancia global
export_utils = ExportUtils()
