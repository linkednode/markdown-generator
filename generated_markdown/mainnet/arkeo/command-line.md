



# command-line

## Tokens


```bash
# Withdraw all rewards
arkeod tx distribution withdraw-all-rewards --from $WALLET --chain-id $ARKEO_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uarkeo -y 

# Withdraw rewards and commission from your validator
arkeod tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $ARKEO_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uarkeo -y 

# Check your balance
arkeod query bank balances $WALLET_ADDRESS

# Delegate to Yourself
arkeod tx staking delegate $VALOPER_ADDRESS 1000000uarkeo --from $WALLET --chain-id $ARKEO_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uarkeo -y 

# Delegate to Someone else
arkeod tx staking delegate <TO_VALOPER_ADDRESS> 1000000uarkeo --from $WALLET --chain-id $ARKEO_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uarkeo -y 

# Unbond
arkeod tx staking unbond $VALOPER_ADDRESS 1000000uarkeo --from $WALLET --chain-id $ARKEO_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uarkeo -y 

# Transfer funds
arkeod tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 1000000uarkeo --from $WALLET --chain-id $ARKEO_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uarkeo -y 


```
## Key management


```bash
# Add New Wallet
arkeod keys add $WALLET

# Add Existing Wallet
arkeod keys add $WALLET --recover

# List Wallets
arkeod keys list

# Delete Wallet
arkeod keys delete $WALLET

# Show Wallet Address
arkeod keys show $WALLET -a

# Export Key (save to wallet.backup)
arkeod keys export $WALLET

# Import Key
arkeod keys import wallet.backup

# View EVM Prived Key
arkeod keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
arkeod query staking validator $VALOPER_ADDRESS

# check validator info
arkeod status 2>&1 | jq

# Jailing info
arkeod q slashing signing-info $(arkeod tendermint show-validator)

# Slashing parameters
arkeod q slashing params

# Unjail validator
arkeod tx slashing unjail --from $WALLET --chain-id $name_chain --gas-adjustment 1.5 --gas auto --gas-prices=0.001uarkeo 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status arkeod

# Start Service
sudo systemctl start arkeod

# Stop Service
sudo systemctl stop arkeod

# Restart Service
sudo systemctl restart arkeod

# Enable Service
sudo systemctl enable arkeod

# Disable Service
sudo systemctl disable arkeod

# View Logs
sudo journalctl -fu arkeod -o cat

# Reload Service
sudo systemctl daemon-reload


```