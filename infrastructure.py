```python id="c9xp41"
from web3 import Web3
import json

RPC_ENDPOINT = "https://mainnet.base.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

web3 = Web3(
    Web3.HTTPProvider(RPC_ENDPOINT)
)

wallet = web3.eth.account.from_key(
    PRIVATE_KEY
)

project = "coinbookers"
network = "base"
category = "solution"

target_contract = Web3.to_checksum_address(
    "0x1234567890123456789012345678901234567890"
)

transaction = {
    "to": target_contract,
    "value": 0,
    "gas": 125000,
    "gasPrice": web3.eth.gas_price,
    "nonce": web3.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 8453,
    "data": "0x"
}

signed = web3.eth.account.sign_transaction(
    transaction,
    PRIVATE_KEY
)

result = {
    "project": project,
    "network": network,
    "type": category,
    "wallet": wallet.address,
    "contract": target_contract,
    "hash": signed.hash.hex()
}

print(
    json.dumps(
        result,
        indent=2
    )
)

# Optional send
# tx_hash = web3.eth.send_raw_transaction(
#     signed.raw_transaction
# )
# print(tx_hash.hex())

# solved
```
