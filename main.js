// document.getElementById('mobile-menu').addEventListener('click', function() {
//     document.querySelector('.nav-list').classList.toggle('active');
// });

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

    // test to add copy botton
    // document.getElementById('copyButton').addEventListener('click', function() {
    //     copyToClipboard('#result');
    // });

    if (!document.getElementById('copyButton').hasAttribute('data-copied')) {
        document.getElementById('copyButton').addEventListener('click', function() {
            copyToClipboard('#result');
        });
        document.getElementById('copyButton').setAttribute('data-copied', 'true');
    }

}

// function to copythe generated password

function copyToClipboard(text) {
    let dummy = document.createElement("textarea");
    dummy.value = document.querySelector(text).textContent;
    document.body.appendChild(dummy);
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
    // alert('Password copied to clipboard!');
}