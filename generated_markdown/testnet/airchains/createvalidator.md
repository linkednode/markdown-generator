



# createvalidator

## Check status


```bash
# check sync status, once your node is fully synced, the output from "catching_up" will print "false"
junctiond status 2>&1 | jq

```
## Create validator


```bash
cd $HOME
# Create validator.json file
echo "{\"pubkey\":{\"@type\":\"/cosmos.crypto.ed25519.PubKey\",\"key\":\"$(junctiond tendermint show-validator | grep -Po '\"key\":\s*\"\K[^"]*')\"},
\"amount\": \"1000000amf\",
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
junctiond tx staking create-validator validator.json \
--from $WALLET \
--chain-id $AIRCHAINS_CHAIN_ID \
--fees 200amf \
-y

```