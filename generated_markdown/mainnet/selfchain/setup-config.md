



# setup-config

## Custom Ports(Optional)


```bash
# set custom ports in app.toml
sed -i.bak -e "s%:1317%:${SELFCHAIN_CHAIN_ID}317%g;
s%:8080%:${SELFCHAIN_CHAIN_ID}080%g;
s%:9090%:${SELFCHAIN_CHAIN_ID}090%g;
s%:9091%:${SELFCHAIN_CHAIN_ID}091%g;
s%:8545%:${SELFCHAIN_CHAIN_ID}545%g;
s%:8546%:${SELFCHAIN_CHAIN_ID}546%g;
s%:6065%:${SELFCHAIN_CHAIN_ID}065%g" $HOME/.selfchain/config/app.toml

```

```bash
# set custom ports in config.toml file
sed -i.bak -e "s%:26658%:${SELFCHAIN_CHAIN_ID}658%g;
s%:26657%:${SELFCHAIN_CHAIN_ID}657%g;
s%:6060%:${SELFCHAIN_CHAIN_ID}060%g;
s%:26656%:${SELFCHAIN_CHAIN_ID}656%g;
s%^external_address = ""%external_address = "$(wget -qO- eth0.me):${SELFCHAIN_CHAIN_ID}656"%;
s%:26660%:${SELFCHAIN_CHAIN_ID}660%g" $HOME/.selfchain/config/config.toml
```
## Setup Pruning, gas prices


```bash
# config pruning
sed -i -e "s/^pruning *=.*/pruning = "custom"/" $HOME/.selfchain/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = "100"/" $HOME/.selfchain/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = "50"/" $HOME/.selfchain/config/app.toml

# set minimum gas price, enable prometheus and disable indexing
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "0.5uslf"|g' $HOME/.selfchain/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.selfchain/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = "null"/" $HOME/.selfchain/config/config.toml"

```
## Setup genesis and addrbook


```bash
# download genesis and addrbook
wget -O $HOME/.selfchain/config/genesis.json https://server-3.itrocket.net/mainnet/selfchain/genesis.json
wget -O $HOME/.selfchain/config/addrbook.json https://server-3.itrocket.net/mainnet/selfchain/addrbook.json

```
## Create systemd service


```bash
sudo tee /etc/systemd/system/selfchaind.service > /dev/null <<EOF
[Unit]
Description=selfchain node
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/.selfchain
ExecStart=$(which selfchaind) start --home $HOME/.selfchain
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
sudo systemctl enable selfchaind
sudo systemctl restart selfchaind && sudo journalctl -fu selfchaind -o cat

```