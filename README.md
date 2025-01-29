Tift jurnal

1. Loyihani klonlash

GitHub repozitoriyasini kompyuteringizga klonlash uchun quyidagi komandani ishlating:

bash
git clone https://github.com/bakhtiyorturaev/tift_jurnal.git
cd tift_jurnal

2. 
python3 -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows

3.
pip install -r requirements.txt

4.
python manage.py migrate

5.
python manage.py createsuperuser

6.
python manage.py createsuperuser

Texnologiyalar
Django 5.1.5
Django Rest Framework
PostgreSQL
CKEditor 5
Gunicorn
Whitenoise
Python 3.10 +
