
Copy .env.example to .env and fill in your keys.

Then run:
```sh
uv venv
source .venv/bin/activate # (in Windows use `.venv\Scripts\activate`)
uv pip install -r requirements.txt
python test.py
```