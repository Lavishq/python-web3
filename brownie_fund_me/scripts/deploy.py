from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on persistent network like goerli, use the associated address
    # else deploy mocks

    # Here, below line checked if the network is development or not and performed accordingly
    # but currently since we are mocking on local chain so we deploy mock only if our chain is not stored in LOCAL_BLOCKCHAIN_ENVIRONMENTS( meaning it is persists locally )
    # if network.show_active() != "development":
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verfiy"),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()


# ganache persisting using `brownie networks add Ethereum ganache-local host=<link like http://127.0.0.1:8545> chainid=1337``
