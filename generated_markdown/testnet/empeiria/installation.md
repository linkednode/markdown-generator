



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
curl -LO https://github.com/empe-io/empe-chain-releases/raw/master/v0.2.2/emped_v0.2.2_linux_amd64.tar.gz
tar -xvf emped_v0.2.2_linux_amd64.tar.gz
chmod +x $HOME/bin/emped
mv $HOME/bin/emped $HOME/go/bin/emped

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export EMPEIRIA_CHAIN_ID="empe-testnet-2"" >> $HOME/.bashrc
echo "export EMPEIRIA_PORT="23"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
emped config node tcp://localhost:${EMPEIRIA_PORT}657
emped config chain-id $EMPEIRIA_CHAIN_ID
emped init "$MONIKER" --chain-id $EMPEIRIA_CHAIN_ID

```