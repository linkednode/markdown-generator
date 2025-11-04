



# command-line

## Tokens


```bash
# Withdraw all rewards
dorad tx distribution withdraw-all-rewards --from $WALLET --chain-id $DORA_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka -y 

# Withdraw rewards and commission from your validator
dorad tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $DORA_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka -y 

# Check your balance
dorad query bank balances $WALLET_ADDRESS

# Delegate to Yourself
dorad tx staking delegate $VALOPER_ADDRESS 1000000000000000000peaka --from $WALLET --chain-id $DORA_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka -y 

# Delegate to Someone else
dorad tx staking delegate <TO_VALOPER_ADDRESS> 1000000000000000000peaka --from $WALLET --chain-id $DORA_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka -y 

# Unbond
dorad tx staking unbond $VALOPER_ADDRESS 1000000000000000000peaka --from $WALLET --chain-id $DORA_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka -y 

# Transfer funds
dorad tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 1000000000000000000peaka --from $WALLET --chain-id $DORA_CHAIN_ID --gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka -y 


```
## Key management


```bash
# Add New Wallet
dorad keys add $WALLET

# Add Existing Wallet
dorad keys add $WALLET --recover

# List Wallets
dorad keys list

# Delete Wallet
dorad keys delete $WALLET

# Show Wallet Address
dorad keys show $WALLET -a

# Export Key (save to wallet.backup)
dorad keys export $WALLET

# Import Key
dorad keys import wallet.backup

# View EVM Prived Key
dorad keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
dorad query staking validator $VALOPER_ADDRESS

# check validator info
dorad status 2>&1 | jq

# Jailing info
dorad q slashing signing-info $(dorad tendermint show-validator)

# Slashing parameters
dorad q slashing params

# Unjail validator
dorad tx slashing unjail --from $WALLET --chain-id $name_chain --gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status dorad

# Start Service
sudo systemctl start dorad

# Stop Service
sudo systemctl stop dorad

# Restart Service
sudo systemctl restart dorad

# Enable Service
sudo systemctl enable dorad

# Disable Service
sudo systemctl disable dorad

# View Logs
sudo journalctl -fu dorad -o cat

# Reload Service
sudo systemctl daemon-reload


```