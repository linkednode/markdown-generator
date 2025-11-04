



# create-validator

## Check status


```bash
# check sync status, once your node is fully synced, the output from "catching_up" will print "false"
atomoned status 2>&1 | jq

```
## Create validator


```bash
atomoned tx staking create-validator \
--amount=1000000uatone \
--pubkey=$(atomoned tendermint show-validator) \
--moniker="$MONIKER" \
--chain-id=$ATOMONE_CHAIN_ID \
--commission-rate="0.10" \
--commission-max-rate="0.20" \
--commission-max-change-rate="0.01" \
--identity "" \
--details="" \
--min-self-delegation="1" \
--from=$WALLET \
--gas-adjustment 1.5 --gas auto --gas-prices=0.001uatone \
-y

```