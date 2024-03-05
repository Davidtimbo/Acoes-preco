from requests import get
import time
import datetime
import yfinance as yf

nome_ativo = "BBDC4.SA"  # Adicione o sufixo '.SA' ao nome do ativo
valor_desejado = 15.00   # valor para notificação

# Definindo o horário inicial e final para a execução da verificação
hora_inicial = datetime.time(10, 0) # 10:00
hora_final = datetime.time(17, 0)   # 17:00

# Função para enviar mensagem pelo Telegram
def msg_telegram(nome_ativo):
    CHAVE_API = "6412459532:AAHoLtbHX6Gupjkxk-XMWeF3pOqnEfSl7MU"
    BOT_CHAT_ID = 1067817885

    # Obtendo o valor atual do ativo usando a biblioteca yfinance
    valor_atual = yf.Ticker(nome_ativo).history(period='1d')  # Alterado o período para '1d'
    
    # Verificando se há dados na série antes de acessar o último elemento
    if not valor_atual.empty:
        valor_atual_atualizado = valor_atual['Close'].iloc[-1]

        if valor_atual_atualizado <= valor_desejado:
            mensagem = f"Abra sua corretora!\nO {str(nome_ativo.upper())} CAIU!\nÓtima oportunidade!\nValor atual {valor_atual_atualizado:,.2f}"
            url_mensagem = f"https://api.telegram.org/bot{CHAVE_API}/sendMessage?chat_id={BOT_CHAT_ID}&parse_mode=Markdown&text={mensagem}"

            print(f"{mensagem}\n")

            # Enviando a mensagem pelo Telegram usando a biblioteca requests
            get(url_mensagem)

            print("Fluxo finalizado, encerrando.\n")
            return True
        else:
            print("Fluxo incompleto, continuando.\n")
            return False
    else:
        print("Série vazia. Não é possível acessar o último elemento.\n")
        return False

print(">>> Iniciando...")

while True:
    agora = datetime.datetime.now().time()

    if hora_inicial <= agora <= hora_final:
        if msg_telegram(nome_ativo):
            break

    time.sleep(600)  # Aguarda 10 minutos antes de verificar novamente

