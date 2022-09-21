pragma solidity ^0.5.0;

import "./AbstractWrapper.sol";

contract Curio17bERC1155Wrapper is AbstractWrapper {

    function initialize() internal {
        create(172, 0xE0B5E6F32d657e0e18d4B3E801EBC76a5959e123, "ipfs://QmY2qTLrNmUvwVyKQF1JFqxSyZPtDH9cBo4CteLY3mtUYb"); // TODO replace with new image
    }

    constructor() AbstractWrapper() public {}
}
