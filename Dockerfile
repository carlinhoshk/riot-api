# Use a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Expõe a porta que o aplicativo Flask está usando (substitua pela porta correta)
EXPOSE 5000

# Define a variável de ambiente para o Flask
# ENV FLASK_APP=app.py

# Inicia o aplicativo Flask quando o contêiner for iniciado
# CMD ["flask", "run", "--host=0.0.0.0"]
