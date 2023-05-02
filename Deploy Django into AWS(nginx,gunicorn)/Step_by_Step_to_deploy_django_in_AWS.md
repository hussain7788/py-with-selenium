Step - Ubuntu Operating system
        - login to ubuntu server from AWS EC2 instance
        - run all the commands in user = ubuntu (not root user)

Step 1 - Installing python and nginx

        - sudo apt update
        - sudo apt install python3-pip python3-dev nginx

Step 2 - Creating a python virtual environment 

        - sudo pip3 install virtualenv
        - virtualenv env
        - source env/bin/activate

Step 3 - Installing Django and gunicorn

        - pip install django gunicorn

Step 4 - Setting up our Django project
        - git clone "clone url"
        - go to settings.py  [/home/ubuntu/My_Projects/Ecommerce_Project/Ecommerce_Project.settings.py]
        - add AWS EC2 instance server IPv4 address in ALLOWED_HOSTS = ['54.226.46.73']
        - sudo ufw allow 8000
        - Run the server python3 manage.py runserver 0.0.0.0:8000

Step 5 - Configuring gunicorn
        - gunicorn --bind 0.0.0.0:8000 Ecommerce_Project.wsgi
    It will start the server .now we can access our web application across world with internet
    But if there is a problem with server then it will stop .so we should not stop our server
    Server should run 24*7 .So here we have to setup gunicorn services to run 24*7
        - deactivate
        

Step 6 - Gunicorn Socket and Service setup
        - sudo nano /etc/systemd/system/gunicorn.socket (it will open file in nano, copy code below as it is)
        -   [Unit]
            Description=gunicorn socket

            [Socket]
            ListenStream=/run/gunicorn.sock

            [Install]
            WantedBy=sockets.target

        - sudo vim /etc/systemd/system/gunicorn.service (copy below code and do changes as below)
        - User = current username (amazon-linux = ec2-user or ubuntu = ubuntu)
        - WorkingDirectory = your Django app directory
        - ExecStart = Environment directory where we installed all packages
        - Ecommerce_Project.wsgi:application = project_name.wsgi
        - Now after above chages paste the code in gunicron.service file and save

        - [Unit]
            Description=gunicorn daemon
            Requires=gunicorn.socket
            After=network.target

            [Service]
            User=ubuntu
            Group=www-data
            WorkingDirectory=/home/ubuntu/My_Projects/Ecommerce_Project
            ExecStart=/home/ubuntu/My_Projects/env/bin/gunicorn \
                    --access-logfile - \
                    --workers 3 \
                    --bind unix:/run/gunicorn.sock \
                    Ecommerce_Project.wsgi:application

            [Install]
            WantedBy=multi-user.target

Step 7 - Enable gunicorn Socket
        - Lets now start and enable the gunicorn socket
        - sudo systemctl start gunicorn.socket
        - sudo systemctl enable gunicorn.socket

Step 8 - Configuring Nginx as a reverse proxy
        - sudo nano /etc/nginx/sites-available/Ecommerce_Project (copy paste below code do the changes)
        - server_name <AWS EC2 server IP address>;
        - location /static/ = Django project location
        - after above changes paste code in above nano file
        
        - server {
                    listen 80;
                    server_name 54.226.46.73;

                    location = /favicon.ico { access_log off; log_not_found off; }
                    location /static/ {
                        root /home/ubuntu/My_Projects/Ecommerce_Project;
                    }

                    location / {
                        include proxy_params;
                        proxy_pass http://unix:/run/gunicorn.sock;
                    }
                }

        - Activate the configuration using the following command
        - sudo ln -s /etc/nginx/sites-available/Ecommerce_Project /etc/nginx/sites-enabled/
        - sudo systemctl restart nginx (restart nginx)
        - Done.
 Step 9 - Check server on chrome with below IP

        - 54.226.46.73:8000
        - Now we Successfully deployed our Django application into AWS EC2 instance with nginx webserver and   gunicorn socket.


---------------------------------