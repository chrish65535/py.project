init:
	pipenv install -r requirements.txt

test:
	nosetests tests
