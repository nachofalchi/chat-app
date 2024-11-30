.myenv:
	@python -m venv .myenv
	@(. .myenv/bin/activate && \
	pip install -q -r requirements.txt)

run: .myenv
	@(. .myenv/bin/activate; \
		python main.py)