



# create-validator

## Check status


```bash
# check sync status, once your node is fully synced, the output from "catching_up" will print "false"
dorad status 2>&1 | jq

```
## Create validator


```bash
dorad tx staking create-validator \
--amount=1000000000000000000peaka \
--pubkey=$(dorad tendermint show-validator) \
--moniker="$MONIKER" \
--chain-id=$DORA_CHAIN_ID \
--commission-rate="0.10" \
--commission-max-rate="0.20" \
--commission-max-change-rate="0.01" \
--identity "" \
--details="" \
--min-self-delegation="1" \
--from=$WALLET \
--gas-adjustment 1.5 --gas auto --gas-prices=10000000000peaka \
-y

```