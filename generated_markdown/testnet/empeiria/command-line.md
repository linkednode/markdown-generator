



# command-line

## Tokens


```bash
# Withdraw all rewards
emped tx distribution withdraw-all-rewards --from $WALLET --chain-id $EMPEIRIA_CHAIN_ID --gas auto --gas-adjustment 1.5 --fees 30uempe -y 

# Withdraw rewards and commission from your validator
emped tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $EMPEIRIA_CHAIN_ID --gas auto --gas-adjustment 1.5 --fees 30uempe -y 

# Check your balance
emped query bank balances $WALLET_ADDRESS

# Delegate to Yourself
emped tx staking delegate $VALOPER_ADDRESS 1000000uempe --from $WALLET --chain-id $EMPEIRIA_CHAIN_ID --gas auto --gas-adjustment 1.5 --fees 30uempe -y 

# Delegate to Someone else
emped tx staking delegate <TO_VALOPER_ADDRESS> 1000000uempe --from $WALLET --chain-id $EMPEIRIA_CHAIN_ID --gas auto --gas-adjustment 1.5 --fees 30uempe -y 

# Unbond
emped tx staking unbond $VALOPER_ADDRESS 1000000uempe --from $WALLET --chain-id $EMPEIRIA_CHAIN_ID --gas auto --gas-adjustment 1.5 --fees 30uempe -y 

# Transfer funds
emped tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 1000000uempe --from $WALLET --chain-id $EMPEIRIA_CHAIN_ID --gas auto --gas-adjustment 1.5 --fees 30uempe -y 


```
## Key management


```bash
# Add New Wallet
emped keys add $WALLET

# Add Existing Wallet
emped keys add $WALLET --recover

# List Wallets
emped keys list

# Delete Wallet
emped keys delete $WALLET

# Show Wallet Address
emped keys show $WALLET -a

# Export Key (save to wallet.backup)
emped keys export $WALLET

# Import Key
emped keys import wallet.backup

# View EVM Prived Key
emped keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
emped query staking validator $VALOPER_ADDRESS

# check validator info
emped status 2>&1 | jq

# Jailing info
emped q slashing signing-info $(emped tendermint show-validator)

# Slashing parameters
emped q slashing params

# Unjail validator
emped tx slashing unjail --from $WALLET --chain-id $name_chain --gas auto --gas-adjustment 1.5 --fees 30uempe 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status emped

# Start Service
sudo systemctl start emped

# Stop Service
sudo systemctl stop emped

# Restart Service
sudo systemctl restart emped

# Enable Service
sudo systemctl enable emped

# Disable Service
sudo systemctl disable emped

# View Logs
sudo journalctl -fu emped -o cat

# Reload Service
sudo systemctl daemon-reload


```