#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is reboot IPv4 phones.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Develop"


import os
from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException


# Colores para impresion de pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
green = "\x1b[00;00;1;092m"
blue = "\x1b[00;00;1;034m"


def ssh_alive(ip):
    """
    Funcion para establecer que dispositivos son alcanzados por SSH.

    Esta funcion realiza una conexion SSH a los dispositivos, si es exitosa,
    guarda el resultado en un archivo para su posterior tratamiento.
    """
    ipv4_phone = {
                "device_type": "generic_termserver",    # Tipo de dispositivo.
                "ip": ip,                               # IP Address.
                "username": "admin",                    # Nombre de Usuario.
                "password": "(@Esperanza86)*"           # Password de usuario.
                }

    try:
        # Llamada a la funcion Netmiko y agregarla al variable net_connect
        net_connect = Netmiko(**ipv4_phone)

        if net_connect.is_alive():
            print(
                f"\t{red}La Conexion {blue}SSH {red}con "
                + f"{blue}{ip} {red}es {blue}permitida.{color_reset}")

            # Obtener el directorio actual
            directory = os.getcwd()
            # Abrir "crear el archivo ssh_alive_IP".
            f = open(file=f"{directory}/tmp/ssh_alive_{ip}", mode="a")
            # Escribir la ip en el arcivo.
            f.write(f"{ip}")
            # Cerrar el archivo.
            f.close()

        else:
            print(
                f"\t{red}La Conexion {blue}SSH {red}con "
                + f"{blue}{ip} {red}no es {blue}permitida.{color_reset}")

        # Fin de la conexion
        net_connect.disconnect()

    except NetMikoTimeoutException:
        # print(error)
        print(
            f"\t{red}El dispositivo {blue}{ip} "
            + f"{red}no esta {blue}disponible.{color_reset}")

    except NetMikoAuthenticationException:
        print(
            f"\t{red}Contraseña {blue}incorrecta {red}para {blue}{ip}")