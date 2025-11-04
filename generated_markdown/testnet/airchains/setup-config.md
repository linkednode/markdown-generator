



# setup-config

## Custom Ports(Optional)


```bash
# set custom ports in app.toml
sed -i.bak -e "s%:1317%:${AIRCHAINS_CHAIN_ID}317%g;
s%:8080%:${AIRCHAINS_CHAIN_ID}080%g;
s%:9090%:${AIRCHAINS_CHAIN_ID}090%g;
s%:9091%:${AIRCHAINS_CHAIN_ID}091%g;
s%:8545%:${AIRCHAINS_CHAIN_ID}545%g;
s%:8546%:${AIRCHAINS_CHAIN_ID}546%g;
s%:6065%:${AIRCHAINS_CHAIN_ID}065%g" $HOME/.junction/config/app.toml

```

```bash
# set custom ports in config.toml file
sed -i.bak -e "s%:26658%:${AIRCHAINS_CHAIN_ID}658%g;
s%:26657%:${AIRCHAINS_CHAIN_ID}657%g;
s%:6060%:${AIRCHAINS_CHAIN_ID}060%g;
s%:26656%:${AIRCHAINS_CHAIN_ID}656%g;
s%^external_address = ""%external_address = "$(wget -qO- eth0.me):${AIRCHAINS_CHAIN_ID}656"%;
s%:26660%:${AIRCHAINS_CHAIN_ID}660%g" $HOME/.junction/config/config.toml
```
## Setup Pruning, gas prices


```bash
# config pruning
sed -i -e "s/^pruning *=.*/pruning = "custom"/" $HOME/.junction/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = "100"/" $HOME/.junction/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = "50"/" $HOME/.junction/config/app.toml

# set minimum gas price, enable prometheus and disable indexing
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "0.001amf"|g' $HOME/.junction/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.junction/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = "null"/" $HOME/.junction/config/config.toml"

```
## Setup genesis and addrbook


```bash
# download genesis and addrbook
wget -O $HOME/.junction/config/genesis.json https://server-3.itrocket.net/testnet/airchains/genesis.json
wget -O $HOME/.junction/config/addrbook.json https://server-3.itrocket.net/testnet/airchains/addrbook.json

```
## Create systemd service


```bash
sudo tee /etc/systemd/system/junctiond.service > /dev/null <<EOF
[Unit]
Description=airchains node
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/.junction
ExecStart=$(which junctiond) start --home $HOME/.junction
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
sudo systemctl enable junctiond
sudo systemctl restart junctiond && sudo journalctl -fu junctiond -o cat

```