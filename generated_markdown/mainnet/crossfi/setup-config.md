



# setup-config

## Custom Ports(Optional)


```bash
# set custom ports in app.toml
sed -i.bak -e "s%:1317%:${CROSSFI_CHAIN_ID}317%g;
s%:8080%:${CROSSFI_CHAIN_ID}080%g;
s%:9090%:${CROSSFI_CHAIN_ID}090%g;
s%:9091%:${CROSSFI_CHAIN_ID}091%g;
s%:8545%:${CROSSFI_CHAIN_ID}545%g;
s%:8546%:${CROSSFI_CHAIN_ID}546%g;
s%:6065%:${CROSSFI_CHAIN_ID}065%g" $HOME/.crossfid/config/app.toml

```

```bash
# set custom ports in config.toml file
sed -i.bak -e "s%:26658%:${CROSSFI_CHAIN_ID}658%g;
s%:26657%:${CROSSFI_CHAIN_ID}657%g;
s%:6060%:${CROSSFI_CHAIN_ID}060%g;
s%:26656%:${CROSSFI_CHAIN_ID}656%g;
s%^external_address = ""%external_address = "$(wget -qO- eth0.me):${CROSSFI_CHAIN_ID}656"%;
s%:26660%:${CROSSFI_CHAIN_ID}660%g" $HOME/.crossfid/config/config.toml
```
## Setup Pruning, gas prices


```bash
# config pruning
sed -i -e "s/^pruning *=.*/pruning = "custom"/" $HOME/.crossfid/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = "100"/" $HOME/.crossfid/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = "50"/" $HOME/.crossfid/config/app.toml

# set minimum gas price, enable prometheus and disable indexing
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "10000000000000mpx"|g' $HOME/.crossfid/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.crossfid/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = "null"/" $HOME/.crossfid/config/config.toml"

```
## Setup genesis and addrbook


```bash
# download genesis and addrbook
wget -O $HOME/.crossfid/config/genesis.json https://server-3.itrocket.net/mainnet/crossfi/genesis.json
wget -O $HOME/.crossfid/config/addrbook.json https://server-3.itrocket.net/mainnet/crossfi/addrbook.json

```
## Create systemd service


```bash
sudo tee /etc/systemd/system/crossfid.service > /dev/null <<EOF
[Unit]
Description=crossfi node
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/.crossfid
ExecStart=$(which crossfid) start --home $HOME/.crossfid
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
sudo systemctl enable crossfid
sudo systemctl restart crossfid && sudo journalctl -fu crossfid -o cat

```