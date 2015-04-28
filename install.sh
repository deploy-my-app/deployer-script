#get the package manager
if[ -n "$(which apt-get)" ];
	INSTALL="sudo apt-get"
elif[ -n "$(which yum)" ];
	INSTALL="sudo yum"
if[ ! -z INSTALL ];
$("$INSTALL update -y")
$("$INSTALL upgrade -y")
#install dependnecies
$("$INSTALL install python python-pip git -y")

sudo pip install cherrypy
sudo pip install flask
sudo pip install flask-restful
sudo pip install pyinstaller
sudo pip install requests

#get our repo
sudo rm -rf /usr/share/deployer/ 2&>1 /dev/null
sudo mkdir -pf /usr/share/deployer/ 2&>1 /dev/null
cd /usr/share/deployer
sudo git clone https://github.com/my-app-deployer/deployer.git .
#link all the deamon and binaries thingy
sudo ln -s /usr/share/deployer/deamon.sh /etc/init.d/deployer-deamon
sudo ln -s /usr/share/deployer/bin/* /usr/local/bin/
#Trigger installation
sudo /usr/local/bin/deployer-install
#update the rc file to start deamon on startup
sudo update-rc.d -f carbage defaults

sudo /etc/init.d/deployer-deamon start