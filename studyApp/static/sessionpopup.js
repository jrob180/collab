
var index = 0;
const participants = [];
const classes = ['MATH_25C', 'COMS_1004C', 'ENG_LITC', 'FROSCI_DISCC'];

//getting user profile info 

var modal = document.querySelector('.modal');
var modalBtn = document.querySelector('.modal-btn');
var modalBg = document.querySelector('.modal-bg');
var modalClose = document.querySelector('.modal-close');
var errorModal = document.querySelector('.modal-error');
var classes1 = document.getElementById('COMS_1004');
var classes2 = document.getElementById('MATH_25');
var classes3 = document.getElementById('ENG_LIT');
var classes4 = document.getElementById('FROSCI_DISC');
var allClasses = document.getElementById('all_rooms');

function getCurrentCourse(){
    if (document.getElementById('MATH_25').classList.contains('current_page_item')){
        return 'MATH_25'
    }
    else if (document.getElementById('COMS_1004').classList.contains('current_page_item')) {
        return 'COMS_1004'
    }
    else if (document.getElementById('ENG_LIT').classList.contains('current_page_item')) {
        return 'ENG_LIT'
    }
    else if (document.getElementById('FROSCI_DISC').classList.contains('current_page_item')) {
        return 'FROSCI_DISC'
    }
    else if(document.getElementById('all_rooms').classList.contains('current_page_item')){
        return 'all_rooms'
    }

}   
function getCurrentCourseName(){
        var s = getCurrentCourse()
        return s.replace(/_/g, " ")
        }

window.onload=function(){   //displays and closes the modal (popup window)

    
    modalBtn.addEventListener('click', function(){
        modalBg.classList.add('bg-active');
    });
    
    modalClose.addEventListener('click', function(){
        modalBg.classList.remove('bg-active');
    });
}

   //stores the value from the input field and creates a room with it
   
   function createRoom(){

    var name;

    var input = document.getElementById('description').value;

    if(input.length < 29){
    name = input
    }
    else{
        name = input.substring(0,30) + "..."
    }

    modalBg.classList.remove('bg-active'); //takes away the modal 

    var room = document.createElement('div')

    if (document.getElementById('MATH_25').classList.contains('current_page_item')){
        room.classList.add('MATH_25C')
    }
    else if (document.getElementById('COMS_1004').classList.contains('current_page_item')) {
        room.classList.add('COMS_1004C')
    }
    else if (document.getElementById('ENG_LIT').classList.contains('current_page_item')) {
        room.classList.add('ENG_LITC')
    }
    else if (document.getElementById('FROSCI_DISC').classList.contains('current_page_item')) {
        room.classList.add('FROSCI_DISCC')
    } 

    room.classList.add('all_rooms')
    
    room.classList.add('current_room_example')
    
    var allRooms = document.getElementsByClassName('current_rooms')[0]
    var roomContents = `

        {% block content %}
			<p class = "name">${name}</p>

			<div class = "inner_room" id = ${index}>
				<div class = "user_bars">
                    <img src = "assets/IMG_6931.jpeg">
                    {% for post in posts %}
                        <p>{{Rooms.Users}}</p>
                    {% endfor %}
                </div>
            </div>
            <div class = "people">
				<button class = "join_room" onclick = "joinRoom(${index})">Join Room</button>
				<i class="fas fa-users"></i>
				<p>1</p>
            </div>
        {% endblock content %}
        `
    room.innerHTML = roomContents
    allRooms.append(room)
    participants.push(1)
    index++

    document.getElementById('description').value = ""
    }

    allClasses.addEventListener('click', function(){
        var s = getCurrentCourse() + 'C';
        var currentClass = document.getElementById(getCurrentCourse())
        allClasses.classList.add('current_page_item')
        currentClass.classList.remove('current_page_item')

        var len = document.getElementsByClassName(s).length
    for(var i = 0; i < len;i++){
        
        var prevRooms = document.getElementsByClassName(s)[i]
        prevRooms.style.display="none"
        
    }

    len = document.getElementsByClassName('all_rooms').length
    for(var i = 0; i<len;i++){
        var currentRooms = document.getElementsByClassName('all_rooms')[i]
        currentRooms.style.display="inline-block"
    }
    
    var header = document.getElementsByClassName('banner_2')[0]
    header.innerHTML=`<h1>
    Welcome to all current study sessions!
    </h1>
    <p>Here you can find study groups for assignments you are working on.</p>
    `
    })

   classes4.addEventListener('click',function(){
    //var s = getCurrentCourse()+'C';
    var currentClass = document.getElementById(getCurrentCourse())
    classes4.classList.add('current_page_item')
    currentClass.classList.remove('current_page_item')
    
        
    for(var j = 0; j < classes.length; j++){

        var len = document.getElementsByClassName(classes[j]).length
        for(var i = 0; i < len;i++){

            var prevRooms = document.getElementsByClassName(classes[j])[i]
            prevRooms.style.display="none"
        
        }
    }

    len = document.getElementsByClassName('FROSCI_DISCC').length
    for(var i = 0; i<len;i++){
        var currentRooms = document.getElementsByClassName('FROSCI_DISCC')[i]
        currentRooms.style.display="inline-block"
    }
    
    var header = document.getElementsByClassName('banner_2')[0]
    var name = getCurrentCourseName()
    header.innerHTML=`<h1>
    Welcome to ${name}!
    </h1>
    <p>Here you can find study groups for assignments you are working on.</p>
    `
});
classes3.addEventListener('click',function(){
    
    var currentClass = document.getElementById(getCurrentCourse())
    classes3.classList.add('current_page_item')
    currentClass.classList.remove('current_page_item')
    
    for(var j = 0; j < classes.length; j++){

        var len = document.getElementsByClassName(classes[j]).length
        for(var i = 0; i < len;i++){

            var prevRooms = document.getElementsByClassName(classes[j])[i]
            prevRooms.style.display="none"
        
        }
    }

    len = document.getElementsByClassName('ENG_LITC').length
    for(var i = 0; i<len;i++){
        var currentRooms = document.getElementsByClassName('ENG_LITC')[i]
        currentRooms.style.display="inline-block"
    }
    var header = document.getElementsByClassName('banner_2')[0]
    var name = getCurrentCourseName()
    header.innerHTML=`<h1>
    Welcome to ${name}!
    </h1>
    <p>Here you can find study groups for assignments you are working on.</p>
    `
});
classes2.addEventListener('click',function(){
    
    var currentClass = document.getElementById(getCurrentCourse())
    classes2.classList.add('current_page_item')
    currentClass.classList.remove('current_page_item')
    
    for(var j = 0; j < classes.length; j++){

        var len = document.getElementsByClassName(classes[j]).length
        for(var i = 0; i < len;i++){

            var prevRooms = document.getElementsByClassName(classes[j])[i]
            prevRooms.style.display="none"
        
        }
    }

    len = document.getElementsByClassName('MATH_25C').length
    for(var i = 0; i<len;i++){
        var currentRooms = document.getElementsByClassName('MATH_25C')[i]
        currentRooms.style.display="inline-block"
    }
    var header = document.getElementsByClassName('banner_2')[0]
    var name = getCurrentCourseName()
    header.innerHTML=`<h1>
    Welcome to ${name}!
    </h1>
    <p>Here you can find study groups for assignments you are working on.</p>
    `
});


