import axios from 'axios';
import { env } from '$lib/env';

export async function get({ params }) {
	console.log("get trads")
	console.log(env.VITE_BACKEND_DNS)
	const url = `${env.VITE_BACKEND_DNS}/trad/`;
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
