let token = localStorage.getItem(
"token"
)



async function register(){

const data={

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

}

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
JSON.stringify(
data
)

})

if(response.ok){

alert(
"Registration Successful"
)

window.location=
"login.html"

}
else{

alert(
"Registration Failed"
)

}

}




async function login(){

const response=
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

const data=
await response.json()

token=
data.access_token

localStorage.setItem(

"token",

token

)

window.location=
"dashboard.html"

}




async function createTask(){

const title=
document.getElementById(
"task_title"
).value


if(!title){

alert(
"Enter task"
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

const response=
await fetch(

"http://127.0.0.1:8000/tasks",

{

headers:{

Authorization:

`Bearer ${token}`

}

})

const data=
await response.json()

const tasks=
data.tasks || data


let html=""


tasks.forEach(task=>{

html+=`

<div class="task">

<h3>

${task.title}

</h3>

<p>

Status:

${task.completed

?

"Completed ✅"

:

"Pending ⏳"

}

</p>

<div class="btn-group">

<button
class="complete-btn"

onclick=
"completeTask(
${task.id}
)"

>

Mark Completed

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
).innerHTML=
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



window.onload=
function(){

if(

window.location.pathname
.includes(
"dashboard"
)

){

loadTasks()

}

}
function logout(){

localStorage.removeItem(
"token"
)

window.location=
"login.html"

}