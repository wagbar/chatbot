# Usando uma imagem base do Python
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do seu projeto para o container
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar a aplicação
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]