(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });

    
})(jQuery);

function showLogin(role) {
    if (role === 'farmer') {
        window.location.href = '/farmer-login.html';
    } else if (role === 'company') {
        window.location.href = '/company-login.html';
    } else if (role === 'agrishop') {
        window.location.href = '/agrishop-login.html';
    }
}

// Toggle between Sign In and Sign Up forms
function toggleForm(type) {
    const signinForm = document.getElementById('farmer-signin');
    const signupForm = document.getElementById('farmer-signup');

    if (type === 'signin') {
        signinForm.style.display = 'block';
        signupForm.style.display = 'none';
    } else if (type === 'signup') {
        signinForm.style.display = 'none';
        signupForm.style.display = 'block';
    }
}

// app.js

document.addEventListener('DOMContentLoaded', () => {
    // Login Form Validation
    const loginForms = document.querySelectorAll('.auth-form form');
    loginForms.forEach(form => {
        form.addEventListener('submit', (event) => {
            const email = form.querySelector('input[name="email"]').value.trim();
            const password = form.querySelector('input[name="password"]').value.trim();

            if (!email || !password) {
                alert('Please fill in all fields.');
                event.preventDefault();
            }
        });
    });

    // Signup Form Validation
    const signupForms = document.querySelectorAll('.auth-form form');
    signupForms.forEach(form => {
        form.addEventListener('submit', (event) => {
            const email = form.querySelector('input[name="email"]').value.trim();
            const password = form.querySelector('input[name="password"]').value.trim();
            const confirmPassword = form.querySelector('input[name="confirm-password"]').value.trim();

            if (!email || !password || !confirmPassword) {
                alert('Please fill in all fields.');
                event.preventDefault();
            } else if (password !== confirmPassword) {
                alert('Passwords do not match.');
                event.preventDefault();
            }
        });
    });
});
