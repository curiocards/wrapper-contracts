"""
import pytest

@pytest.fixture
# impersonate account that owns 35 unwrapped curio 17b
def cardHolder(accounts):
    return accounts["0xd8df722f43700b017f48908bc0af05e7d203f957"]

@pytest.fixture
# existing 17b contract
def curio17b(project):
    return project.CardToken.at("0xE0B5E6F32d657e0e18d4B3E801EBC76a5959e123")

#@pytest.fixture
#def oldWrapper(project):
#    return project.WrappedCurioCards.at("0x3c2754c0cdc5499df1a50d608d8985070bf87b30")

def test_migrate_success(project, accounts, curio17b, cardHolder):
    # todo remove this- use fixture instead
    oldWrapper = project.WrappedCurioCards.deploy(sender=accounts[1])

    # transfer 3 erc20 curios to accounts[0]
    curio17b.transfer(accounts[0].address, 3, sender=cardHolder)

    # wrap these up using the old wrapper
    curio17b.approve(oldWrapper.address, 2000, sender=accounts[0])
    oldWrapper.wrap(172, 3, sender=accounts[0])

    # assert balance is 3 in old wrapper
    assert oldWrapper.balanceOf(accounts[0].address, 172) == 3

    # deploy new wrapper
    #newWrapper = project.Curio17bERC1155Wrapper.deploy(sender=accounts[1])
    newWrapper = project.Curio17bERC1155Wrapper.deploy(oldWrapper.address, sender=accounts[1])

    # set approval on oldWrapper
    oldWrapper.setApprovalForAll(newWrapper.address, True, sender=accounts[0])
    # set approval on erc20
    curio17b.approve(newWrapper.address, 2000, sender=accounts[0])

    # then migrate to newWrapper
    newWrapper.migrate(172, 3, sender=accounts[0])

    # assert balance is 0 in old wrapper
    # assert balance is 3 in new wrapper

"""