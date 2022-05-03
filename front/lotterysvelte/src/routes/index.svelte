
<script >
    import Header from "./Header.svelte";

    import { onMount } from 'svelte';

	let SendTransactionNFTL;
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
	onMount(
	  async () => {
			provider = new ethers.providers.Web3Provider(window.ethereum)
			SendTransactionNFTL = async () => {
				let subContract = new ethers.Contract(subContractAddress, subContractAbi, provider.getSigner())
				const amount =  ethers.utils.parseUnits('10.0', 9)
				let tx = await subContract.transfer("0x89a46Bc0835806008EaE03855e21852f463e6462",amount)
				console.log(tx)
			}
	  })
</script>
<section class=" hero tracking-widest">
<Header {subContractAddress} {provider} {subContractAbi}/>
<h1 class="text-3xl font-bold text-yellow-300 text-center  pt-32 drop-shadow-xl">
    The Lottery Test
</h1>
	<div  class="text-center w-1/2 mx-auto text-white">
		<p class="text-6xl pt-20  font-semibold drop-shadow-xl">
			Prices:
		</p>
		<ol class="text-3xl text-left w-2/3 mx-auto py-10 font-normal">
			<li class="text-5xl py-2 drop-shadow-xl">
				1. 1 kilo de cacahouette
			</li>
			<li class="text-4xl py-2 drop-shadow-xl">
				2. 1 NFTL
			</li>
			<li>
				3. 1 BNB
			</li>
		</ol>
	</div>
	<div class="text-center px-30 mb-20 tracking-widest">
		<button on:click={SendTransactionNFTL} class="bg-gradient-to-br from-pink-500 to-orange-400 rounded-full px-20 py-4 text-white border-4 border-orange-800 drop-shadow-md">
			<p class="text-3xl font-semithin drop-shadow-xl">
				Buy Ticket 
			</p>
		</button>
	</div>

	<div class=" bg-trasparent">
		<svg  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 10" preserveAspectRatio="none" class=" inline-block align-bottom relative w-full h-32">
		<polygon points="100 0 100 10 0 10" />
		</svg>
	</div>
</section>
<section class="winner text-yellow-400">

	<h2 class="text-4xl text-center mx-auto ">Last Winners:</h2>

	<ol class="text-3xl text-left w-1/2 mx-auto py-10 font-normal">
		<li class="text-5xl py-2 drop-shadow-xl">
			1. 1 kilo de cacahouette -> 0x3erfsf
		</li>
		<li class="text-4xl py-2 drop-shadow-xl">
			2. 1 NFTL -> 0x3erfsf
		</li>
		<li>
			3. 1 BNB -> 0x3erfsf
		</li>
	</ol>

</section>
<footer class="winner text-center mx-auto py-10 text-3xl">
	contact@fasdf.com
</footer>
<style>
	svg{
		fill:#aa7e40;
	}
	.hero
	{
		font-family: 'Kanit', sans-serif;
		background: rgb(105,50,0);
background: radial-gradient(circle, rgba(105,50,0,1) 0%, rgba(26,0,5,1) 100%);
	}
	.winner{
		background-color:  #aa7e40;
	}
</style>