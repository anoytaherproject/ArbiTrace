# ArbiTrace

Starter dashboard investor berbasis Flask dengan UI dark/gold. Data finansial pada versi ini adalah **demo/simulasi**.

## Jalankan lokal
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Buka `http://127.0.0.1:5000`.

Demo login:
- Email: `demo@arbitrace.app`
- Password: `demo123`

## GitHub
Upload seluruh isi folder ArbiTrace ke repository. GitHub Pages tidak menjalankan Python/Flask; deploy backend Flask ke layanan hosting Python. Supabase dapat ditambahkan kemudian melalui `.env`.

Jangan commit `.env`, service-role key, password, atau secret key.
