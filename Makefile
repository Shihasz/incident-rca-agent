.DEFAULT_GOAL := help
.PHONY: help install lint format typecheck test check clean

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "} {printf "  %-12s %s\n", $$1, $$2}'

install: ## Install the package with dev dependencies and git hooks
	pip install -e ".[dev]"
	pre-commit install

lint: ## Run Ruff lint and format checks
	ruff check src tests
	ruff format --check src tests

format: ## Auto-fix lint issues and format code
	ruff check --fix src tests
	ruff format src tests

typecheck: ## Run mypy in strict mode
	mypy

test: ## Run the test suite with coverage
	pytest --cov=rca_agent --cov-report=term-missing

check: lint typecheck test ## Run lint, type checks, and tests

clean: ## Remove caches and build artifacts (keeps .venv)
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov build dist
	find . -type d -name __pycache__ -not -path "./.venv/*" -prune -exec rm -rf {} +
