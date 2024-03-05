# Monitorar Ativos e Notificar via Telegram
- Este script Python monitora o valor de um ativo financeiro usando a biblioteca yfinance e envia uma notificação via Telegram quando o valor do ativo atinge um limite desejado.
- O script realiza verificações a cada 10 minutos durante o horário configurado.

### Configuração
Instalação de Dependências:
Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalá-las usando o seguinte comando:
```bash
pip install requests yfinance
``` 

### Configuração do Telegram:

Obtenha uma chave de API (token) para o seu bot no Telegram.
Substitua a variável CHAVE_API no script com a chave do seu bot.
Substitua BOT_CHAT_ID pelo ID do chat do seu bot.
- [Token telegram](https://helpdesk.bitrix24.com.br/open/17643424/)

### Configuração do Ativo:
Defina o nome do ativo (```nome_ativo```) e o valor desejado para notificação (```valor_desejado```).

### Horário de Execução:
Configure o horário inicial e final (```hora_inicial``` e ```hora_final```) para a execução da verificação.
### Execução
Execute o script Python usando o seguinte comando:

```bash
python nome_do_script.py
``` 

Certifique-se de ter o Python instalado em seu ambiente.
