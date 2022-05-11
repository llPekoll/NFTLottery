<script>
  import { getContext } from 'svelte';
  import Popup from './Popup.svelte';
  export let weGotBug
  const { open } = getContext('simple-modal');
  $: if(weGotBug) {

      open(Popup, { message: "👛 Please Verify if your wallet is connected 👛 <br /> 💰 And check if you have engough found💰 <br />" });
  }

</script>
