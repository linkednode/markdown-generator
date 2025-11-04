



# setup-config

## Custom Ports(Optional)


```bash
# set custom ports in app.toml
sed -i.bak -e "s%:1317%:${EMPEIRIA_CHAIN_ID}317%g;
s%:8080%:${EMPEIRIA_CHAIN_ID}080%g;
s%:9090%:${EMPEIRIA_CHAIN_ID}090%g;
s%:9091%:${EMPEIRIA_CHAIN_ID}091%g;
s%:8545%:${EMPEIRIA_CHAIN_ID}545%g;
s%:8546%:${EMPEIRIA_CHAIN_ID}546%g;
s%:6065%:${EMPEIRIA_CHAIN_ID}065%g" $HOME/.empe-chain/config/app.toml

```

```bash
# set custom ports in config.toml file
sed -i.bak -e "s%:26658%:${EMPEIRIA_CHAIN_ID}658%g;
s%:26657%:${EMPEIRIA_CHAIN_ID}657%g;
s%:6060%:${EMPEIRIA_CHAIN_ID}060%g;
s%:26656%:${EMPEIRIA_CHAIN_ID}656%g;
s%^external_address = ""%external_address = "$(wget -qO- eth0.me):${EMPEIRIA_CHAIN_ID}656"%;
s%:26660%:${EMPEIRIA_CHAIN_ID}660%g" $HOME/.empe-chain/config/config.toml
```
## Setup Pruning, gas prices


```bash
# config pruning
sed -i -e "s/^pruning *=.*/pruning = "custom"/" $HOME/.empe-chain/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = "100"/" $HOME/.empe-chain/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = "50"/" $HOME/.empe-chain/config/app.toml

# set minimum gas price, enable prometheus and disable indexing
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "0.0001uempe"|g' $HOME/.empe-chain/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.empe-chain/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = "null"/" $HOME/.empe-chain/config/config.toml"

```
## Setup genesis and addrbook


```bash
# download genesis and addrbook
wget -O $HOME/.empe-chain/config/genesis.json https://server-3.itrocket.net/testnet/empeiria/genesis.json
wget -O $HOME/.empe-chain/config/addrbook.json https://server-3.itrocket.net/testnet/empeiria/addrbook.json

```
## Create systemd service


```bash
sudo tee /etc/systemd/system/emped.service > /dev/null <<EOF
[Unit]
Description=empeiria node
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/.empe-chain
ExecStart=$(which emped) start --home $HOME/.empe-chain
Restart=on-failure
RestartSec=5
LimitNOFILE=65535
[Install]
WantedBy=multi-user.target
EOF

```
## Start service


```bash
sudo systemctl daemon-reload
sudo systemctl enable emped
sudo systemctl restart emped && sudo journalctl -fu emped -o cat

```