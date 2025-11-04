



# create-wallet

## Create wallet


```bash
# to create a new wallet, use the following command. dont forget to save the mnemonic
dorad keys add $WALLET

# to restore exexuting wallet, use the following command
dorad keys add $WALLET --recover

# save wallet and validator address
WALLET_ADDRESS=$(dorad keys show $WALLET -a)
VALOPER_ADDRESS=$(dorad keys show $WALLET --bech val -a)
echo "export WALLET_ADDRESS="$WALLET_ADDRESS >> $HOME/.bashrc
echo "export VALOPER_ADDRESS="$VALOPER_ADDRESS >> $HOME/.bashrc
source $HOME/.bashrc

# before creating a validator, you need to fund your wallet and check balance
dorad query bank balances $WALLET_ADDRESS

```