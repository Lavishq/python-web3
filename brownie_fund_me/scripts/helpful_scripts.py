from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    # if network.show_active() == "development":
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying mocks...")
    if len(MockV3Aggregator) <= 0:  # if already deployed then don't redeploy
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("mocks deplyoed ")


# brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https:mainnet.infura.io/v3/$WEB3_INFURA_PROJECT_ID ...' like below
# brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/lol_put_your_api_key accounts=10 mnemonic=brownie port=8545
