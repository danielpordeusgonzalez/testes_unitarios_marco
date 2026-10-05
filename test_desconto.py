import os
from pathlib import Path
import runpy

import pytest


RAIZ = Path(__file__).resolve().parent
CODIGO = os.environ.get(
    "DESCONTO_CODIGO", "src/tech/danielpordeusg/operacoes/desconto.py"
)
calcular_desconto = runpy.run_path(str(RAIZ / CODIGO))["calcular_desconto"]


@pytest.mark.parametrize(
    "valor_compra,tipo_cliente,esperado",
    [
        (0, "COMUM", 0),
        (0, "VIP", 0),
        (50, "COMUM", 0),
        (50, "VIP", 2.50),
        (99.99, "COMUM", 0),
        (99.99, "VIP", 5.00),
        (100, "COMUM", 10.00),
        (100, "VIP", 15.00),
        (100.01, "COMUM", 10.00),
        (100.01, "VIP", 15.00),
        (250, "COMUM", 25.00),
        (250, "VIP", 37.50),
        (499.99, "COMUM", 50.00),
        (499.99, "VIP", 75.00),
        (500, "COMUM", 100.00),
        (500, "VIP", 125.00),
        (500.01, "COMUM", 100.00),
        (500.01, "VIP", 125.00),
        (600, "COMUM", 120.00),
        (600, "VIP", 150.00),
        (999.90, "COMUM", 199.98),
        (1000, "COMUM", 200.00),
        (1000.10, "COMUM", 200.00),
        (799.80, "VIP", 199.95),
        (800, "VIP", 200.00),
        (800.20, "VIP", 200.00),
        (10000, "COMUM", 200.00),
        (10000, "VIP", 200.00),
    ],
)
def test_desconto_por_faixa_e_teto(valor_compra, tipo_cliente, esperado):
    assert calcular_desconto(valor_compra, tipo_cliente) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "tipo_cliente", ["VIP", "VIp", "ViP", "Vip", "vIP", "vIp", "viP", "vip"]
)
@pytest.mark.parametrize("valor_compra,esperado", [(50, 2.50), (200, 30.00), (600, 150.00)])
def test_vip_independente_de_maiusculas(valor_compra, esperado, tipo_cliente):
    assert calcular_desconto(valor_compra, tipo_cliente) == pytest.approx(esperado)
