let newPassword = "";

document.getElementById('mobile-menu').addEventListener('click', function() {
     document.querySelector('.nav-list').classList.toggle('active');
});

function generatePassword() {
    const length = parseInt(document.getElementById('length').value);
    const uppercase = document.getElementById('uppercase').checked;
    const lowercase = document.getElementById('lowercase').checked;
    const digits = document.getElementById('digits').checked;
    const symbols = document.getElementById('symbols').checked;

    let chars = '';
    if (uppercase) chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (lowercase) chars += 'abcdefghijklmnopqrstuvwxyz';
    if (digits) chars += '0123456789';
    if (symbols) chars += '!@#$%^&*()_+[]{}|;:,.<>?';

    if (chars === '') {
        document.getElementById('result').innerText = 'Please select at least one character type.';
        return;
    }

    /* ---- Add if conditions for limit of characters */
    if(length > 20) {
        result.innerText = 'Please select a number under 20';
        return;
    }
    if (length < 5) {
        result.innerText = 'Please select a number above 5';
        return;
    }


    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
        
    }

    document.getElementById('result').innerText = password;
    newPassword = password;
    return newPassword;

    // document.getElementById('copyButton').addEventListener('click', function() {
    //     copyToClipboard('#result');
    // });

}

// Copy Button
function copyToClipboard() {
    navigator.clipboard.writeText(newPassword).then(function() {
        alert('Text copied to clipboard');
    }).catch(function(err) {
        console.error('Error in copying text: ', err);
    });
}


/* ______________ Dashboard Buttons __________________ 
const userButtonsDiv = document.getElementById('user-btt');
const dashboardDiv = document.getElementById('dashboard-btn');

// Check if the current path is "/dashboard"
if (window.location.pathname === '/dashboard') {
    userButtonsDiv.style.display = 'none';  
    dashboardDiv.style.display = 'flex'; 
}*/

/* ______________ Copy Informations from dashboard __________________ */
function copy(that){
    var inp = document.createElement('input');  // Create a new input element
    document.body.appendChild(inp);             // Append the input to the body
    inp.value = that.textContent;               // Set the input's value to the textContent of the clicked element
    inp.select();                               // Select the input field
    document.execCommand('copy');               // Copy the selected text
    inp.remove();                               // Remove the input field from the DOM
    
    // Optional: Notify the user
    alert("Copied");
}

/* ______________ Copy password to Save input __________________ */
// Get Value form /home
function cutAndSave() {
    var passwordText = document.getElementById('result').textContent;
    localStorage.setItem('passwordValue', passwordText);
    document.getElementById('result').textContent = "";
    window.location.href = '/save';
}

// Put Value in /save
window.onload = function() {
    var savedPassword = localStorage.getItem('passwordValue');
    if (savedPassword) {
        document.getElementById('pwd').value = savedPassword;
        localStorage.removeItem('passwordValue');
    }
}