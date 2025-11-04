



# installation


```bash
# Install Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install curl git wget htop tmux build-essential jq make lz4 gcc unzip -y

```
## Install Go


```bash
cd $HOME
VER="1.22.3"
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
wget https://github.com/Orchestra-Labs/symphony/releases/download/v1.0.4/symphonyd-1.0.4-SNAPSHOT-fad9f314f-linux-amd64.tar.gz
tar -xzf symphonyd-1.0.4-SNAPSHOT-fad9f314f-linux-amd64.tar.gz
mv symphonyd $HOME/go/bin/symphonyd

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export SYMPHONY_CHAIN_ID="symphony-1"" >> $HOME/.bashrc
echo "export SYMPHONY_PORT="23"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
symphonyd config node tcp://localhost:${SYMPHONY_PORT}657
symphonyd config chain-id $SYMPHONY_CHAIN_ID
symphonyd init "$MONIKER" --chain-id $SYMPHONY_CHAIN_ID

```