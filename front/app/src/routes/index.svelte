<script context="module" lang="ts">
	export const prerender = false;
	export async function load({ url, fetch, session, context }) {
		const res = await fetch(`/query/trad`);
		const res2 = await fetch(`/query/lottery`);
		const res3 = await fetch(`/query/winner`);
		return {
			props: {
				trad: await res.json(),
				lottery: await res2.json(),
				winners: await res3.json()
			}
		};
	}
</script>

<script>
	import { onMount } from 'svelte';

	import Header from './Header.svelte';
	import Ticket from './Ticket.svelte';
	import Counter from './Counter.svelte';


  import Modal from 'svelte-simple-modal';
  import { browser } from '$app/env';
  import Content from './Content.svelte'


	export let trad;
	export let lottery;
	export let winners;

	let SendTransactionNFTL;
	let provider;
	let ticktNb = 1;
	let account;
	let paid = false;
	$: total = ticktNb * lottery.ticket_price;
	const subContractAddress = '0x81663d5149cADBbc48CF1a7F21b05719Ee1420A9';
	const subContractAbi = [
		{
			constant: true,
			inputs: [],
			name: 'name',
			outputs: [
				{
					name: '',
					type: 'string'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: false,
			inputs: [
				{
					name: '_spender',
					type: 'address'
				},
				{
					name: '_value',
					type: 'uint256'
				}
			],
			name: 'approve',
			outputs: [
				{
					name: '',
					type: 'bool'
				}
			],
			payable: false,
			stateMutability: 'nonpayable',
			type: 'function'
		},
		{
			constant: true,
			inputs: [],
			name: 'totalSupply',
			outputs: [
				{
					name: '',
					type: 'uint256'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: false,
			inputs: [
				{
					name: '_from',
					type: 'address'
				},
				{
					name: '_to',
					type: 'address'
				},
				{
					name: '_value',
					type: 'uint256'
				}
			],
			name: 'transferFrom',
			outputs: [
				{
					name: '',
					type: 'bool'
				}
			],
			payable: false,
			stateMutability: 'nonpayable',
			type: 'function'
		},
		{
			constant: true,
			inputs: [],
			name: 'decimals',
			outputs: [
				{
					name: '',
					type: 'uint8'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: true,
			inputs: [
				{
					name: '_owner',
					type: 'address'
				}
			],
			name: 'balanceOf',
			outputs: [
				{
					name: 'balance',
					type: 'uint256'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: true,
			inputs: [],
			name: 'symbol',
			outputs: [
				{
					name: '',
					type: 'string'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: false,
			inputs: [
				{
					name: '_to',
					type: 'address'
				},
				{
					name: '_value',
					type: 'uint256'
				}
			],
			name: 'transfer',
			outputs: [
				{
					name: '',
					type: 'bool'
				}
			],
			payable: false,
			stateMutability: 'nonpayable',
			type: 'function'
		},
		{
			constant: true,
			inputs: [
				{
					name: '_owner',
					type: 'address'
				},
				{
					name: '_spender',
					type: 'address'
				}
			],
			name: 'allowance',
			outputs: [
				{
					name: '',
					type: 'uint256'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			payable: true,
			stateMutability: 'payable',
			type: 'fallback'
		},
		{
			anonymous: false,
			inputs: [
				{
					indexed: true,
					name: 'owner',
					type: 'address'
				},
				{
					indexed: true,
					name: 'spender',
					type: 'address'
				},
				{
					indexed: false,
					name: 'value',
					type: 'uint256'
				}
			],
			name: 'Approval',
			type: 'event'
		},
		{
			anonymous: false,
			inputs: [
				{
					indexed: true,
					name: 'from',
					type: 'address'
				},
				{
					indexed: true,
					name: 'to',
					type: 'address'
				},
				{
					indexed: false,
					name: 'value',
					type: 'uint256'
				}
			],
			name: 'Transfer',
			type: 'event'
		}
	];
	let countdown;
	let weGotBug = false;
	onMount(async () => {
		provider = new ethers.providers.Web3Provider(window.ethereum);
		SendTransactionNFTL = async () => {
			let subContract = new ethers.Contract(
				subContractAddress,
				subContractAbi,
				provider.getSigner()
			);

			const amount = ethers.utils.parseUnits(`${total}.0`, 9);
			try{
				let tx = await subContract.transfer(lottery.lotery_wallet_address, amount);
			} catch {
				weGotBug = true
				return 0;
			}
			const data = {
				ticket_holder_wallet_address: account,
				ticket_nb: ticktNb,
				transation_id: 'wip',
				lotery_nb: lottery.lotery_nb
			};
			const posted = await fetch(`/query/ticket`, {
				method: 'POST',
				body: JSON.stringify(data)
			});
			paid = true;
		};
	});

	let countDownDate = new Date(lottery.date_end).getTime();
	
	let x = setInterval(function () {
		let now = new Date().getTime();
		let distance = countDownDate - now;

		let days = Math.floor(distance / (1000 * 60 * 60 * 24));
		let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		let seconds = Math.floor((distance % (1000 * 60)) / 1000);

		countdown = `${days}d ${hours}h  ${minutes}m  ${seconds}s`;

		if (distance < 0) {
			clearInterval(x);
			countdown = '!!!!! Done !!!!!';
		}
	}, 1000);
</script>

<section class=" hero tracking-widest">
	<Header {subContractAddress} {provider} {subContractAbi} bind:account {trad} />
	{#if lottery.error}
		<h1 class="text-7xl font-bold text-yellow-300 text-center  py-32 drop-shadow-xl underline">
			{trad.now_no_lottery}
		</h1>
	{:else if paid}
		<h1 class="text-7xl font-bold text-yellow-300 text-center  py-32 drop-shadow-xl underline">
			{trad.thanks}
		</h1>
	{:else}
		<h1 class="text-7xl font-bold text-yellow-300 text-center  pt-32 drop-shadow-xl underline">
			. {lottery.lotery_name} .
		</h1>
		{#if lottery.cashin_display}
			<h1 class="text-xl  text-white text-center drop-shadow-xl">
				{trad.current_cashin}: {lottery.cash_in} $NFTL
			</h1>
		{/if}
		<div class="text-3xl font-bold text-yellow-500 text-center  drop-shadow-xl pt-10">
			{trad.until}:
		</div>
		<div class="text-3xl font-bold text-yellow-500 text-center  drop-shadow-xl">
			{countdown}
		</div>
		<div class="text-center w-1/2 mx-auto text-white">
			<p class="text-6xl pt-20  font-semibold drop-shadow-xl">
				{trad.prices}:
			</p>
			<ol class="text-3xl text-left w-2/3 mx-auto py-10 font-normal">
				{#each lottery.prices as price, i}
					<li class="text-{7 - i * 3}xl py-1 drop-shadow-xl">
						{price.place}. {price.gain}
					</li>
				{/each}
			</ol>
		</div>
		<div class="text-center text-white">
			{trad.ticket_nb}
			<Counter bind:ticktNb />
			<div class="text-3xl font-bold text-yellow-300 text-center pt-5 drop-shadow-xl">
				{trad.total_price}: {total} $NFTL
			</div>
		</div>
	{#if browser}
	<Modal>
		<Content bind:weGotBug/>
	</Modal>
	{/if}
		<div class="text-center px-30 mb-20 tracking-widest pt-20 ">
			<button on:click={SendTransactionNFTL} class="drop-shadow-md">
				<Ticket />
			</button>
			<div class="text-center text-white pt-5 text-lg">
				{trad.ticket_price}: ${lottery.ticket_price}NFTL
			</div>
		</div>
		<div class="w-full text-center mx-auto py-10">
			<p class="text-white">
				{trad.need_more}
			</p>
			<a href={trad.get_nftl_link}>
				<button class="bg-red-500 text-yellow-300 rounded-lg py-2 px-10  ">
					{trad.get_nftl}
				</button>
			</a>
		</div>
	{/if}

	<div class=" bg-trasparent">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 100 10"
			preserveAspectRatio="none"
			class=" inline-block align-bottom relative w-full h-32"
		>
			<polygon points="100 0 100 10 0 10" />
		</svg>
	</div>
</section>
<section class="winner text-yellow-400">
	<h2 class="text-4xl text-center mx-auto ">{trad.last_winners}:</h2>
	<ol class="text-3xl text-left w-1/2 mx-auto py-10 font-normal">
		{#each winners.winners as winner, i}
			<li class="text-{5 - i * 2}xl py-2 drop-shadow-xl">
				{winner.place}. {winner.price} -> {winner.address}
			</li>
		{/each}
	</ol>
</section>
<footer class="winner text-center mx-auto py-10 text-3xl flex items-center justify-center ">
	<div class="text-yellow-300">
		<a href="mailto:{trad.email_link}">{trad.email}</a>
	</div>
	<a href={trad.twitter_link} class="tweet mx-10" target="_blank">
		<svg width="1em" height="1em" viewBox="0 0 1536 1536" class="fill-yellow-300"
			><path
				fill="#facc14"
				d="M1280 482q-56 25-121 34q68-40 93-117q-65 38-134 51q-61-66-153-66q-87 0-148.5 61.5T755 594q0 29 5 48q-129-7-242-65T326 422q-29 50-29 106q0 114 91 175q-47-1-100-26v2q0 75 50 133.5T461 885q-29 8-51 8q-13 0-39-4q21 63 74.5 104t121.5 42q-116 90-261 90q-26 0-50-3q148 94 322 94q112 0 210-35.5t168-95t120.5-137t75-162T1176 618q0-18-1-27q63-45 105-109zm256-194v960q0 119-84.5 203.5T1248 1536H288q-119 0-203.5-84.5T0 1248V288Q0 169 84.5 84.5T288 0h960q119 0 203.5 84.5T1536 288z"
			/></svg
		>
	</a>
</footer>
<p class="px-10 py-2 text-white winner text-yellow-300">{trad.general_condition}</p>

<style>
	svg {
		fill: #aa7e40;
	}
	.tweet {
		transform: scale(2);
	}
	.hero {
		font-family: 'Kanit', sans-serif;
		background: rgb(105, 50, 0);
		background: radial-gradient(circle, rgba(105, 50, 0, 1) 0%, rgba(26, 0, 5, 1) 100%);
	}
	.winner {
		background-color: #aa7e40;
	}
</style>
