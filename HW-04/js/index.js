$('#login-form').submit(async function(e) {
    e.preventDefault();
    if (validateCaptcha()) {
        // console.log(e)

        // console.log(sha256("@l!c3"));
        // console.log(sha256("B0b"));
        // console.log(sha256("Ch@rl!3"));
        // console.log(sha256("D@v3"));

        let credentials = {
            'username': '',
            'password': '',
        }

        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;
        let hashed_password = sha256(password);
        // console.log(password)
        // console.log(hashed_password)

        credentials.username = username;
        credentials.password = hashed_password;
        console.log(credentials);

        // Make the database connection
        $.getJSON("database.json", function(json) {
            console.log(json);
            let database = json['UserAccounts'];
            console.log(database);
            let index = database.username.indexOf(username);
            console.log(index);
            if (index !== -1 && hashed_password === database.password[index]) {
                console.log('successful login')
                localStorage.setItem('username', username);
                localStorage.setItem('clearance', database.clearance[index]);
                window.location.href = "http://127.0.0.1:5500/HW-04/homepage.html?";

            } else {
                alert("Username or password was incorrect")
            }
        });
    } else {
        document.getElementById('captchaTextBox').value = "";
    }
});