import { api,updateAxiosHeader } from '@/helpers/axios.config';
import { getHeaderConfig, setHeaderConfig } from '@/helpers/utils'

export async function login(email: any, password: any) {

    let headerConfig: any = getHeaderConfig()
    let response = await api.post('authenticate/', { email: email, password: password })
    .then((response) => {
        headerConfig = {
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
                'Authorization': response.data['auth_token'],
                // 'client': response.headers['client'],
                // 'uid': response.headers['uid'],
            }
        }
        setHeaderConfig(headerConfig);
        updateAxiosHeader()


        return response;
    })
    return response;
}


