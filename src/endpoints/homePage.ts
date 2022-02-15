import {api} from '@/helpers/axios.config';


export async function getTotalsNumber() {
    let res = await api
    .get('dashboard');
     if (res) return res.data
     else
     return false
}


