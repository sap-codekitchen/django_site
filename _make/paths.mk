# make commands to run locally in order to deploy to servers
host = athena
appname = codekitchen

remote_env = ${appname}
host_env = ${host}:${remote_env}
host_staging = ${host_env}/tmp
remote_staging = ${remote_env}/tmp
local_static = ./${appname}/static
host_static_parent = ${host_env}/www/
host_static = ${host_env}/www/static

remote_repo = ${remote_env}/Scripts/django
host_repo = ${host}:${remote_repo}

config_dir = ${appname}/${appname}
local_config_dir = ./${config_dir}

remote_config_dir = ${remote_repo}/${config_dir}
host_config_dir = ${host_repo}/${config_dir}


