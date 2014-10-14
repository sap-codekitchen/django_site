db.sync:
	python ./codekitchen/manage.py syncdb --noinput
	make script run=load_db_models

db.rm:
	rm -rf ./codekitchen/db.sqlite3

db.rebuild:
	make db.rm
	make db.sync

