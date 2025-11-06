



# command-line

## Tokens


```bash
# Withdraw all rewards
selfchaind tx distribution withdraw-all-rewards --from $WALLET --chain-id $SELFCHAIN_CHAIN_ID --gas-adjustment 1.2 --gas auto --gas-prices=0.5uslf -y 

# Withdraw rewards and commission from your validator
selfchaind tx distribution withdraw-rewards $VALOPER_ADDRESS --from $WALLET --chain-id $SELFCHAIN_CHAIN_ID --gas-adjustment 1.2 --gas auto --gas-prices=0.5uslf -y 

# Check your balance
selfchaind query bank balances $WALLET_ADDRESS

# Delegate to Yourself
selfchaind tx staking delegate $VALOPER_ADDRESS 1000000uslf --from $WALLET --chain-id $SELFCHAIN_CHAIN_ID --gas-adjustment 1.2 --gas auto --gas-prices=0.5uslf -y 

# Delegate to Someone else
selfchaind tx staking delegate <TO_VALOPER_ADDRESS> 1000000uslf --from $WALLET --chain-id $SELFCHAIN_CHAIN_ID --gas-adjustment 1.2 --gas auto --gas-prices=0.5uslf -y 

# Unbond
selfchaind tx staking unbond $VALOPER_ADDRESS 1000000uslf --from $WALLET --chain-id $SELFCHAIN_CHAIN_ID --gas-adjustment 1.2 --gas auto --gas-prices=0.5uslf -y 

# Transfer funds
selfchaind tx bank send $WALLET_ADDRESS <TO_WALLET_ADDRESS> 1000000uslf --from $WALLET --chain-id $SELFCHAIN_CHAIN_ID --gas-adjustment 1.2 --gas auto --gas-prices=0.5uslf -y 


```
## Key management


```bash
# Add New Wallet
selfchaind keys add $WALLET

# Add Existing Wallet
selfchaind keys add $WALLET --recover

# List Wallets
selfchaind keys list

# Delete Wallet
selfchaind keys delete $WALLET

# Show Wallet Address
selfchaind keys show $WALLET -a

# Export Key (save to wallet.backup)
selfchaind keys export $WALLET

# Import Key
selfchaind keys import wallet.backup

# View EVM Prived Key
selfchaind keys unsafe-export-eth-key $WALLET


```
## Validator Operations


```bash
# check validator details
selfchaind query staking validator $VALOPER_ADDRESS

# check validator info
selfchaind status 2>&1 | jq

# Jailing info
selfchaind q slashing signing-info $(selfchaind tendermint show-validator)

# Slashing parameters
selfchaind q slashing params

# Unjail validator
selfchaind tx slashing unjail --from $WALLET --chain-id $SELFCHAIN_CHAIN_ID --gas-adjustment 1.2 --gas auto --gas-prices=0.5uslf 
```
## Service Operations


```bash
# Check Service Status
sudo systemctl status selfchaind

# Start Service
sudo systemctl start selfchaind

# Stop Service
sudo systemctl stop selfchaind

# Restart Service
sudo systemctl restart selfchaind

# Enable Service
sudo systemctl enable selfchaind

# Disable Service
sudo systemctl disable selfchaind

# View Logs
sudo journalctl -fu selfchaind -o cat

# Reload Service
sudo systemctl daemon-reload


```