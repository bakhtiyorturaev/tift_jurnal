# 1. Python imijini tanlash
FROM python:3.11-slim

# 2. Loyihani konteynerga nusxalash
WORKDIR /app

# Talab qilinadigan fayllarni ko'chirib olish
COPY requirements.txt /app/

# 3. Kerakli kutubxonalarni o'rnatish
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani konteynerga nusxalash
COPY . /app/

# 4. Portni ochish (Django default port: 8000)
EXPOSE 8000

# 5. Django serverini ishga tushurish
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.wsgi:application"]
