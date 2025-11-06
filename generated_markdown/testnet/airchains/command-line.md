



# command-line

## Tokens


```bash
# Withdraw all rewards
junctiond tx distribution withdraw-all-rewards --from $WALLET --chain-id $AIRCHAINS_CHAIN_ID --fees 200amf -y 

# Withdraw rewards and commission from your validator
junctiond tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $AIRCHAINS_CHAIN_ID --fees 200amf -y 

# Check your balance
junctiond query bank balances $WALLET_ADDRESS

# Delegate to Yourself
junctiond tx staking delegate $VALOPER_ADDRESS 1000000amf --from $WALLET --chain-id $AIRCHAINS_CHAIN_ID --fees 200amf -y 

# Delegate to Someone else
junctiond tx staking delegate <TO_VALOPER_ADDRESS> 1000000amf --from $WALLET --chain-id $AIRCHAINS_CHAIN_ID --fees 200amf -y 

# Unbond
junctiond tx staking unbond $VALOPER_ADDRESS 1000000amf --from $WALLET --chain-id $AIRCHAINS_CHAIN_ID --fees 200amf -y 

# Transfer funds
junctiond tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 1000000amf --from $WALLET --chain-id $AIRCHAINS_CHAIN_ID --fees 200amf -y 


```
## Key management


```bash
# Add New Wallet
junctiond keys add $WALLET

# Add Existing Wallet
junctiond keys add $WALLET --recover

# List Wallets
junctiond keys list

# Delete Wallet
junctiond keys delete $WALLET

# Show Wallet Address
junctiond keys show $WALLET -a

# Export Key (save to wallet.backup)
junctiond keys export $WALLET

# Import Key
junctiond keys import wallet.backup

# View EVM Prived Key
junctiond keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
junctiond query staking validator $VALOPER_ADDRESS

# check validator info
junctiond status 2>&1 | jq

# Jailing info
junctiond q slashing signing-info $(junctiond tendermint show-validator)

# Slashing parameters
junctiond q slashing params

# Unjail validator
junctiond tx slashing unjail --from $WALLET --chain-id $AIRCHAINS_CHAIN_ID --fees 200amf 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status junctiond

# Start Service
sudo systemctl start junctiond

# Stop Service
sudo systemctl stop junctiond

# Restart Service
sudo systemctl restart junctiond

# Enable Service
sudo systemctl enable junctiond

# Disable Service
sudo systemctl disable junctiond

# View Logs
sudo journalctl -fu junctiond -o cat

# Reload Service
sudo systemctl daemon-reload


```