# Используем базовый образ Python
FROM python:3.12.2 

# Устанавливаем рабочую директорию в корень контейнера
WORKDIR /

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в корень контейнера
COPY . .

CMD ["sh", "-c", "prisma generate && python run.py"]