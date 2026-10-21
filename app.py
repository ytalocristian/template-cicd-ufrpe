from flask import Flask
from faker import Faker
import pyfiglet
import platform
import socket

app = Flask(__name__)
fake = Faker('pt_BR')

# =======================================================================
# Altere o nome abaixo no GitHub para testar o CI/CD
NOME_DA_EQUIPE = "Ytalo Cristian"
COR_DO_TEMA = "#064e3b" 
# =======================================================================

@app.route('/')
def home():
    # Coleta informações reais do Sistema Operacional / Container
    hostname = socket.gethostname()
    arquitetura = platform.machine()
    sistema = platform.system()
    
    # Usa bibliotecas externas (Pyfiglet e Faker)
    banner_ascii = pyfiglet.figlet_format("DevOps UFRPE")
    cliente_falso = fake.name()
    ip_falso = fake.ipv4()

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Painel de Infraestrutura</title>
        <style>
            body {{ background-color: {COR_DO_TEMA}; color: #f8fafc; font-family: monospace; padding: 40px; }}
            .card {{ background: #0f172a; padding: 25px; border-radius: 10px; border: 1px solid #334155; max-width: 700px; margin: auto; }}
            h1 {{ color: #38bdf8; margin-top: 0; }}
            pre {{ color: #4ade80; font-weight: bold; overflow-x: auto; }}
            .badge {{ background: #0284c7; padding: 4px 10px; border-radius: 5px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            <pre>{banner_ascii}</pre>
            <h1>🚀 {NOME_DA_EQUIPE}</h1>
            <hr style="border-color: #334155;">
            <h3>📊 Telemetria do Sistema Operacional (Kernel):</h3>
            <p><b>ID do Container (Hostname):</b> <span class="badge">{hostname}</span></p>
            <p><b>Arquitetura da CPU:</b> <span class="badge">{arquitetura}</span> (x86_64 = Intel/AMD | aarch64 = ARM Oracle)</p>
            <p><b>Sistema Base:</b> {sistema}</p>
            <hr style="border-color: #334155;">
            <h3>🎲 Teste de Dependência Externa (Lib Faker):</h3>
            <p>Último acesso simulado: <b>{cliente_falso}</b> (IP: {ip_falso})</p>
            <p style="color: #94a3b8; font-size: 12px;">Atualize a página (F5) para gerar um novo acesso.</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    # Roda na porta 8080 liberando acesso externo (0.0.0.0)
    app.run(host='0.0.0.0', port=8080)
