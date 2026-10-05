# Testes da atividade

O codigo principal corrigido esta em `src/tech/danielpordeusg/operacoes/desconto.py`.
Os 52 casos em `test_desconto.py` verificam faixas, limites, categorias, as oito
combinacoes de maiusculas/minusculas de VIP e o teto de R$ 200,00.
Resultados com centavos seguem o arredondamento do codigo fornecido.
Entradas invalidas nao possuem comportamento definido nos criterios de aceite;
seu tratamento precisa ser esclarecido antes de acrescentar testes de aceitacao.

## Execucao no PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe executar_relatorios.py
```

O script executa exatamente os mesmos testes contra duas implementacoes:

- `evidencias/desconto_original.py`: reproducao do original do enunciado.
  Resultado: 23 testes falham e 29 passam.
- Codigo principal corrigido: os 52 testes passam.

O codigo principal ja havia sido corrigido antes da criacao dos testes.
Portanto, PRINT1 registra uma reproducao posterior com o original do enunciado,
e nao uma captura historica anterior a correcao.

Os relatorios reais sao salvos em `evidencias/PRINT1.txt` e `evidencias/PRINT2.txt`.
Esses arquivos sao texto: para a entrega, tire capturas de tela dos resultados
e salve como PRINT1.png e PRINT2.png. Inclua os testes e o resumo final.

Para testar apenas o codigo principal corrigido:

```powershell
.\.venv\Scripts\python.exe -m pytest test_desconto.py -v -p no:cacheprovider
```
