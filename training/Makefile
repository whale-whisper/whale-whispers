# make targets to run training jobs
.PHONY: train
train: .ve
	.ve/bin/python whales.py

.PHONY: compile-requirements
compile-requirements: requirements.txt

requirements.txt: .ve/bin/pip requirements.in
	@.ve/bin/pip-compile --resolver=backtracking requirements.in

.ve: .ve/bin/pip requirements.txt
	.ve/bin/pip install -r requirements.txt && touch .ve

.ve/bin/pip:
	python3 -m venv .ve
	.ve/bin/pip install wheel pip-tools

.PHONY: deps
deps:

.PHONY: clean
clean:
	rm -rf .ve
