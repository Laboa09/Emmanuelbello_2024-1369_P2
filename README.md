# Emmanuelbello_2024-1369_P2

⚠️ Uso estrictamente educativo / laboratorio

Este repositorio contiene material desarrollado únicamente para prácticas académicas en un entorno aislado y controlado.
No debe usarse en redes/sistemas reales ni sin autorización explícita.
El autor no promueve el uso indebido y asume que cualquier ejecución será con permiso.


Práctica 1: Ataque DoS con CDP

Video de Demostración
https://youtu.be/zPP2iGL8FP4
---

1. Descripción del Ataque
Este proyecto implementa un ataque de Denegación de Servicio (DoS) dirigido al protocolo CDP (Cisco Discovery Protocol). 

El script genera miles de paquetes CDP falsificados con direcciones MAC de origen y nombres de dispositivo aleatorios (`FakeDevice_XXXX`). Esto satura la tabla de vecinos del Switch objetivo, consumiendo su memoria y dificultando la administración de la red.

2. Entorno de Laboratorio (Topología)
Atacante: Ubuntu Desktop 20.04 (Virtualizado en PNETLab).
    Herramienta: Python 3 + Scapy.
    Interfaz: `ens3`.
Víctima: Switch Cisco vIOS (L2).
 Red: 192.168.10.0/24.

3. Requisitos y Ejecución

Prerrequisitos
Se requiere tener instalada la librería Scapy:
```bash
sudo pip3 install scapy

Comando de Ejecución
El script debe ejecutarse con privilegios de superusuario para poder inyectar paquetes en la interfaz de red:

sudo python3 cdp_dos.py




4. Evidencia de Funcionamiento
Antes del ataque, la tabla de vecinos del Switch muestra solo los dispositivos legítimos. Durante la ejecución del script, la tabla se inunda con entradas falsas:
 
 

5. Medidas de Mitigación 
Para proteger la infraestructura de red contra este tipo de ataques, se recomiendan las siguientes configuraciones en los dispositivos Cisco:

Deshabilitar CDP Globalmente: Si el protocolo no es estrictamente necesario. “no cdp run”

Deshabilitar CDP por Interfaz: En puertos conectados a usuarios finales o dispositivos no confiables. 
“Interface gig0/1
no cdp Enable”


