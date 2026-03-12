.PHONY: install up down test demo api

install:
python3 -m venv .venv && . .venv/bin/activate && pip install --upgrade pip && pip install -e .

up:
docker compose up -d

down:
docker compose down

test:
. .venv/bin/activate && pytest -q

demo:
. .venv/bin/activate && python -m msc_energy_lab.cli.main demo

api:
. .venv/bin/activate && uvicorn msc_energy_lab.api.app:app --reload --port 8000
