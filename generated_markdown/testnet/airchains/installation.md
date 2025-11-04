



# installation


```bash
# Install Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install curl git wget htop tmux build-essential jq make lz4 gcc unzip -y

```
## Install Go


```bash
cd $HOME
VER="1.21.6"
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
wget https://github.com/airchain-network/airchains-node/releases/download/v0.1.0/junctiond
chmod +x junctiond
mv $HOME/junctiond $HOME/go/bin/junctiond

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export AIRCHAINS_CHAIN_ID="junction"" >> $HOME/.bashrc
echo "export AIRCHAINS_PORT="20"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
junctiond config node tcp://localhost:${AIRCHAINS_PORT}657
junctiond config chain-id $AIRCHAINS_CHAIN_ID
junctiond init "$MONIKER" --chain-id $AIRCHAINS_CHAIN_ID

```