"""Executa os mesmos testes contra o original reproduzido e o codigo corrigido."""

import os
from pathlib import Path
import subprocess
import sys


RAIZ = Path(__file__).resolve().parent
EVIDENCIAS = RAIZ / "evidencias"


def executar(nome, titulo, codigo):
    ambiente = os.environ.copy()
    ambiente["DESCONTO_CODIGO"] = codigo
    ambiente["PYTHONIOENCODING"] = "utf-8"
    resultado = subprocess.run(
        [sys.executable, "-m", "pytest", "test_desconto.py", "-v", "--tb=short", "--color=no", "-p", "no:cacheprovider"],
        cwd=RAIZ,
        env=ambiente,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    relatorio = f"{titulo}\nCodigo testado: {codigo}\n\n{resultado.stdout}{resultado.stderr}"
    (EVIDENCIAS / f"{nome}.txt").write_text(relatorio, encoding="utf-8")
    print(relatorio)
    return resultado.returncode


if __name__ == "__main__":
    original = executar(
        "PRINT1",
        "PRINT1 - REPRODUCAO com o codigo original do enunciado (com bugs)",
        "evidencias/desconto_original.py",
    )
    corrigido = executar(
        "PRINT2",
        "PRINT2 - Execucao com o codigo corrigido",
        "src/tech/danielpordeusg/operacoes/desconto.py",
    )
    if original != 1 or corrigido != 0:
        sys.exit("Resultado inesperado: confira os relatorios.")
