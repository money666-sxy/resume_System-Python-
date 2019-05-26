function login() {
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    if(username == "" || password == "") {
        var elem = document.getElementById('modal1')
        var instances = M.Modal.init(elem)
        instances.open()
    }else {
        document.getElementById("log_form").submit()
    }
}






