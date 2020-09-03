function myfunc() {
    if (document.getElementById('Title').innerHTML == 'First Title') {
        document.getElementById('Title').innerHTML = 'New Title';
    } else {
        document.getElementById('Title').innerHTML = 'First Title';
    }
}