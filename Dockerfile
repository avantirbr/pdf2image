# Usar uma imagem base do Python
FROM python:3.9-slim

# Instalar a dependência do sistema (poppler) - AQUI ESTÁ A MÁGICA!
RUN apt-get update && apt-get install -y poppler-utils

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app.py .

# Expor a porta que a aplicação vai rodar
EXPOSE 5001

# Comando para rodar a aplicação
CMD ["python", "app.py"]
