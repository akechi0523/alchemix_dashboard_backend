amo_abi = [
    {
      "inputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "admin",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "operator",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "rewardReceiver",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "transmuterBuffer",
              "type": "address"
            },
            {
              "internalType": "contract IERC20",
              "name": "fraxShareToken",
              "type": "address"
            },
            {
              "internalType": "contract IERC20",
              "name": "curveToken",
              "type": "address"
            },
            {
              "internalType": "contract IStableSwap2Pool",
              "name": "twoPool",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "twoPoolSlippage",
              "type": "uint256"
            },
            {
              "internalType": "contract IConvexToken",
              "name": "convexToken",
              "type": "address"
            },
            {
              "internalType": "contract IConvexStakingWrapper",
              "name": "convexStakingWrapper",
              "type": "address"
            },
            {
              "internalType": "contract IConvexFraxBooster",
              "name": "convexFraxBooster",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "convexPoolId",
              "type": "uint256"
            }
          ],
          "internalType": "struct InitializationParams",
          "name": "params",
          "type": "tuple"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "target",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        },
        {
          "internalType": "bytes",
          "name": "data",
          "type": "bytes"
        }
      ],
      "name": "ERC20CallFailed",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "message",
          "type": "string"
        }
      ],
      "name": "IllegalArgument",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "message",
          "type": "string"
        }
      ],
      "name": "IllegalState",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "bytes",
          "name": "data",
          "type": "bytes"
        },
        {
          "internalType": "bytes",
          "name": "result",
          "type": "bytes"
        }
      ],
      "name": "MulticallFailed",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "message",
          "type": "string"
        }
      ],
      "name": "Unauthorized",
      "type": "error"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "admin",
          "type": "address"
        }
      ],
      "name": "AdminUpdated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "withdrawn",
          "type": "uint256"
        }
      ],
      "name": "BurnTwoPoolTokens",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amountFxs",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amountCurve",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amountConvex",
          "type": "uint256"
        }
      ],
      "name": "ClaimRewards",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        }
      ],
      "name": "DepositTwoPoolTokens",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256[2]",
          "name": "amounts",
          "type": "uint256[2]"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "mintedTwoPoolTokens",
          "type": "uint256"
        }
      ],
      "name": "MintTwoPoolTokens",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "mintedTwoPoolTokens",
          "type": "uint256"
        }
      ],
      "name": "MintTwoPoolTokens",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "operator",
          "type": "address"
        }
      ],
      "name": "OperatorUpdated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "pendingAdmin",
          "type": "address"
        }
      ],
      "name": "PendingAdminUpdated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "ReclaimTwoPoolAsset",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "rewardReceiver",
          "type": "address"
        }
      ],
      "name": "RewardReceiverUpdated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "transmuterBuffer",
          "type": "address"
        }
      ],
      "name": "TransmuterBufferUpdated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "twoPoolSlippage",
          "type": "uint256"
        }
      ],
      "name": "TwoPoolSlippageUpdated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        }
      ],
      "name": "WithdrawTwoPoolTokens",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "acceptAdmin",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "admin",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "burnTwoPoolTokens",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "withdrawn",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "claimRewards",
      "outputs": [
        {
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "convexFraxBooster",
      "outputs": [
        {
          "internalType": "contract IConvexFraxBooster",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "convexFraxVault",
      "outputs": [
        {
          "internalType": "contract IConvexFraxVault",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "convexPoolId",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "convexStakingWrapper",
      "outputs": [
        {
          "internalType": "contract IConvexStakingWrapper",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "convexToken",
      "outputs": [
        {
          "internalType": "contract IConvexToken",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "curveToken",
      "outputs": [
        {
          "internalType": "contract IERC20",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "depositTwoPoolTokens",
      "outputs": [
        {
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        },
        {
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "lockTime",
          "type": "uint256"
        }
      ],
      "name": "depositTwoPoolTokensCustomLock",
      "outputs": [
        {
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        },
        {
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        }
      ],
      "name": "emergencyRecall",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        }
      ],
      "name": "exchangeRate",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256[2]",
          "name": "amounts",
          "type": "uint256[2]"
        }
      ],
      "name": "flush",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "flush",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256[2]",
          "name": "amounts",
          "type": "uint256[2]"
        },
        {
          "internalType": "uint256",
          "name": "lockTime",
          "type": "uint256"
        }
      ],
      "name": "flushCustomLock",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "lockTime",
          "type": "uint256"
        }
      ],
      "name": "flushCustomLock",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "fraxShareToken",
      "outputs": [
        {
          "internalType": "contract IERC20",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        }
      ],
      "name": "getTokenForTwoPoolAsset",
      "outputs": [
        {
          "internalType": "contract IERC20",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "name": "kekId",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "timeLocked",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "mintTwoPoolTokens",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "minted",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256[2]",
          "name": "amounts",
          "type": "uint256[2]"
        }
      ],
      "name": "mintTwoPoolTokens",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "minted",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes[]",
          "name": "data",
          "type": "bytes[]"
        }
      ],
      "name": "multicall",
      "outputs": [
        {
          "internalType": "bytes[]",
          "name": "results",
          "type": "bytes[]"
        }
      ],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "onERC20Received",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "operators",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pendingAdmin",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        }
      ],
      "name": "recall",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "reclaimTwoPoolAsset",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "rewardReceiver",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "operator",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "value",
          "type": "bool"
        }
      ],
      "name": "setOperator",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "value",
          "type": "address"
        }
      ],
      "name": "setPendingAdmin",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "value",
          "type": "address"
        }
      ],
      "name": "setRewardReceiver",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "value",
          "type": "address"
        }
      ],
      "name": "setTransmuterBuffer",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setTwoPoolSlippage",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "sweep",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "transmuterBuffer",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "twoPool",
      "outputs": [
        {
          "internalType": "contract IStableSwap2Pool",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "enum PoolAsset",
          "name": "asset",
          "type": "uint8"
        }
      ],
      "name": "twoPoolAssetReserves",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "twoPoolSlippage",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        }
      ],
      "name": "withdrawTwoPoolTokens",
      "outputs": [
        {
          "internalType": "bool",
          "name": "success",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]