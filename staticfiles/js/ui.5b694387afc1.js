
// class UI {
//     constructor(){
//         this.wrapper = document.querySelector('#post-comments');
//         this.container = document.querySelector('.container');
//         this.nameInput = document.querySelector('#user-name');
//         this.titleInput = document.querySelector('#user-title');
//         this.postInput = document.querySelector('#user-comment');
//     }
//     showPosts(posts){
//        let output = '';
//        posts.forEach(post => {
//            output += `  <section id=${post.id} class="mysection">
//            <div id="post" class="mypost">
//                <h4 id="my-names">${post.name}</h4>
//                <p class="title" >${post.title}</p>
//                <p id="my-comment">${post.post}</p>
//            </div>

//            <div class="button-div" id="edidel">
//                <button class="btn-edit" id="edit-button">edit</button>
//                <button class="btn-delete" id="delete-button">delete</button>
//                <div class="date-div"></div>
//            </div>
//        </section>`
//        }) 

//        this.wrapper.innerHTML = output;
//     }

//     clearUserInput(){
//         this.nameInput.value = '';
//         this.titleInput.value = '';
//         this.postInput.value = '';
//     }
// }

// // Initiate class
// export const ui = new UI();

