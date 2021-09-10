# Richwatch

Richwatch é um script python que faz consultas à API da Binance para ober um resumo do seu saldo na carteira Spot.

## Exemplo de saída

```
Richwatch 0.1
 Data from: 2021-09-08 20:59:59
  ADA: US$ 166.09 = 65.52 @ US$ 1.53
  BTC: US$ 560.75 = 900.02 @ US$ 86553.61
  CAKE: US$ 63.91 = 2.12 @ US$ 300.12
  ETH: US$ 102.51 = 0.99 @ US$ 3256.19
  USDT: US$ 0.18 = 0.22 @ US$ 1.00
  SOL: US$ 33.56 = 100.40 @ US$ 0.33
Total: US$ 4230.00 / R$ 912.47
```
Nota: Os valores numéricos do exemplo são aleatórios

## Requisitos

O script utiliza o `python-binance` para as consultas. Para gerar novos pacotes e "compilado" são utilizados o fpm e o pyinstaller.

## Instruções

### Build

O script `build.sh` incluído gerará um pacote .deb e um "binário" numa pasta dist dentro do diretório de trabalho

### Uso

Fornecer as variáveis de ambiente BINANCEAPI e BINANCESECRET no momento da execução. O relatório será impresso para o STDOUT.
O formato de saída é conciso de forma que possa se enviado a mensageiro como telegram. Segue exemplo:

```
#!/bin/bash

BINANCEKEY="lkjnlJNLAJSjYLJKEYH987987a9o987a98wueqbajbs8d76AKJNkqwea98912kjnkan" BINANCESECRET="lkm1283HKLJ1291823j1o28uoLKJ98u12l3kjLKJNlkj2312378klajsdl" /usr/local/bin/richwatch | /usr/local/bin/telegram-send --pre --stdin
```

O script acima pode ser executado via CRON para emitir relatórios periodicamente.



## Licença

Copyright (C) 2021 Renato Rodrigues Zippert

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
