
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
	# copy private settings to appropriate location
	scp ./${config_dir}/shared_private.py ${host_config_dir}/shared_private.py
	scp ./${config_dir}/private_settings_server.py ${host_config_dir}/private_settings.py



