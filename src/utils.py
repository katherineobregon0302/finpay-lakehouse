# utils.py
# Funciones reutilizables compartidas por los notebooks de Bronze, Silver y Gold

from datetime import datetime

def get_execution_time_id():
    """
    Genera un identificador único basado en la fecha y hora de ejecución.
    Formato: YYYYMMDD_HHMMSS
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def log_message(message, level="INFO"):
    """
    Imprime un mensaje con timestamp y nivel de log.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")
