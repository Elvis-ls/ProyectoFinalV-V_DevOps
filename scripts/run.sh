#!/bin/bash
# Script para ejecutar la aplicación en diferentes modos
MODE=${1:-dev}

if [ "$MODE" == "test" ]; then
    echo "Ejecutando en modo TEST..."
    docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit
else
    echo "Ejecutando en modo DESARROLLO..."
    docker-compose up -d
fi
