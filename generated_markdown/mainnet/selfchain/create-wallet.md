



# create-wallet

## Create wallet


```bash
# to create a new wallet, use the following command. dont forget to save the mnemonic
selfchaind keys add $WALLET

# to restore exexuting wallet, use the following command
selfchaind keys add $WALLET --recover

# save wallet and validator address
WALLET_ADDRESS=$(selfchaind keys show $WALLET -a)
VALOPER_ADDRESS=$(selfchaind keys show $WALLET --bech val -a)
echo "export WALLET_ADDRESS="$WALLET_ADDRESS >> $HOME/.bashrc
echo "export VALOPER_ADDRESS="$VALOPER_ADDRESS >> $HOME/.bashrc
source $HOME/.bashrc

# before creating a validator, you need to fund your wallet and check balance
selfchaind query bank balances $WALLET_ADDRESS

```