classes1.addEventListener('click',function(){
    
    var currentClass = document.getElementById(getCurrentCourse())
    classes1.classList.add('current_page_item')
    currentClass.classList.remove('current_page_item')
    
    for(var j = 0; j < classes.length; j++){

        var len = document.getElementsByClassName(classes[j]).length
        for(var i = 0; i < len;i++){

            var prevRooms = document.getElementsByClassName(classes[j])[i]
            prevRooms.style.display="none"
        
        }
    }
    
    len = document.getElementsByClassName('COMS_1004C').length
    for(var i = 0; i<len;i++){
        var currentRooms = document.getElementsByClassName('COMS_1004C')[i]
        currentRooms.style.display="inline-block"
    }
    /*var currentRooms = document.getElementsByClassName('COMS_1004C')[0]
    var prevRooms = document.getElementsByClassName('MATH_25C')[0]
    prevRooms.style.display="none"
    currentRooms.style.display="inline-block"*/
    
    var header = document.getElementsByClassName('banner_2')[0]
    var name = getCurrentCourseName()
    header.innerHTML=`<h1>
    Welcome to CS 50!
    </h1>
    <p>Here you can find study groups for assignments you are working on.</p>
    `
    
});


//var scale = Math.min(         //making elements resizable 
  //    availableWidth / contentWidth, 
  //    availableHeight / contentHeight 
  //  );

function joinRoom(i){ //adding user cards to rooms

    var user = document.createElement('div')  
    user.classList.add("user_bars")
    var room = document.getElementById(i)
    var userTemplate = `
        
            <img src = "https://lh5.googleusercontent.com/-GJUFLxkUuV0/AAAAAAAAAAI/AAAAAAAAAAM/AMZuuckYZsWT2rHK6s9I0PgjslvdzREv1Q/s96-c/photo.jpg">
            <p>Jackson Roberts</p>
            
       
    `
    user.innerHTML = userTemplate
    room.append(user)

    updateParticipants(i);
  }
  

 /*function removeUser(){

    var user = document.createElement('div')  
    user.classList.add("user_bars")
    var room = document.getElementsByClassName('inner_room')[index]
    var userTemplate = `
        
            <img src = "assets/IMG_6931.jpeg">
            <p>Jackson Roberts</p>
       
    `
    user.innerHTML = userTemplate
    room.remove(user)
  }*/
function removeUser(i, j){
    var innerRoom = document.getElementsByClassName('inner_room')[i];
    var userBar = innerRoom.getElementsByClassName('user_bars')[j];
    innerRoom.removeChild(userBar);

    decreaseParticipants(i);
}

  
 function updateParticipants(i){

    participants[i] += 1;
    var room = document.getElementById(i)
    room.nextElementSibling.innerHTML = `             
    
        <button class = "join_room" onclick = "joinRoom(${i})">Join Room</button>
        <i class="fas fa-users"></i>
        <p>${participants[i]}</p>
    
    `
 }
 
 function decreaseParticipants(i){

    participants[i] -= 1;
    var room = document.getElementById(i)
    room.nextElementSibling.innerHTML = `             
    
        <button class = "join_room" onclick = "joinRoom(${i})">Join Room</button>
        <i class="fas fa-users"></i>
        <p>${participants[i]}</p>
    
    `
 }

 function removeRoom(i){
     var currentRooms = document.getElementsByClassName('current_rooms')[0];
     var room;

     if (document.getElementById('MATH_25').classList.contains('current_page_item')){
        room = currentRooms.getElementsByClassName('MATH_25C current_room_example')[i];
    }
    else if (document.getElementById('COMS_1004').classList.contains('current_page_item')) {
        room = currentRooms.getElementsByClassName('COMS_1004C current_room_example')[i];
    }
    else if (document.getElementById('ENG_LIT').classList.contains('current_page_item')) {
        room = currentRooms.getElementsByClassName('ENG_LITC current_room_example')[i];
    }
    else if (document.getElementById('FROSCI_DISC').classList.contains('current_page_item')) {
        room = currentRooms.getElementsByClassName('FROSCI_DISCC current_room_example')[i];
    } 

     currentRooms.removeChild(room);
 }
