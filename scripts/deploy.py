from brownie import FundMe
from scripts.helpful_scripts import get_account


def deploy_find_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account})
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_find_me()
