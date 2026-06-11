# Define the build targets (not real files)
.PHONY: build clean docs all validate

# Path for keeping build logs with timestamp
LOG_FILE = docs/source/_templates/logs/$(shell date +'%Y%m%d%H%M%S')_build_logs.txt

# Main task: run build and docs sequentially
all: 
	@mkdir -p docs/source/_templates/logs
	@echo "Starting full build process..."
	@$(MAKE) build 2>&1 | tee $(LOG_FILE)
	@$(MAKE) docs 2>&1 | tee -a $(LOG_FILE)
	@echo "Build complete. Logs saved to $(LOG_FILE)"

# Validate tokens, then compile design tokens using Style Dictionary
build: validate
	@echo "Building design tokens..."
	npx style-dictionary build --config scripts/config.json

# Step to run token validation script
validate:
	@echo "Validating design tokens..."
	python3 scripts/validate_tokens.py

# Generate docs and build website (PDF build is excluded to avoid errors)
docs:
	@echo "Generating documentation content from tokens..."
	python3 scripts/generate_docs.py
	@echo "Building full documentation..."
	cd docs && $(MAKE) build-all

# Cleanup build artifacts
clean:
	@echo "Cleaning builds (Logs kept)..."
	rm -rf build/*
	cd docs && rm -rf build/*
