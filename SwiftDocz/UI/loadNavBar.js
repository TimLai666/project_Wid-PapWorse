
fetch('./navBar.html', {
        method: "GET"
    })
    .then(response => response.text())
    .then(html => {
        document.getElementById('navbar-placeholder').innerHTML = html;
    })
    .catch(error => {
        console.error('Error loading navbar:', error);
    });