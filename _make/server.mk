python_install_dir = ~/codekitchen/web_scripts/django
python_bin_dir = ~/codekitchen/web_scripts/django

server.install:
	# this command installs all required python packages
    pip install \
        -r requirements.txt \
        -t ${python_install_dir} \
        --install-options="--install-scripts=${python_bin_dir}"

