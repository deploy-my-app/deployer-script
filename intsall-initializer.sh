#get the package manager
if[ -n "$(which apt-get)" ]; then
	INSTALL="sudo apt-get"
elif[ -n "$(which yum)" ]; then
	INSTALL="sudo yum"
if[ -z INSTALL ]; then
  echo "We couldn't determine your package manager, please either edit this script if you know what you are doing or contact support thomas-deployer.com/support"
  exit 1
fi
$("$INSTALL update -y")
$("$INSTALL upgrade -y")
#install dependnecies
$("$INSTALL install python python-pip git -y")

NAME="deployer"
BASE_PATH="/usr/share/$NAME/"
LOCAL_BIN="/usr/local/bin/"
DEAMON_SCRIPT="deamonize.sh"
INSTALLER_SCRIPT="deployer-install"

sudo pip install flask

sudo pip install pyinstaller
sudo pip install requests

#get our repo
sudo rm -rf "$BASE_PATH" 2&>1 /dev/null
sudo mkdir -pf "$BASE_PATH" 2&>1 /dev/null
cd "$BASE_PATH"
sudo git clone https://github.com/my-app-deployer/deployer.git .
#link all the deamon and binaries thingy
sudo ln -s "$BASE_PATH$DEAMON_SCRIPT" /etc/init.d/"$NAME"
sudo ln -s bin/* "$LOCAL_BIN"
#Trigger installation
sudo "$LOCAL_BIN $INSTALLER_SCRIPT"
#update the rc file to start deamon on startup
sudo update-rc.d -f "$NAME" defaults

sudo /etc/init.d/"$NAME" start