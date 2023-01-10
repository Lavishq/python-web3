from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    account = accounts[0]
    # account = accounts.load('acc') # load added accounts of brownie
    print(account)
    # or add account using `brownie accounts new acc` then enter pkey pre `0x`
    # `brownie accounts list`
    # `brownie accounts delete acc`
    # also env can be used using the yaml of the repo
    # account = accountS.add(os.getenv("PRIVATE_KEY"))
    # or even
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print((updated_stored_value))


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
