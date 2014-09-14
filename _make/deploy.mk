# make commands to run locally in order to deploy to servers
deployhost = codekitchen
appname = codekitchen

deploy.live:
	# this is used for full deployment
	make pre-deploy
	# copy the source archive to remote
	scp -r ./versions/latest.zip ${deployhost}:/webapps/${appname}/latest.zip
	# unzip the source archive into temp folder
	ssh ${deployhost} 'unzip -o /webapps/${appname}/latest.zip -d /webapps/${appname}/tmp'
	# copy shared private settings to remote temp folder
	scp ./${appname}/${appname}/shared_private.py ${deployhost}:/webapps/${appname}/tmp/${appname}/${appname}/shared_private.py
	# copy static to remote
	scp -r ./${appname}/static ${deployhost}:/webapps/${appname}/
	# overwrite existing app with new files from source archive
	ssh ${deployhost} 'mkdir -p /webapps/${appname}/${appname}/'
	ssh ${deployhost} 'cp -rf /webapps/${appname}/tmp/* /webapps/${appname}/${appname}/'
	# finally, copy the private settings into the appropriate location
	ssh ${deployhost} 'cp /webapps/${appname}/private_settings.py /webapps/${appname}/${appname}/${appname}/${appname}/private_settings.py'

deploy.live.configs:
	scp ./${appname}/${appname}/private_settings.py ${deployhost}:/webapps/${appname}/private_settings.py
	scp ./${appname}/${appname}/shared_private.py ${deployhost}:/webapps/${appname}/shared_private.py
	scp ./${appname}/${appname}/gunicorn_start ${deployhost}:/webapps/${appname}/bin/gunicorn_start
	scp ./${appname}/${appname}/${appname}.conf ${deployhost}:/webapps/${appname}/${appname}.conf
	scp ./${appname}/${appname}/${appname}.nginxconf ${deployhost}:/webapps/${appname}/${appname}.nginxconf


