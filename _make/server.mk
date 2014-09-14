# make commands to run on the server
appname = codekitchen

server.install:
	# this command installs all required python packages
	pip install -r ./server-requirements.txt
	pip install -r ./requirements.txt

server.configs:
	# run these as root
	# sudo -i
	# copy private configuration files for the server
	cp /webapps/${appname}/${appname}.conf /etc/supervisor/conf.d/${appname}.conf #supervisor
	# nginx config settings
	cp /webapps/${appname}/${appname}.nginxconf /etc/nginx/sites-available/${appname}
	rm -rf /etc/nginx/sites-enabled/${appname}
	ln -s /etc/nginx/sites-available/${appname} /etc/nginx/sites-enabled/${appname}
	rm -rf /etc/nginx/sites-available/default
	# refresh permissions
	chown -R ${appname}:webadmins /webapps/${appname}
	chmod -R g+w /webapps/${appname}
	chmod +x /webapps/${appname}/bin/gunicorn_start
	supervisorctl reread
	supervisorctl update

server.check:
	sudo supervisorctl status ${appname}

server.restart:
	sudo supervisorctl restart ${appname}
	sudo service nginx restart 


server.run.nginx:
	sudo service nginx start

server.run.gunicorn:
	sudo supervisorctl start ${appname}

