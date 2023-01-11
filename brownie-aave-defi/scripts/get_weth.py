from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    get_weth()


def get_weth():
    """Mints weth by depositing eth"""

    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
    tx.wait(
        1
    )  # i did not use this for goerli get_weth call and it worked correctly twice
    print("received .1 eth")
    return tx
