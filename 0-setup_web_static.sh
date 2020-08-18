#!/usr/bin/env bash
# Installs NGINX and sets up the initial file structure for the rest of the project
#	- Creates a symbolic link between the shared/ and releases/ folders
#	- Gives the ownership of the data/ folder to user and group called 'ubuntu'
#	- Update NGINX conf file to serve content from /data/web_static/current/ as /data/web_static/current/
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i '/^\tserver_name*/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
