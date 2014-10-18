include _make/paths.mk

run:
	# this starts both the django and node development servers
	# http://localhost:3000    Javascript development server
	# http://localhost:3001    Django development server
	kill `lsof -t -i:3000` || true
	kill `lsof -t -i:3001` || true
	gulp & python ./codekitchen/manage.py runserver 3001

run.live:
	# make run.live ip=18.111.62.202
	python ./codekitchen/manage.py runserver $(ip) & gulp

clean:
	# this command removes all compiled python files
	# and files created by javascript development
	find . -name "*.pyc" -exec rm -rf {} \;

install:
	# this command installs all python and javascript packages required for
	# development
	pip install -r ./requirements.txt
	npm install

script:
	# run a script
	python ./codekitchen/manage.py runscript $(run)

build:
	python ./codekitchen/manage.py collectstatic --noinput

bundle:
	git archive HEAD --format=zip > ./versions/latest.zip

pre-deploy:
	make build
	make bundle


include _make/db.mk
include _make/deploy.mk
include _make/server.mk
include _make/test.mk

