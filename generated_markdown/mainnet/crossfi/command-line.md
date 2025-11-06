



# command-line

## Tokens


```bash
# Withdraw all rewards
crossfid tx distribution withdraw-all-rewards --from $WALLET --chain-id $CROSSFI_CHAIN_ID --gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx -y 

# Withdraw rewards and commission from your validator
crossfid tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $CROSSFI_CHAIN_ID --gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx -y 

# Check your balance
crossfid query bank balances $WALLET_ADDRESS

# Delegate to Yourself
crossfid tx staking delegate $VALOPER_ADDRESS 10000000000000mpx --from $WALLET --chain-id $CROSSFI_CHAIN_ID --gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx -y 

# Delegate to Someone else
crossfid tx staking delegate <TO_VALOPER_ADDRESS> 10000000000000mpx --from $WALLET --chain-id $CROSSFI_CHAIN_ID --gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx -y 

# Unbond
crossfid tx staking unbond $VALOPER_ADDRESS 10000000000000mpx --from $WALLET --chain-id $CROSSFI_CHAIN_ID --gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx -y 

# Transfer funds
crossfid tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 10000000000000mpx --from $WALLET --chain-id $CROSSFI_CHAIN_ID --gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx -y 


```
## Key management


```bash
# Add New Wallet
crossfid keys add $WALLET

# Add Existing Wallet
crossfid keys add $WALLET --recover

# List Wallets
crossfid keys list

# Delete Wallet
crossfid keys delete $WALLET

# Show Wallet Address
crossfid keys show $WALLET -a

# Export Key (save to wallet.backup)
crossfid keys export $WALLET

# Import Key
crossfid keys import wallet.backup

# View EVM Prived Key
crossfid keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
crossfid query staking validator $VALOPER_ADDRESS

# check validator info
crossfid status 2>&1 | jq

# Jailing info
crossfid q slashing signing-info $(crossfid tendermint show-validator)

# Slashing parameters
crossfid q slashing params

# Unjail validator
crossfid tx slashing unjail --from $WALLET --chain-id $CROSSFI_CHAIN_ID --gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status crossfid

# Start Service
sudo systemctl start crossfid

# Stop Service
sudo systemctl stop crossfid

# Restart Service
sudo systemctl restart crossfid

# Enable Service
sudo systemctl enable crossfid

# Disable Service
sudo systemctl disable crossfid

# View Logs
sudo journalctl -fu crossfid -o cat

# Reload Service
sudo systemctl daemon-reload


```