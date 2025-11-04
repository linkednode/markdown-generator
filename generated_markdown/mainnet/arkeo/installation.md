



# installation


```bash
# Install Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install curl git wget htop tmux build-essential jq make lz4 gcc unzip -y

```
## Install Go


```bash
cd $HOME
VER="1.21.13"
wget "https://golang.org/dl/go$VER.linux-amd64.tar.gz"
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go$VER.linux-amd64.tar.gz"
rm "go$VER.linux-amd64.tar.gz"
echo "export PATH=$PATH:/usr/local/go/bin:~/go/bin" >> ~/.bashrc
source $HOME/.bashrc
[ ! -d ~/go/bin ] && mkdir -p ~/go/bin

```
## Download Binary


```bash
cd $HOME
git clone https://github.com/ArkeoNetwork/arkeo
git checkout v1.0.13
make install
mv $HOME/arkeod $HOME/go/bin/arkeod

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export ARKEO_CHAIN_ID="arkeo-main-v1"" >> $HOME/.bashrc
echo "export ARKEO_PORT="21"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
arkeod config node tcp://localhost:${ARKEO_PORT}657
arkeod config chain-id $ARKEO_CHAIN_ID
arkeod init "$MONIKER" --chain-id $ARKEO_CHAIN_ID

```