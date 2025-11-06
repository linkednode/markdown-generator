



# command-line

## Tokens


```bash
# Withdraw all rewards
symphonyd tx distribution withdraw-all-rewards --from $WALLET --chain-id $SYMPHONY_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices 0.025note -y 

# Withdraw rewards and commission from your validator
symphonyd tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $SYMPHONY_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices 0.025note -y 

# Check your balance
symphonyd query bank balances $WALLET_ADDRESS

# Delegate to Yourself
symphonyd tx staking delegate $VALOPER_ADDRESS 1000000note --from $WALLET --chain-id $SYMPHONY_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices 0.025note -y 

# Delegate to Someone else
symphonyd tx staking delegate <TO_VALOPER_ADDRESS> 1000000note --from $WALLET --chain-id $SYMPHONY_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices 0.025note -y 

# Unbond
symphonyd tx staking unbond $VALOPER_ADDRESS 1000000note --from $WALLET --chain-id $SYMPHONY_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices 0.025note -y 

# Transfer funds
symphonyd tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 1000000note --from $WALLET --chain-id $SYMPHONY_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices 0.025note -y 


```
## Key management


```bash
# Add New Wallet
symphonyd keys add $WALLET

# Add Existing Wallet
symphonyd keys add $WALLET --recover

# List Wallets
symphonyd keys list

# Delete Wallet
symphonyd keys delete $WALLET

# Show Wallet Address
symphonyd keys show $WALLET -a

# Export Key (save to wallet.backup)
symphonyd keys export $WALLET

# Import Key
symphonyd keys import wallet.backup

# View EVM Prived Key
symphonyd keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
symphonyd query staking validator $VALOPER_ADDRESS

# check validator info
symphonyd status 2>&1 | jq

# Jailing info
symphonyd q slashing signing-info $(symphonyd tendermint show-validator)

# Slashing parameters
symphonyd q slashing params

# Unjail validator
symphonyd tx slashing unjail --from $WALLET --chain-id $SYMPHONY_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices 0.025note 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status symphonyd

# Start Service
sudo systemctl start symphonyd

# Stop Service
sudo systemctl stop symphonyd

# Restart Service
sudo systemctl restart symphonyd

# Enable Service
sudo systemctl enable symphonyd

# Disable Service
sudo systemctl disable symphonyd

# View Logs
sudo journalctl -fu symphonyd -o cat

# Reload Service
sudo systemctl daemon-reload


```