



# setup-config

## Custom Ports(Optional)


```bash
# set custom ports in app.toml
sed -i.bak -e "s%:1317%:${SYMPHONY_CHAIN_ID}317%g;
s%:8080%:${SYMPHONY_CHAIN_ID}080%g;
s%:9090%:${SYMPHONY_CHAIN_ID}090%g;
s%:9091%:${SYMPHONY_CHAIN_ID}091%g;
s%:8545%:${SYMPHONY_CHAIN_ID}545%g;
s%:8546%:${SYMPHONY_CHAIN_ID}546%g;
s%:6065%:${SYMPHONY_CHAIN_ID}065%g" $HOME/.symphonyd/config/app.toml

```

```bash
# set custom ports in config.toml file
sed -i.bak -e "s%:26658%:${SYMPHONY_CHAIN_ID}658%g;
s%:26657%:${SYMPHONY_CHAIN_ID}657%g;
s%:6060%:${SYMPHONY_CHAIN_ID}060%g;
s%:26656%:${SYMPHONY_CHAIN_ID}656%g;
s%^external_address = ""%external_address = "$(wget -qO- eth0.me):${SYMPHONY_CHAIN_ID}656"%;
s%:26660%:${SYMPHONY_CHAIN_ID}660%g" $HOME/.symphonyd/config/config.toml
```
## Setup Pruning, gas prices


```bash
# config pruning
sed -i -e "s/^pruning *=.*/pruning = "custom"/" $HOME/.symphonyd/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = "100"/" $HOME/.symphonyd/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = "50"/" $HOME/.symphonyd/config/app.toml

# set minimum gas price, enable prometheus and disable indexing
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "0.025note"|g' $HOME/.symphonyd/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.symphonyd/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = "null"/" $HOME/.symphonyd/config/config.toml"

```
## Setup genesis and addrbook


```bash
# download genesis and addrbook
wget -O $HOME/.symphonyd/config/genesis.json curl -L https://snap.vinjan.xyz/symphony/addrbook.json > $HOME/.symphonyd/config/addrbook.json
wget -O $HOME/.symphonyd/config/addrbook.json curl -L https://snapshot.vinjan.xyz/symphony/genesis.json > $HOME/.symphonyd/config/genesis.json

```
## Create systemd service


```bash
sudo tee /etc/systemd/system/symphonyd.service > /dev/null <<EOF
[Unit]
Description=symphony node
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/.symphonyd
ExecStart=$(which symphonyd) start --home $HOME/.symphonyd
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
sudo systemctl enable symphonyd
sudo systemctl restart symphonyd && sudo journalctl -fu symphonyd -o cat

```