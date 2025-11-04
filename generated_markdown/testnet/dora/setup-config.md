



# setup-config

## Custom Ports(Optional)


```bash
# set custom ports in app.toml
sed -i.bak -e "s%:1317%:${DORA_CHAIN_ID}317%g;
s%:8080%:${DORA_CHAIN_ID}080%g;
s%:9090%:${DORA_CHAIN_ID}090%g;
s%:9091%:${DORA_CHAIN_ID}091%g;
s%:8545%:${DORA_CHAIN_ID}545%g;
s%:8546%:${DORA_CHAIN_ID}546%g;
s%:6065%:${DORA_CHAIN_ID}065%g" $HOME/.dora/config/app.toml

```

```bash
# set custom ports in config.toml file
sed -i.bak -e "s%:26658%:${DORA_CHAIN_ID}658%g;
s%:26657%:${DORA_CHAIN_ID}657%g;
s%:6060%:${DORA_CHAIN_ID}060%g;
s%:26656%:${DORA_CHAIN_ID}656%g;
s%^external_address = ""%external_address = "$(wget -qO- eth0.me):${DORA_CHAIN_ID}656"%;
s%:26660%:${DORA_CHAIN_ID}660%g" $HOME/.dora/config/config.toml
```
## Setup Pruning, gas prices


```bash
# config pruning
sed -i -e "s/^pruning *=.*/pruning = "custom"/" $HOME/.dora/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = "100"/" $HOME/.dora/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = "50"/" $HOME/.dora/config/app.toml

# set minimum gas price, enable prometheus and disable indexing
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "10000000000peaka"|g' $HOME/.dora/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.dora/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = "null"/" $HOME/.dora/config/config.toml"

```
## Setup genesis and addrbook


```bash
# download genesis and addrbook
wget -O $HOME/.dora/config/genesis.json https://server-2.itrocket.net/testnet/dora/genesis.json
wget -O $HOME/.dora/config/addrbook.json https://server-2.itrocket.net/testnet/dora/addrbook.json

```
## Create systemd service


```bash
sudo tee /etc/systemd/system/dorad.service > /dev/null <<EOF
[Unit]
Description=dora node
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/.dora
ExecStart=$(which dorad) start --home $HOME/.dora
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
sudo systemctl enable dorad
sudo systemctl restart dorad && sudo journalctl -fu dorad -o cat

```