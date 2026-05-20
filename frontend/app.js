let token = localStorage.getItem(
    "token"
);



async function register(){

try{

const response =
await fetch(

"http://127.0.0.1:8000/register",

{

method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:
JSON.stringify({

username:
document.getElementById(
"reg_username"
).value,

email:
document.getElementById(
"reg_email"
).value,

password:
document.getElementById(
"reg_password"
).value

})

})

const data =
await response.json()

console.log(data)

if(response.ok){

alert(
"Registration Successful"
)

}
else{

alert(
data.detail
)

}

}

catch(error){

console.log(error)

alert(
"Registration Failed"
)

}

}





async function login(){

try{

const response =
await fetch(

"http://127.0.0.1:8000/login",

{

method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:
JSON.stringify({

email:
document.getElementById(
"login_email"
).value,

password:
document.getElementById(
"login_password"
).value

})

})

const data =
await response.json()

token =
data.access_token

localStorage.setItem(

"token",

token

)

alert(
"Login Successful"
)

window.location.href =

"dashboard.html"

}

catch(error){

console.log(error)

alert(
"Login Failed"
)

}

}





async function createTask(){

const title =
document.getElementById(
"task_title"
).value


if(!title){

alert(
"Enter task title"
)

return

}


await fetch(

"http://127.0.0.1:8000/tasks",

{

method:"POST",

headers:{

Authorization:
`Bearer ${token}`,

"Content-Type":
"application/json"

},

body:
JSON.stringify({

title:title

})

})


document.getElementById(
"task_title"
).value=""

loadTasks()

}





async function loadTasks(){

if(!token){

return

}

const response =
await fetch(

"http://127.0.0.1:8000/tasks",

{

headers:{

Authorization:
`Bearer ${token}`

}

})

const tasks =
await response.json()

let html=""

tasks.forEach(task=>{

html += `

<div class="task">

<div class="task-content">

<div class="task-title">

${task.title}

</div>

<div class="task-status">

Status:

${
task.completed

?

"Completed"

:

"Pending"

}

</div>

</div>


<div class="task-buttons">

<button

class="complete-btn"

onclick=
"completeTask(
${task.id}
)"

>

Complete

</button>


<button

class="delete-btn"

onclick=
"deleteTask(
${task.id}
)"

>

Delete

</button>

</div>

</div>

`

})

document.getElementById(
"tasks"
).innerHTML =
html

}





async function completeTask(
id
){

await fetch(

`http://127.0.0.1:8000/tasks/${id}`,

{

method:"PUT",

headers:{

Authorization:
`Bearer ${token}`,

"Content-Type":
"application/json"

},

body:
JSON.stringify({

completed:true

})

})

loadTasks()

}





async function deleteTask(
id
){

await fetch(

`http://127.0.0.1:8000/tasks/${id}`,

{

method:"DELETE",

headers:{

Authorization:
`Bearer ${token}`

}

})

loadTasks()

}





function logout(){

localStorage.removeItem(
"token"
)

window.location.href =

"login.html"

}





window.onload = function(){

if(

window.location.pathname
.includes(
"dashboard"
)

){

loadTasks()

}

}