# Show the help message (default)
[group('core')]
@help:
    just --list

# Start the stack
[group('core')]
dev: compose-down compose-up

# Stop the stack
[group('core')]
stop: compose-down

alias c := compose

# Run a compose command
[group('core')]
compose +args="":
    docker compose {{ args }}

# Show logs using docker compose
[group('core')]
logs target="app":
    docker compose logs -f {{ target }}

# Automatically fix linting errors and format code
[group('core')]
fix:
    #!/usr/bin/env bash
    cd app
    uv run ruff check --fix
    uv run ruff check --select I --fix
    uv run ruff format
    cd ..
    just --format --unstable

# Starts the stack
[private]
compose-up:
    docker compose up

# Stops the stack and removes all volumes and orphans
[private]
compose-down:
    docker compose kill --remove-orphans
    docker compose down --volumes
