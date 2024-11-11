// login.js

// Simple form validation
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("login-form");
    
    form.addEventListener("submit", function (event) {
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        
        if (!email || !password) {
            alert("Please enter both email and password.");
            event.preventDefault();
        }
    });
});

// Google Sign-In success handler
function onSignIn(googleUser) {
    const profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId());
    console.log("Name: " + profile.getName());
    console.log("Email: " + profile.getEmail());

    // Redirect or send data to the backend here if needed
    // window.location.href = "/dashboard"; // Example redirect after sign-in
}

// Google Sign-Out
function signOut() {
    const auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log("User signed out.");
    });
}
