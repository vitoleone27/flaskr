Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-18.04"

  config.vm.network "forwarded_port", guest: 80, host: 8000
  #Allow access on my host machine

  config.vm.synced_folder ".", "/app"
  #sync current directory to /app

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get upgrade
    apt-get install -y python3-venv nginx
    #Install required OS package
    #Install virtual machine

    chown vagrant:vagrant -R /app
    #Make vagrant the owner and group all files into /app
    cd /app
    python3 -m venv /.venv
    source /app/.venv/bin/activate

    git clone https://github.com/vitoleone27/flaskr.git
    cd flaskr/

    /app/.venv/bin/pip install -e .
    #creates virtual machine
    #installing flask gunicorn in the virtual machine

    cp /app/flaskr/app.service /etc/systemd/system/
    cp /app/flaskr/app /etc/nginx/sites-available
    ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
    rm /etc/nginx/sites-enabled/default
    #Copying app.service to the folder system
    #copying nginx.conf to the nginx.conf to the system.
    #running the default, so it now uses nginx.conf file for the runtime
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    export FLASK_APP=flaskr
    flask init-db
    #Initialize database in the .venv
  SHELL

config.vm.provision "shell", inline: <<-SHELL
  systemctl enable app
  systemctl start app
  #enable app to start at boot
SHELL
end
