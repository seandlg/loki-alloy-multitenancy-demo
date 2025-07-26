FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY . /app

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "main.py"]