#!/usr/bin/env bash
# Roda uma vez, quando o codespace é criado
set -euo pipefail

pip install -r requirements.txt

# O pre-commit só é ativado quando o projeto já tem a configuração (aula de padrões em diante)
if [ -f .pre-commit-config.yaml ]; then
  pre-commit install
  pre-commit install-hooks
fi
