/*
imageUrl = 'x';

gapi.load('auth2', function(){
  gapi.auth2.init();
})



function renderButton() {
    gapi.signin2.render('my-signin2', {
      'scope': 'profile email',
      'width': 240,
      'height': 50,
      'longtitle': true,
      'theme': 'dark',
      'onsuccess': onSuccess,
      'onfailure': onFailure
    });
  }

function onSignIn(googleUser) { //signing the user in

    var profile = googleUser.getBasicProfile();
    window.alert('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    window.alert(profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    window.open('index.html', '_blank');
  }


  function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
  }
  */
/*
  window.onload=function(){
  document.getElementById('#signout').addEventListener('click', function(){
    signOut();
    window.alert('Hello');

  });
}
*/

//login page text animation

 
  

