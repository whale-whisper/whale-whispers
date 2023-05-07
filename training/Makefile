.PHONY: compile-requirements
compile-requirements: requirements.txt

requirements.txt: requirements.in
	@.ve/bin/pip-compile --resolver=backtracking requirements.in

.ve: requirements.txt
	python3 -m venv .ve
	.ve/bin/pip install wheel pip-tools
	.ve/bin/pip install -r requirements.txt

.PHONY: deps
deps:
	@echo "Installing dependencies..."
	@command -v ffmpeg > /dev/null || brew install ffmpeg

