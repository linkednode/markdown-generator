



# setup-config

## Custom Ports(Optional)


```bash
# set custom ports in app.toml
sed -i.bak -e "s%:1317%:${ATOMONE_CHAIN_ID}317%g;
s%:8080%:${ATOMONE_CHAIN_ID}080%g;
s%:9090%:${ATOMONE_CHAIN_ID}090%g;
s%:9091%:${ATOMONE_CHAIN_ID}091%g;
s%:8545%:${ATOMONE_CHAIN_ID}545%g;
s%:8546%:${ATOMONE_CHAIN_ID}546%g;
s%:6065%:${ATOMONE_CHAIN_ID}065%g" $HOME/.atomone/config/app.toml

```

```bash
# set custom ports in config.toml file
sed -i.bak -e "s%:26658%:${ATOMONE_CHAIN_ID}658%g;
s%:26657%:${ATOMONE_CHAIN_ID}657%g;
s%:6060%:${ATOMONE_CHAIN_ID}060%g;
s%:26656%:${ATOMONE_CHAIN_ID}656%g;
s%^external_address = ""%external_address = "$(wget -qO- eth0.me):${ATOMONE_CHAIN_ID}656"%;
s%:26660%:${ATOMONE_CHAIN_ID}660%g" $HOME/.atomone/config/config.toml
```
## Setup Pruning, gas prices


```bash
# config pruning
sed -i -e "s/^pruning *=.*/pruning = "custom"/" $HOME/.atomone/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = "100"/" $HOME/.atomone/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = "50"/" $HOME/.atomone/config/app.toml

# set minimum gas price, enable prometheus and disable indexing
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "0.001uatone"|g' $HOME/.atomone/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.atomone/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = "null"/" $HOME/.atomone/config/config.toml"

```
## Setup genesis and addrbook


```bash
# download genesis and addrbook
wget -O $HOME/.atomone/config/genesis.json https://server-2.itrocket.net/testnet/atomone/genesis.json
wget -O $HOME/.atomone/config/addrbook.json https://server-2.itrocket.net/testnet/atomone/addrbook.json

```
## Create systemd service


```bash
sudo tee /etc/systemd/system/atomoned.service > /dev/null <<EOF
[Unit]
Description=atomone node
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/.atomone
ExecStart=$(which atomoned) start --home $HOME/.atomone
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
sudo systemctl enable atomoned
sudo systemctl restart atomoned && sudo journalctl -fu atomoned -o cat

```