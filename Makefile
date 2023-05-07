.PHONY: run
run: .ve
	.ve/bin/python3 process.py

.PHONY: run-mixer
run-mixer: .ve deps
	.ve/bin/python3 mixer.py

.PHONY: compile-requirements
compile-requirements: requirements.txt

requirements.txt: requirements.in
	@.ve/bin/pip-compile requirements.in

.ve: requirements.txt
	python3 -m venv .ve
	.ve/bin/pip install wheel pip-tools
	.ve/bin/pip install -r requirements.txt

.PHONY: deps
deps:
	@echo "Installing dependencies..."
	@command -v ffmpeg > /dev/null || brew install ffmpeg

