test.users:
	python ./codekitchen/manage.py runscript add_users

test.sync:
	python ./codekitchen/manage.py syncdb --noinput

test.destroy:
	rm -rf ./codekitchen/db.sqlite3

test.rebuild:
	make test.destroy
	make test.sync
