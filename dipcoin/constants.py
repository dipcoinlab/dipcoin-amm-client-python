# Copyright (c) 2025 Dipcoin LLC
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel

class ContractConstants(BaseModel):
    initial_package_id: str | None = None
    package_id: str
    admin_cap_id: str
    global_id: str
    pool_registry_table_id: str

CONTRACT_CONSTANTS = {
    "testnet": ContractConstants(
        initial_package_id="0x8fa1e6e1da7d34d15d867702a78e0ba391e08b28fac913b2d16c16301fe914bd",
        package_id="0x0d49def4e064373781d211d778f5779b7b655556983f4108a76cce8e216f2e55",
        admin_cap_id="0x80c9b8db86eb5c40a41967ac778a4372b9afa1e1d4a39b404369999f83e95cb7",
        global_id="0xf516a0a20187772473930686cae725880800eb3c1cc1a369dd97f3af3fbb06d5",
        pool_registry_table_id="0xa232533579e171deec78696dae61ae4cb4d181df9ca90da56db97cfed4774abd",
    )
}

NODE_RPC = {
    'testnet': 'https://fullnode.testnet.sui.io:443',
    'mainnet': 'https://fullnode.mainnet.sui.io:443',
}

TESTNET_FAUCET = {
    "package_id": "0x5c68f3d2ebfd711454da300d6abf3c7254dc9333cd138cdc68e158ebffd24483",
    "faucet_id": "0xce512917214d7e5b21b63f33ec2aebd923852bd3de27128c83f40d9a9f8bad35",
    "COIN_USDC": "0x5c68f3d2ebfd711454da300d6abf3c7254dc9333cd138cdc68e158ebffd24483::coins::USDC",
    "COIN_WSOL": "0x5c68f3d2ebfd711454da300d6abf3c7254dc9333cd138cdc68e158ebffd24483::coins::WSOL",
    "COIN_WETH": "0x5c68f3d2ebfd711454da300d6abf3c7254dc9333cd138cdc68e158ebffd24483::coins::WETH",
    "COIN_CETUS": "0x5c68f3d2ebfd711454da300d6abf3c7254dc9333cd138cdc68e158ebffd24483::coins::CETUS",
}

DEFAULT_SLIPPAGE = 0.005