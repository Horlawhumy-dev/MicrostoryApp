
// class HTTP {

//     async getData(url){
//         const response = await fetch(url);
//         const resData = await response.json();
//         return resData;
//     }

//     async postData(url, data){
//         const response = await fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-type': 'application/json'
//             },
//             body:  JSON.stringify(data)
//         });
//         const resData = await response.json();
//         return resData;
//     }

//     async updateData(url, data){
//         const response = await fetch(url, {
//             method: 'PUT',
//             headers: {
//                 "Content-type": "application/json"
//             },
//             body: JSON.stringify(data)
//         })

//         const resData = await response.json();
//         return resData;
//     }

//     // async deleteData(url, method, data){
//     //     const response = await fetch(url, {
//     //         method: method,
//     //         headers: {
//     //             "Content-Type": "Application/json"
//     //         },
//     //         body: data
//     //     })

//     //     const resData = await response.json();
//     //     return resData;
    
// }

// // Initiate class
// export const http  = new HTTP();