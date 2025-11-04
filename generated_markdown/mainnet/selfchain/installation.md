



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
wget https://snap.nodex.one/selfchain/selfchaind
chmod +x selfchaind
mv $HOME/selfchaind $HOME/go/bin/selfchaind

```
## Setup Variables


```bash
echo "export WALLET="wallet"" >> $HOME/.bashrc
echo "export MONIKER="test"" >> $HOME/.bashrc
echo "export SELFCHAIN_CHAIN_ID="self-1"" >> $HOME/.bashrc
echo "export SELFCHAIN_PORT="19"" >> $HOME/.bashrc
source $HOME/.bashrc"

```
## Config and Init app


```bash
selfchaind config node tcp://localhost:${SELFCHAIN_PORT}657
selfchaind config chain-id $SELFCHAIN_CHAIN_ID
selfchaind init "$MONIKER" --chain-id $SELFCHAIN_CHAIN_ID

```