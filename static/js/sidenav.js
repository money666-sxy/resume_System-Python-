function show_sidebar() {
    var elem = document.getElementById('slide-out');
    var instances = M.Sidenav.init(elem);
    instances.open()
}