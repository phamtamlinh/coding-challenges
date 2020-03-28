function solution(S, P, Q) {
    let l = S.length + 1;
    let [arrA, arrC, arrG, arrT] = [Array(l).fill(0), Array(l).fill(0), Array(l).fill(0), Array(l).fill(0)];

    
    for(let i=1; i<l; i++) {
        arrA[i] = arrA[i-1];
        arrC[i] = arrC[i-1];
        arrG[i] = arrG[i-1];
        arrT[i] = arrT[i-1];
        if(S[i-1] == 'A') {
            arrA[i]++;
        } else if (S[i-1] == 'C') {
            arrC[i]++;
        } else if (S[i-1] == 'G') {
            arrG[i]++;
        } else if (S[i-1] == 'T') {
            arrT[i]++;
        }
    }
    let result = [];
    for(let i=0; i<P.length; i++) {
        if(arrA[Q[i]+1] - arrA[P[i]] > 0) {
            result.push(1);
        } else if (arrC[Q[i]+1] - arrC[P[i]] > 0){
            result.push(2);
        } else if (arrG[Q[i]+1] - arrG[P[i]] > 0){
            result.push(3);
        } else if (arrT[Q[i]+1] - arrT[P[i]] > 0){
            result.push(4);
        }
    }
    return result;
}
