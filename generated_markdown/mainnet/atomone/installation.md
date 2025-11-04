



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
git clone https://github.com/atomone-hub/atomone
git checkout v1.0.0
make install
mv $HOME/atomoned $HOME/go/bin/atomoned

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export ATOMONE_CHAIN_ID="atomone-1"" >> $HOME/.bashrc
echo "export ATOMONE_PORT="20"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
atomoned config node tcp://localhost:${ATOMONE_PORT}657
atomoned config chain-id $ATOMONE_CHAIN_ID
atomoned init "$MONIKER" --chain-id $ATOMONE_CHAIN_ID

```