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
    document.getElementById('farmer-login').style.display = 'none';
    document.getElementById('company-login').style.display = 'none';
    document.getElementById('agrishop-login').style.display = 'none';

    if (role === 'farmer') {
        document.getElementById('farmer-login').style.display = 'block';
    } else if (role === 'company') {
        document.getElementById('company-login').style.display = 'block';
    } else if (role === 'agrishop') {
        document.getElementById('agrishop-login').style.display = 'block';
    }
}

// app.js

document.addEventListener('DOMContentLoaded', () => {
    // Login Form Validation
    const loginForm = document.querySelector('form#loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            const email = loginForm.email.value.trim();
            const password = loginForm.password.value.trim();

            if (!email || !password) {
                alert('Please fill in all fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    }

    // Signup Form Validation
    const signupForm = document.querySelector('form#signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', (event) => {
            const username = signupForm.username.value.trim();
            const email = signupForm.email.value.trim();
            const password = signupForm.password.value.trim();
            const confirmPassword = signupForm.confirm_password.value.trim();

            if (!username || !email || !password || !confirmPassword) {
                alert('Please fill in all fields.');
                event.preventDefault(); // Prevent form submission
            }

            if (password !== confirmPassword) {
                alert('Passwords do not match.');
                event.preventDefault(); // Prevent form submission
            }
        });
    }
});

