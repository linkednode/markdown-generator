



# createvalidator

## Check status


```bash
# check sync status, once your node is fully synced, the output from "catching_up" will print "false"
symphonyd status 2>&1 | jq

```
## Create validator


```bash
cd $HOME
# Create validator.json file
echo "{\"pubkey\":{\"@type\":\"/cosmos.crypto.ed25519.PubKey\",\"key\":\"$(symphonyd tendermint show-validator | grep -Po '\"key\":\s*\"\K[^"]*')\"},
\"amount\": \"1000000note\",
\"moniker\": \"$MONIKER\",
\"identity\": \"\",
\"website\": \"\",
\"security\": \"\",
\"details\": \"\",
\"commission-rate\": \"0.1\",
\"commission-max-rate\": \"0.2\",
\"commission-max-change-rate\": \"0.01\",
\"min-self-delegation\": \"1\"
}" > validator.json

# Create a validator using the JSON configuration
symphonyd tx staking create-validator validator.json \
--from $WALLET \
--chain-id $SYMPHONY_CHAIN_ID \
--gas-adjustment 1.5 --gas auto --gas-prices 0.025note \
-y

```