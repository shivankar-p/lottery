from brownie import OurToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_sup = Web3.toWei(1000, "ether")
def deploy():
    acc = get_account()
    tok = OurToken.deploy(initial_sup, {"from": acc})

def main():
    deploy()