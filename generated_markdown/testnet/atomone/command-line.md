



# command-line

## Tokens


```bash
# Withdraw all rewards
atomoned tx distribution withdraw-all-rewards --from $WALLET --chain-id $ATOMONE_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone -y 

# Withdraw rewards and commission from your validator
atomoned tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $ATOMONE_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone -y 

# Check your balance
atomoned query bank balances $WALLET_ADDRESS

# Delegate to Yourself
atomoned tx staking delegate $VALOPER_ADDRESS 1000000uatone --from $WALLET --chain-id $ATOMONE_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone -y 

# Delegate to Someone else
atomoned tx staking delegate <TO_VALOPER_ADDRESS> 1000000uatone --from $WALLET --chain-id $ATOMONE_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone -y 

# Unbond
atomoned tx staking unbond $VALOPER_ADDRESS 1000000uatone --from $WALLET --chain-id $ATOMONE_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone -y 

# Transfer funds
atomoned tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 1000000uatone --from $WALLET --chain-id $ATOMONE_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone -y 


```
## Key management


```bash
# Add New Wallet
atomoned keys add $WALLET

# Add Existing Wallet
atomoned keys add $WALLET --recover

# List Wallets
atomoned keys list

# Delete Wallet
atomoned keys delete $WALLET

# Show Wallet Address
atomoned keys show $WALLET -a

# Export Key (save to wallet.backup)
atomoned keys export $WALLET

# Import Key
atomoned keys import wallet.backup

# View EVM Prived Key
atomoned keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
atomoned query staking validator $VALOPER_ADDRESS

# check validator info
atomoned status 2>&1 | jq

# Jailing info
atomoned q slashing signing-info $(atomoned tendermint show-validator)

# Slashing parameters
atomoned q slashing params

# Unjail validator
atomoned tx slashing unjail --from $WALLET --chain-id $ATOMONE_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status atomoned

# Start Service
sudo systemctl start atomoned

# Stop Service
sudo systemctl stop atomoned

# Restart Service
sudo systemctl restart atomoned

# Enable Service
sudo systemctl enable atomoned

# Disable Service
sudo systemctl disable atomoned

# View Logs
sudo journalctl -fu atomoned -o cat

# Reload Service
sudo systemctl daemon-reload


```