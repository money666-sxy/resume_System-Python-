function register() {
    var elem = document.getElementById('modal1')
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    var phone = document.getElementById("phone").value
    var email = document.getElementById("email").value
    if(username == "") {
        var elem = document.getElementById('modal1')
        var instances = M.Modal.init(elem)
    } else {
        alert(phone)
        alert(email)
        document.getElementById("reg_form").submit()
    }
}






