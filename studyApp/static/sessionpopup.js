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
var userModal = document.getElementById('signout');
var userBg = document.querySelector('.user-bg');

<<<<<<< HEAD
=======

//var courses = document.querySelector('.list');

//var lithum = document.querySelector('.classes');

//var current_course;
/*window.onload= function(){
    courses = document.getElementsByClassName('list')
    window.alert('he')
}*/
//var lithum = courses[0]
//var section = courses[1]
//var lithum_a = lithum.children[0]
//var section_a = section.children[0]

   //child = courses[0]

    /*current_course = document.querySelector('.active');
    if(current_course != null){
        current_course.classList.toggle('active');
        window.alert('yeehaw1')
        child.classList.toggle('active');
    }
    else{
        
        window.alert('juul25')
    }*/

/*
function course2(){
    courses = document.getElementsByClassName('list');
    child = courses[1]
    var current_course = document.querySelector('.active');
    if(current_course != null){
        current_course.classList.toggle('active');
        window.alert('yeehaw2')
        child.classList.toggle('active');
    }
    else{
        child.classList.toggle('active');
        window.alert('juul18')
    }
}*/


/*for(var i = 0; i < courses.length; i++){

    var sectionCourse = courses[i]
    sectionCourse.addEventListener('click', function(){
        var current_course = document.querySelector('.active')
        if(current_course != null){
            current_course.classList.remove('active');
            window.alert('yeehaw')
            sectionCourse.children[0].classList.add('active');
        }
        else{
            window.alert(sectionCourse.children[0])
            sectionCourse.children[0].classList.add('active');
        }
        
    })
}*/

>>>>>>> 72e859f4aed96f3d3d32d870addda1ad98daf3c3

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
<<<<<<< HEAD
}

userModal.addEventListener('click', function(){
    userBg.classList.add('user-active');
});

userBg.addEventListener('click', function(){
    userBg.classList.remove('user-active'); 
})
  
   //stores the value from the input field and creates a room with it
   
   function createRoom(){

    var name;

    var input = document.getElementById('description').value;
=======
    
    var courses = document.querySelectorAll('.list');
>>>>>>> 72e859f4aed96f3d3d32d870addda1ad98daf3c3

    var location = window.location.pathname;
    if(location == '/section/'){
        courses[1].classList.add('active')
        courses[1].children[0].children[0].classList.remove('far')
        courses[1].children[0].children[0].classList.add('fa')
    }
    else{
        courses[0].classList.add('active')
        courses[0].children[0].children[0].classList.remove('far')
        courses[0].children[0].children[0].classList.add('fa')
    }
    //courses.addEventListener('click', function(){
    //    lithum.classList.add('active');
    //});
    
}

userModal.addEventListener('click', function(){
    userBg.classList.add('user-active');
});

userBg.addEventListener('click', function(){
    userBg.classList.remove('user-active'); 
})
 
   //stores the value from the input field and creates a room with it
   
 /*

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
    })*/
/*
    
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
    var currentRooms = document.getElementsByClassName('COMS_1004C')[0]
    var prevRooms = document.getElementsByClassName('MATH_25C')[0]
    prevRooms.style.display="none"
    currentRooms.style.display="inline-block"
    
    var header = document.getElementsByClassName('banner_2')[0]
    var name = getCurrentCourseName()
    header.innerHTML=`<h1>
    Welcome to CS 50!
    </h1>
    <p>Here you can find study groups for assignments you are working on.</p>
    `
    
});*/


//var scale = Math.min(         //making elements resizable 
  //    availableWidth / contentWidth, 
  //    availableHeight / contentHeight 
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
  

  
//resizing stuff 


var banner_2 = document.querySelector('.banner_2')

function removeBanner(){
    if(window.width() <= 800){
        banner_2.remove()
    }
}

//online header 


/*
var onlineNow = document.getElementById('#online-header');
var users = document.querySelector('.online')

onlineNow.addEventListener('click', function(){
    onlineNow.classList.remove(users);

});

*/
// Course Tab Navigation


<<<<<<< HEAD
     currentRooms.removeChild(room);
 }
//resizing stuff 
 /*
$(function () {
    var isAdded = false;
    $(window).resize(function () {
        if (!isAdded && $(window).width() > 641) {
             isAdded = true;
        } else if (isAdded && $(window).width() <= 641) {
            isAdded = false;
            $('.banner_2').remove();
        }
    });
});
*/

var banner_2 = document.querySelector('.banner_2')

function removeBanner(){
    if(window.width() <= 800){
        banner_2.remove()
    }
}

//online header 

var onlineNow = document.getElementById('#online-header');
var users = document.querySelector('.online')

onlineNow.addEventListener('click', function(){
    onlineNow.classList.remove(users);

});
//flipping the card
/*
    var flip = document.getElementById("flip");
    var roomExample = docoument.querySelector('.current_room_example');


    flip.addEventListener('click', function(){
        roomExample.classList.remove('back');
    })
    
*/

//signing in button
/*
$(".google-button").click(function() {
    window.location = $(this).find("a").attr("href"); 
    return false;
  });
*/


var onlineNowButton = document.getElementById('online-header')
var users = document.querySelector('.online')
var onlineNow = document.getElementById('online-now');

window.onload = function(){
onlineNow.addEventListener('click', function(){
    onlineNow.classList.remove('online');
})
}
//navbar 

const sections = document.querySelectorAll('section');
const bubble = document.querySelector('.bubble');

const colors = [
    ''
]

//removing login graphic
var login_graphic = document.querySelector('.login-graphic');

function removeLoginGraphic(){
    if(window.width() <= 800){
        login_graphic.remove()
    }
}

//login page scrollmagic 
$(document).ready(function(){

    var controller = new ScrollMagic.Controller();

    var ourScene = new ScrollMagic.Scene({
        triggerElement: '#how'
    })
    .setClassToggle('.punchline', 'fade-in')
    .addTo(controller);


});
=======
>>>>>>> 72e859f4aed96f3d3d32d870addda1ad98daf3c3
