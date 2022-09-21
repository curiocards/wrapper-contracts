# Curio Cards wrapper contracts

This repository contains the source code for each of the 3 wrappers in production:
* the ["Official" wrapper](contracts/officialWrapper), deployed at `0x73DA73EF3a6982109c4d5BDb0dB9dd3E3783f313`, with support for bulk wrap/unwrap and paid auditing
* the ["Bootleg" wrapper](contracts/bootlegWrapper), deployed at `0x3c2754c0CDc5499df1a50D608D8985070Bf87b30`, released a few days before the official one, with support for misprint card "17b"
* the [17b-specific wrapper](contracts/17bWrapper), not yet deployed, with support exclusively for card 17b

And also, for posterity:
* the code for the [original ERC-20 Curio Cards](contracts/17b-erc20.sol)

## Developing

This project uses [ApeWorX](https://docs.apeworx.io/ape/stable/index.html). Follow the quick start portion of their documentation to get started.

Copy `.env.sample` to `.env` and edit it to fill in etherscan and infura environment variables.

There is an unused test in [tests/test_migrate.py](tests/test_migrate.py), there's enough context there that you should be able to start writing tests easily enough.