// LOGIN FUNCTION
async function loginUser(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password) {
        showMessage("Please fill all fields", "error");
        return;
    }

    try {
        const res = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                username: username,
                password: password
            })
        });

        if (res.redirected) {
            window.location.href = res.url;
        } else {
            const text = await res.text();
            showMessage(text, "error");
        }

    } catch (err) {
        showMessage("Server error", "error");
    }
}


// REGISTER FUNCTION
async function registerUser(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password) {
        showMessage("All fields required", "error");
        return;
    }

    if (password.length < 4) {
        showMessage("Password must be at least 4 characters", "error");
        return;
    }

    try {
        const res = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                username: username,
                password: password
            })
        });

        if (res.redirected) {
            window.location.href = res.url;
        } else {
            showMessage("Registration successful. Please login.", "success");
        }

    } catch (err) {
        showMessage("Error occurred", "error");
    }
}


// MESSAGE DISPLAY FUNCTION
function showMessage(msg, type) {
    let box = document.getElementById("msg");

    if (!box) {
        box = document.createElement("div");
        box.id = "msg";
        document.body.prepend(box);
    }

    box.innerText = msg;
    box.className = type;

    setTimeout(() => {
        box.innerText = "";
    }, 3000);
}