let newPassword = "";

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

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
    }

    document.getElementById('result').innerText = password;
    newPassword = password;
    return newPassword;
}

function copyToClipboard() {
    navigator.clipboard.writeText(newPassword).then(function() {
        alert('Text copied to clipboard');
    }).catch(function(err) {
        console.error('Error in copying text: ', err);
    });
}

// Assuming you want to attach the copyToClipboard function to a button click event
// document.getElementById('copyButton').addEventListener('click', copyToClipboard);

// document.getElementById('copyButton').addEventListener('click', copyToClipboard);
