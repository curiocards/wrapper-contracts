pragma solidity ^0.5.0;

import "./AbstractWrapper.sol";

contract Curio17bERC1155Wrapper is AbstractWrapper {

    function initialize() internal {
        // TODO change to 0xE0B5E6F32d657e0e18d4B3E801EBC76a5959e123
        // TODO replace with metadata json that points to new image
        create(172, 0x4Dc10B9c07DC00A6af5F8441324B8429D1e2C043, "ipfs://QmRRTcJDTBHC8HfbNREfHarzw3yGi8pkJbwnbPBBRhr5BX");
    }

    constructor() AbstractWrapper() public {}
}
