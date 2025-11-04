



# installation


```bash
# Install Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install curl git wget htop tmux build-essential jq make lz4 gcc unzip -y

```
## Install Go


```bash
cd $HOME
VER="1.22.13"
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
git clone https://github.com/DoraFactory/doravota.git
git checkout 0.4.3
make install
mv $HOME/dorad $HOME/go/bin/dorad

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export DORA_CHAIN_ID="vota-ash"" >> $HOME/.bashrc
echo "export DORA_PORT="22"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
dorad config node tcp://localhost:${DORA_PORT}657
dorad config chain-id $DORA_CHAIN_ID
dorad init "$MONIKER" --chain-id $DORA_CHAIN_ID

```