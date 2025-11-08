# main.py
import serial
import threading
import time
from funcoes import ESPAlerta

# ======== CONFIGURAÇÃO SERIAL ========
ser = serial.Serial('COM3', 115200, timeout=1)

# ======== FUNÇÃO DE MONITORAMENTO SERIAL ========
def ler_serial():
    ESP = ESPAlerta()
    while True:
        try:
            sinal = ser.readline().decode(errors='ignore').strip()
            if sinal in ['UNIFBV', 'CRECHE1', 'CRECHE1 2']:
                print(f"🚨 Sinal de ALERTA recebido de {sinal}!")
                ESP.start(sinal)
        except Exception as e:
            print(f"[ERRO SERIAL] {e}")
        time.sleep(0.1)

# ======== THREAD DE MONITORAMENTO ========
thread_serial = threading.Thread(target=ler_serial, daemon=True)
thread_serial.start()

# ======== LOOP PRINCIPAL ========
print("🔴 Monitorando... aguardando ALERTA.")
while True:
    time.sleep(1)
