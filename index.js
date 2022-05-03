let provider;
const subContractAddress = "0x81663d5149cADBbc48CF1a7F21b05719Ee1420A9"
const subContractAbi = [
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": true,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]

window.onload = function () {

    if (window.ethereum !== "undefined") {
        this.ethereum.on("accountsChanged", handleAccountsChanged)

        window.ethereum.request({
            method: 'eth_accounts'
        }).then(handleAccountsChanged).catch((e) => {
            console.log(e)
        })
        provider = new ethers.providers.Web3Provider(window.ethereum)
    }
}


let account;

const handleAccountsChanged = (acc) => {
    console.log("account have been changed")
    account = acc;
}



const connectWallet = async () => {
    accounts = await window.ethereum.request({
        method: "eth_requestAccounts"
    }).catch((err) => {
        console.log(err.code)
    });

    account = accounts[0]
    let balance = await window.ethereum.request({
        method: "eth_getBalance",
        params: [
            account,
            'latest'
        ]
    }).catch((err) => {
        console.log(err.code)
    })
    console.log("balance")
    let amount = parseInt(balance) / Math.pow(10, 18)
    document.getElementById("amount").innerHTML = `${amount} BNB`

}



const SendTransaction = async () => {
    const params = [{
        "from": account,
        "to": "0x89a46Bc0835806008EaE03855e21852f463e6462",
        "gas": Number(21000).toString(16),
        "gasPrice": Number(2500000).toString(16),
        "value": Number(1000000000000000).toString(16),
        // "data": subContractAddress
    }]
    let transaction = await window.ethereum.request({
        method: "eth_sendTransaction",
        params
    });
}

const CheckFromContract = async () => {
    let subContract = new ethers.Contract(subContractAddress, subContractAbi, provider)
    let bal = await subContract.balanceOf(account)
    let amount = bal.toString() / Math.pow(10, 9)
    document.getElementById("amount").innerHTML = `${amount} $NFTL`
    console.log(`${amount} $NFTL`)

}


const SendTransactionNFTL = async () => {

    let subContract = new ethers.Contract(subContractAddress, subContractAbi, provider.getSigner())
    const amount =  ethers.utils.parseUnits('10.0', 9)
    let tx = await subContract.transfer("0x89a46Bc0835806008EaE03855e21852f463e6462",amount)
    console.log(tx)
}
