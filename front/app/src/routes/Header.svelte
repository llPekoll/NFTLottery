<script>
	import { onMount } from 'svelte';
	// import { ethers } from "https://cdn.ethers.io/lib/ethers-5.0.esm.min.js"
	export let provider;
	export let subContractAddress;
	export let subContractAbi;
	export let account;
	export let trad;

	let amount = trad.wallet;
	let connectWallet;

	onMount(async () => {
		provider = new ethers.providers.Web3Provider(window.ethereum);
		connectWallet = async () => {
			const accounts = await window.ethereum
				.request({
					method: 'eth_requestAccounts'
				})
				.catch((err) => {
					console.log(err.code);
				});
			account = accounts[0];
			let subContract = new ethers.Contract(subContractAddress, subContractAbi, provider);
			let bal = await subContract.balanceOf(account);
			amount = bal.toString() / Math.pow(10, 9);
			amount = `${amount.toFixed(2)} $NFTL`;
		};
	});
</script>

<section class="px-20 py-10">
	<div class="float-left text-3xl  italic pt-2 drop-shadow-xl">
		<img src="tgf-URPS.png" alt="logo" class="w-16" />
	</div>
	<div class="float-right flex oo">
		<div
			class="rounded-full border-2 border-rose-600 p-2 bg-gradient-to-br from-pink-500 to-orange-400 z-10 drop-shadow-xl"
		>
			<svg width="2em" height="2em" viewBox="0 0 256 256"
				><path
					fill=""
					d="M164 144a16 16 0 1 1 16 16a16 16 0 0 1-16-16Zm72-48v104a20.1 20.1 0 0 1-20 20H56a28.1 28.1 0 0 1-28-28V68.2A32.1 32.1 0 0 1 60 36h132a12 12 0 0 1 0 24H60a8.4 8.4 0 0 0-5.8 2.4A8.2 8.2 0 0 0 52 68v.2a8.4 8.4 0 0 0 8.5 7.8H216a20.1 20.1 0 0 1 20 20Zm-24 4H60.5a33.5 33.5 0 0 1-8.5-1.1V192a4 4 0 0 0 4 4h156Z"
				/></svg
			>
		</div>
		<button on:click={connectWallet}>
			<div
				class="text-xl text-white font-semibold rounded-full border-2 border-rose-600 px-10 h-10 mt-0.5 -ml-8 z-0 pt-1 bg-gradient-to-br from-pink-500 to-orange-400 drop-shadow-xl"
			>
				<p class="tracking-widest">
					{amount}
				</p>
			</div>
		</button>
	</div>
	<div class="clear-both" />
</section>

<style>
	path {
		@apply fill-white;
	}
	.oo {
		transform: scale(1.5);
	}
</style>
