// import { ui } from "./ui.js";
// import { http } from "./http.js";

// // form submit event listeners
// document.querySelector('#form').addEventListener('submit', function(e){
//     const nameInput = document.querySelector('#user-name');
//     const titleInput =  document.querySelector('#user-title');
//     const postIput =  document.querySelector('#user-comment');

//     // Validation
//     if(nameInput.value !== '' || titleInput.value !== '' || postIput.value !== ''){
//         // ui.displayUserPosts(nameInput.value, titleInput.value , postIput.value);
//         // clear user input having submitted post
//         ui.clearUserInput();
//         // get posts from json
//         http.getData('db.json')
//         .then(data => {
//         ui.showPosts(data);
//         })
//         .catch(err => {
//             console.log(err);
//         })
        
//     }else{
//         console.log('Something wrong');
//     }
//     e.preventDefault();
// })
