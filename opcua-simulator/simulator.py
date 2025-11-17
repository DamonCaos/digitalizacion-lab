"""
Esqueleto de servidor OPC UA simulado.

Requisitos:
  pip install opcua

NOTA: Este script es una base conceptual para que entiendas
cómo podría montarse un servidor OPC UA de pruebas. Ajusta
los endpoints, certificados y nodos a tu necesidad real.
"""

import time
import random
from opcua import Server

def main():
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/saargummi/simulator/")
    server.set_server_name("SaarGummi-OPCUA-Simulator")

    uri = "http://saargummi.local/opcua/simulator"
    idx = server.register_namespace(uri)

    objects = server.get_objects_node()
    prod_obj = objects.add_object(idx, "LineaExtrusion")

    temp_tag = prod_obj.add_variable(idx, "TempCabezal", 180.0)
    speed_tag = prod_obj.add_variable(idx, "VelocidadLinea", 10.0)
    scrap_tag = prod_obj.add_variable(idx, "ScrapPorcentaje", 1.0)

    temp_tag.set_writable()
    speed_tag.set_writable()
    scrap_tag.set_writable()

    server.start()
    print("Servidor OPC UA simulado en marcha. Ctrl+C para parar.")

    try:
        while True:
            temp = 180 + random.uniform(-5, 5)
            speed = 10 + random.uniform(-2, 2)
            scrap = max(0.0, min(10.0, 1 + random.uniform(-0.5, 0.5)))

            temp_tag.set_value(temp)
            speed_tag.set_value(speed)
            scrap_tag.set_value(scrap)

            time.sleep(2)
    finally:
        server.stop()

if __name__ == "__main__":
    main()
