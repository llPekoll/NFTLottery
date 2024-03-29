import axios from 'axios';
import { env } from '$lib/env';

export async function get({ params }) {
	console.log("lotery ========")
	const url = `${env.VITE_BACKEND_DNS}/lottery/`;
	let response;
	try {
		response = await axios.get(url);
	} catch (error) {
		return { status: 500, body: error };
	}
	return {
		status: 200,
		body: response.data
	};
}
