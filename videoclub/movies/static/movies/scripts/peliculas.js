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