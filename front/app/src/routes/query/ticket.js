import axios from 'axios';
import { env } from '$lib/env';

export async function post({ request }) {
	console.log("ticket")
	const url = `${env.VITE_BACKEND_DNS}/ticket/`;
	const body = await request.json();
	let response;
	try {
		response = await axios.post(url, body);
	} catch (error) {
		return { status: 500, body: error };
	}
	return {
		status: 200,
		body: response.data
	};
}
