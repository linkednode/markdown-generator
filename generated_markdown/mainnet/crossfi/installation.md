



# installation


```bash
# Install Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install curl git wget htop tmux build-essential jq make lz4 gcc unzip -y

```
## Install Go


```bash
cd $HOME
VER="1.21.3"
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
wget https://github.com/crossfichain/crossfi-node/releases/download/v0.1.1/mineplex-2-node._v0.1.1_linux_amd64.tar.gz
chmod +x $HOME/mineplex-chaind
mv $HOME/mineplex-chaind $HOME/go/bin/crossfid
rm mineplex-2-node._v0.1.1_linux_amd64.tar.gz

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export CROSSFI_CHAIN_ID="mineplex-mainnet-1"" >> $HOME/.bashrc
echo "export CROSSFI_PORT="17"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
crossfid config node tcp://localhost:${CROSSFI_PORT}657
crossfid config chain-id $CROSSFI_CHAIN_ID
crossfid init "$MONIKER" --chain-id $CROSSFI_CHAIN_ID

```