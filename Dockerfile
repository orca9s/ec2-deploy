FROM            ec2-deploy:base

ENV         PROJECT_DIR     /srv/project

# Nginx
RUN     apt -y install nginx

# Copy project files
COPY            .   /srv/project
WORKDIR         /srv/project

# virtualenv files
RUN         export VENV_PATH=$(pipenv --venv); echo $venv_PATH;


#Run uWSGI (CMD)
#CMD         pipenv run uwsgi --ini ${PROJECT_DIR}/.config/uwsgi_http.ini

# RUn Nginx
#CMD         nginx -g 'daemon off;'