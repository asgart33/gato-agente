#!/bin/bash

# Script de inicio para Gato Agente en Render
set -e

echo "🐱 Iniciando Gato Agente..."
echo "PWD: $(pwd)"
echo "Archivos en raíz:"
ls -la

echo ""
echo "Archivos en src/:"
ls -la src/ 2>/dev/null || echo "❌ Carpeta src/ no encontrada"

echo ""
echo "Verificando Python:"
python --version
python -m pip --version

echo ""
echo "Instalando dependencias..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo ""
echo "Ejecutando Gato Agente..."
cd /opt/render/project
python -u src/main.py
