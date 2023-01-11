from brownie import network, config, interface
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork-dev"]:
        get_weth()
    lending_pool = get_lending_pool()
    print(lending_pool)


def get_lending_pool():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    # Address from config
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    # Contract -> connecting abi with address (since abi is derived from interface)
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
