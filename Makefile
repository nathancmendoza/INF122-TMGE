# Makefile for tile matching tools package 

help:
	@echo "Makefile for IN4MATX 122 final project. Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'	

venv: ## Setup a virtual environment
	[ -d .venv ] || python3 -m venv .venv --prompt=tilematch_tools

clean-venv: ## Destroy the virtual environment if it exists
	[ ! -d .venv ] || rm -rf .venv

clean-test: ## Remove testing artifacts
	[ ! -d .pytest_cache ] || rm -rf .pytest_cache

clean-pyc: ## Remove package artifacts and cached byte code
	find . -name __pycache__ -exec rm -rf {} +
	find . -name *.egg-info -exec rm -rf {} +

clean-cov: ## Remove code coverage artifacts
	[ ! -e .coverage ] || rm -f .coverage

clean: clean-venv clean-test clean-pyc clean-cov ## Clean up develepment environment

activate: ## Activate the virtual environment for bootstrapping (does NOT activate for you).
	@echo 
	@echo
	@echo "Virtual environment created!"
	@echo "Activate it by running the following:"
	@echo
	@echo "    source .venv/bin/activate"
	@echo 

.PHONY: test
test: ## Run unittests on the source directory
	pytest --cov=tilematch_tools -k "not integration"
	coverage report -m

test-int: ## Run unittests on tests marked integration
	pytest -v -m integration --cache-clear

.PHONY: lint
lint: ## Run lint checks on the source directory
	pylint src/tilematch_tools 

bootstrap: venv ## Bootstrap the virtual environment
	@( \
		source .venv/bin/activate; \
		pip install --upgrade pip; \
		pip3 install --require-virtualenv -r requirements.txt; \
		pip3 install --require-virtualenv -r dev_requirements.txt; \
		pip3 install --editable . ; \
	)
	@$(MAKE) activate

.PHONY: uml ## Auto-generates UML, requires Graphviz
uml:
	mkdir -p ./uml
	pyreverse ./src/tilematch_tools -d ./uml -o png -p tilematch_tools 

.PHONY: docs
## Run docs-init, then cd into ./docs and run `make singlehtml` (`make help` for more options) 
docs-init: ## Initialize sphinx,  rebuild venv to reinitialize
	sphinx-apidoc -F -A "INF 122 Winter 2023 Group 15" -V "0.1" -D html_theme=sphinx_rtd_theme -o ./docs ./src/tilematch_tools

docs-ow: ## Overwrite docs, rebuild venv for significant changes
	sphinx-apidoc -f -o ./docs ./src/tilematch_tools

