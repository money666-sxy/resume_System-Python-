function register() {
    var elem = document.getElementById('modal1')
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    if(username == "") {
        var elem = document.getElementById('modal1')
        var instances = M.Modal.init(elem)
    } else {
        document.getElementById("register_form").submit()
    }
}






