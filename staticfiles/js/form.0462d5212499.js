divmessage = document.querySelector('.divmessages');

setTimeout(function(){
    divmessage.fadeOut('slow');
},3000)

document.querySelector('#user_firstname').addEventListener('keydown', function(e){
    const re = /^([a-zA-Z]+)$/
 
    firstname = document.querySelector('#user_firstname').value
    if(!re.test(firstname)){
         showError('Unmatched values provided!', 'fail')
        console.log("Matched");
    }else{
         showError('Matched values', 'success')
        console.log("Not matched!");
    }
 })
 
//  form =  document.querySelector('form')
 
//  form.addEventListener('submit', function(e){
//      console.log("1223");
 
//      e.preventDefault()
//  })
 
 function showError(message, className){
     const error = document.createElement('div');
     error.className = className;
     error.textContent = message;
 
     const header = document.querySelector('#wrapper');
     header.appendChild(error)
 
     setTimeout(() =>{
           error.remove()
     }, 2000)
 }