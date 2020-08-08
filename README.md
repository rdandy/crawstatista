####Usage

pip install -r requirements.txt

---

####Development mode
gunicorn --reload -w 2 -b 0.0.0.0:8000 proj.app:app

---

####Run
gunicorn -w 2 -b 0.0.0.0:8000 proj.app:app

---
