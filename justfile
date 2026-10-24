@default:
    just --list

# Start the dev server at http://127.0.0.1:8000/steering-council/
up:
    DJANGO_DEBUG=1 uv run python manage.py runserver

# Build the static site into _site/ (GitHub Pages serves _site/steering-council/)
build:
    uv run python manage.py distill generate --output-directory _site --collectstatic --force

# Run the tests
test:
    uv run pytest

# Check GitHub workflows and Dependabot config for security issues
zizmor:
    uvx zizmor .
