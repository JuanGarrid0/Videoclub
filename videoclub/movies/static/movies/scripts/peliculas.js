console.log("Script cargado correctamente");

function buscarPelicula() {
    const query = document.getElementById("barraBusquedaPeliculas").value; // Obtiene el texto de búsqueda
    const url = "/BuscarPeliculas/"; // Ruta de la vista en Django
    const lista = document.getElementById("lista"); // Contenedor de resultados

    // Realiza la solicitud AJAX
    fetch(`${url}?q=${query}`)
        .then(response => response.json())
        .then(data => {
            lista.innerHTML = ""; // Limpia la lista anterior

            if (data.results.length > 0) {
                // Muestra los resultados
                data.results.forEach(entry => {
                    lista.innerHTML += `
                        <a href="/lista/${entry}">
                            <p id="pelicula">${entry}</p>
                            <img src="/static/movies/images/${entry}.jpg" alt="Portada de ${entry}" width="100">
                        </a>
                    `;
                });
            } else {
                lista.innerHTML = "<p>No se encontraron resultados</p>";
            }
        })
        .catch(error => console.error("Error al buscar películas:", error));
}

function loggedIn(){
 
 alert(`Hola, has iniciado sesión`);
}

function loggedOut(){
    alert(`Hola, has cerrado la sesión `);
}
 
function registrado(){

    alert(`Muchas gracias por registrarte`);

}
function condiciones(){
    const checkbox = document.getElementById('aceptar');
    const botonEnviar = document.getElementById('boton-enviar');
    
    if (checkbox.checked) {
        botonEnviar.hidden = false;  // Si el checkbox está marcado, habilita el botón
    } else {
        botonEnviar.hidden = true;  
    }

    checkbox.addEventListener('change', function() {
        if (this.checked) {
            botonEnviar.hidden = false;  
        } else {
            botonEnviar.hidden = true;   
        }
    });
}

function condicionRegistro(){
    const usuario = document.getElementById('username').value;
    const correo = document.getElementById('email').value;
    const pas = document.getElementById('password').value;
    const pass = document.getElementById('confirmation').value;
    const boton = document.getElementById('confirm');
    let relleno = false;
    
    if (pas === pass && correo !== "" && usuario !== "" && pas !== "") {
        relleno = true;
    }
    if (relleno) {
        boton.hidden = false;  
    } else {
        boton.hidden = true;  
    }

    

}

window.onload = function(){

    condiciones();
    condicionRegistro();
}

