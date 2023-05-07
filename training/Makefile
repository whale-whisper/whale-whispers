.PHONY: train
train: .ve
	.ve/bin/python train.py

.PHONY: compile-requirements
compile-requirements: requirements.txt

requirements.txt: .ve/bin/pip requirements.in
	@.ve/bin/pip-compile --resolver=backtracking requirements.in

.ve: .ve/bin/pip requirements.txt
	.ve/bin/pip install -r requirements.txt

.ve/bin/pip:
	python3 -m venv .ve
	.ve/bin/pip install wheel pip-tools

.PHONY: deps
deps:
	@echo "Installing dependencies..."
	@command -v ffmpeg > /dev/null || brew install ffmpeg

