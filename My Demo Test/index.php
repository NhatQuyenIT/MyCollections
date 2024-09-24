<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Login Form</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="login-form">
        <form action="login.php" method="post">
            <h2>Login</h2>
            <div class="input-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" name="login">Login</button>
        </form>
    </div>
</body>
<script>
    // Đoạn mã này có thể được nhúng trong thẻ <script> ở cuối body trong tệp HTML hoặc trong tệp .js riêng.
    document.querySelector('form').addEventListener('submit', function(event) {
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        if (username.trim() === '' || password.trim() === '') {
            alert('Please enter both username and password.');
            event.preventDefault();
        }
    });
</script>
</html>

<?php
// login.php
if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Giả sử đây là thông tin đăng nhập hợp lệ.
    $correct_username = 'admin';
    $correct_password = 'password';

    if ($username == $correct_username && $password == $correct_password) {
        echo "Login successful!";
    } else {
        echo "Invalid username or password!";
    }
}
?>
