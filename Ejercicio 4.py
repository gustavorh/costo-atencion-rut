#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 22:27:14 2021

Nombre: Gustavo Reyes Herrera
RUT: 21023531-0

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

def costo_total_paciente(rut_paciente):
    dicc_ruts = {}
    with open("atenciones.txt", "r") as atenciones:
        for atencion in atenciones:
            ruts = atencion.strip().split(":")[0]
            costo = atencion.strip().split(":")[2]
            
            if ruts not in dicc_ruts:
                print(f"{ruts} no existe, agregandolo")
                dicc_ruts[ruts] = costo
            else:
                print(f"{ruts} ya existe, sumando costo")
                dicc_ruts[ruts] += costo
        
        print(dicc_ruts)
        
    pass

rut = input("Ingrese el RUT del paciente: ")
costo_total = costo_total_paciente(rut)