



# create-validator

## Check status


```bash
# check sync status, once your node is fully synced, the output from "catching_up" will print "false"
crossfid status 2>&1 | jq

```
## Create validator


```bash
crossfid tx staking create-validator \
--amount=10000000000000mpx \
--pubkey=$(crossfid tendermint show-validator) \
--moniker="$MONIKER" \
--chain-id=$CROSSFI_CHAIN_ID \
--commission-rate="0.10" \
--commission-max-rate="0.20" \
--commission-max-change-rate="0.01" \
--identity "" \
--details="" \
--min-self-delegation="1" \
--from=$WALLET \
--gas=auto --gas-adjustment=1.5 --gas-prices 10000000000000mpx \
-y

```