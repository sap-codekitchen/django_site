
deploy.live:
	# this is used for full deployment
	make pre-deploy
	# copy the source archive to remote
	scp -r ./versions/latest.zip ${host_env}/latest.zip
	# unzip the source archive into temp folder
	ssh ${host} 'unzip -o ${remote_env}/latest.zip -d ${remote_staging}'
	# copy static to remote
	scp -r ${local_static} ${host_static_parent}
	ssh ${host} 'mkdir -p ${remote_repo}/'
	# copy the logs over to staging
	ssh ${host} 'cp -r ${remote_logs} ${remote_staging}/ || true'
	# overwrite existing repo directory with new files from source archive
	ssh ${host} 'cp -rf ${remote_staging}/* ${remote_repo}/'
	# refresh permissions on logs folder
	ssh ${host} 'fs sa ${remote_logs} daemon.scripts write'
	# copy private settings to appropriate location
	scp ./${config_dir}/shared_private.py ${host_config_dir}/shared_private.py
	scp ./${config_dir}/private_settings_server.py ${host_config_dir}/private_settings.py



