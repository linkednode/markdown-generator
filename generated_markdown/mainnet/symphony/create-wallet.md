



# create-wallet

## Create wallet


```bash
# to create a new wallet, use the following command. dont forget to save the mnemonic
symphonyd keys add $WALLET

# to restore exexuting wallet, use the following command
symphonyd keys add $WALLET --recover

# save wallet and validator address
WALLET_ADDRESS=$(symphonyd keys show $WALLET -a)
VALOPER_ADDRESS=$(symphonyd keys show $WALLET --bech val -a)
echo "export WALLET_ADDRESS="$WALLET_ADDRESS >> $HOME/.bashrc
echo "export VALOPER_ADDRESS="$VALOPER_ADDRESS >> $HOME/.bashrc
source $HOME/.bashrc

# before creating a validator, you need to fund your wallet and check balance
symphonyd query bank balances $WALLET_ADDRESS

```