import { headerConfigKeyName, userRoleIdKeyname } from '@/app.config'

export function getAuthState(): boolean {
    let auth_state = localStorage.getItem(headerConfigKeyName) ? true : false;
    return auth_state;
}

// export function getRoleId(): number {
//     let roleId = localStorage.getItem(userRoleIdKeyname) ? JSON.parse(localStorage.getItem(userRoleIdKeyname)!) : 0;
//     return roleId;
// }




export function clearAuthInfo(){
    localStorage.removeItem(headerConfigKeyName);
    localStorage.removeItem(userRoleIdKeyname);
}


export function setHeaderConfig(header:any){
    localStorage.setItem(headerConfigKeyName,JSON.stringify(header))
}






export function getHeaderConfig() {
    return localStorage.getItem(headerConfigKeyName)?
    JSON.parse(localStorage.getItem(headerConfigKeyName)):
    {
        headers: {
            "Content-Type": "application/json",
            Accept: "application/json"
        }
    };
}




