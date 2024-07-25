#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:19:49 2024

@author: sofiapansoni
"""

import subprocess

# Esegui il comando Streamlit
process = subprocess.Popen(['streamlit', 'run', 'app.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Leggi l'output del processo
for line in process.stdout:
    print(line.decode('utf-8'), end='')

for line in process.stderr:
    print(line.decode('utf-8'), end='')
