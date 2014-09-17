
deploy.live:
	# this is used for full deployment
	make pre-deploy
	# copy the source archive to remote
	scp -r ./versions/latest.zip ${host_env}/latest.zip
	# unzip the source archive into temp folder
	ssh ${host} 'unzip -o ${remote_env}/latest.zip -d ${remote_staging}'
	# copy static to remote
	scp -r ${local_static} ${host_static_parent}
	# overwrite existing repo directory with new files from source archive
	ssh ${host} 'mkdir -p ${remote_repo}/'
	ssh ${host} 'cp -rf ${remote_staging}/* ${remote_repo}/'
	# copy shared private settings to remote temp folder
	scp ./${config_dir}/shared_private.py ${host_config_dir}/shared_private.py
	# finally, copy the private settings into the appropriate location
	ssh ${host} 'cp ${remote_env}/private_settings.py ${remote_config_dir}/private_settings.py'

deploy.live.private:
	scp ${local_config_dir}/private_settings.py ${host_env}/private_settings.py

deploy.live.config.initial:
	scp ${local_config_dir}/private_settings.py ${host_env}/private_settings.py
	make deploy.live.config

deploy.live.config:
	scp ${local_config_dir}/shared_private.py ${host_config_dir}/shared_private.py
	scp ${local_config_dir}/gunicorn_start ${host_config_dir}/bin/gunicorn_start
	scp ${local_config_dir}/${appname}.conf ${host_config_dir}/${appname}.conf
	scp ${local_config_dir}/${appname}.nginxconf ${host_config_dir}/${appname}.nginxconf


