from brownie import SimpleStorage, accounts, config


def read_contract():
    # simple_storage = SimpleStorage[0]  # gets the first deployed contract
    simple_storage = SimpleStorage[-1]  # most recent deployed contract
    print(
        simple_storage.retrieve()
    )  # it already has contractAddress and abi since it was deployed


def main():
    read_contract()
