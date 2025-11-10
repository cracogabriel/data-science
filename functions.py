"""Funções utilitárias para checagem de datasets.

Contém a função `verify_csvs` que valida a existência de arquivos CSV em um
diretório de dados e opcionalmente encerra a execução com erro se algum
arquivo estiver faltando.
"""
from __future__ import annotations

from pathlib import Path
import sys
from typing import List, Optional


def verify_csvs(data_dir: str | Path = 'data', required: Optional[List[str]] = None, exit_on_missing: bool = True) -> List[str]:
    """Verifica se os arquivos CSV obrigatórios existem em `data_dir`.

    Args:
        data_dir: Caminho para a pasta de dados (padrão: 'data').
        required: Lista de nomes de arquivos obrigatórios. Se None, usa a lista padrão.
        exit_on_missing: Se True, imprime mensagem de erro e chama sys.exit(1) quando houver arquivos faltando.

    Returns:
        Lista de nomes de arquivos que estão faltando (vazia se todos existentes).
    """
    if required is None:
        required = ['all_data.csv', 'id_name.csv', 'steam_app_data.csv']

    base = Path(data_dir)
    missing: List[str] = []
    for name in required:
        if not (base / name).exists():
            missing.append(name)

    if missing and exit_on_missing:
        msg = f"Erro: arquivos ausentes em {base}: {missing}"
        print(msg)
        # interrompe a execução com código de saída 1
        sys.exit(1)

    return missing
