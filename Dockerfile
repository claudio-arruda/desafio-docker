# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app.py .

# Cria o diretório que será mapeado do host
RUN mkdir -p /files_data

# Expõe a porta que a aplicação vai usar
EXPOSE 8000

# Comando para executar a aplicação
CMD ["python", "app.py"]