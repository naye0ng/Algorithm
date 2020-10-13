function solution(n, customers) {
    let kiosk = Array(n).fill(0);

    customers = customers.map(strDate => {
        let date = new Date(strDate.substring(0, 14)); 
        return date.setMinutes(date.getMinutes()+strDate.substring(15));
       
    });

    let available_kiosk = Array(n).fill(null).map((v, i) => [0, i]);
    while(customers.length > 0){
        for(let i = 0; i<n; i++){
            let k = available_kiosk[i][1];
            if(customers.length <= 0) {
                available_kiosk[i] = [99999999999999999999999999, k];
            }else{
                kiosk[k] += 1;
                available_kiosk[i] = [customers.shift(), k];
            }
        }

        available_kiosk.sort((a, b)=>{
            if(a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        })

        for(let i = 0; i<n; i++){
            available_kiosk[i][0] = 0;
        }
    }

    return Math.max(...kiosk);
}