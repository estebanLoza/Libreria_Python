document.addEventListener("DOMContentLoaded", () => {
  // ==========================================
  // 1. OBSERVADOR DE SCROLL (Para todas las páginas)
  // ==========================================
  const observer = new IntersectionObserver(
    (entradas) => {
      entradas.forEach((entrada) => {
        if (entrada.isIntersecting) {
          entrada.target.classList.add("visible");
        } else {
          // Remover la clase hace que la animación se repita al scrollear hacia arriba
          entrada.target.classList.remove("visible");
        }
      });
    },
    { threshold: 0.1 },
  );

  // ==========================================
  // 2. LÓGICA PARA INDEX.HTML (Elementos estáticos)
  // ==========================================
  const elementosEstaticos = document.querySelectorAll(
    ".card, #latinoAmerica, #renovacionID",
  );

  elementosEstaticos.forEach((elemento) => {
    elemento.classList.add("scroll-suave");
    observer.observe(elemento);
  });

  // ==========================================
  // 3. LÓGICA PARA LIBROS.HTML (Llamada a Flask)
  // ==========================================
  const contenedorLibros = document.getElementById("contenedor-libros");
  const templateLibro = document.getElementById("template-libro");

  if (contenedorLibros && templateLibro) {
    fetch("http://127.0.0.1:5000/api/libros")
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error("Error en la respuesta de Flask");
        return respuesta.json();
      })
      .then((libros) => {
        libros.forEach((libro) => {
          const cartaFragmento = templateLibro.content.cloneNode(true);
          const nodoCarta = cartaFragmento.querySelector(".carta-libro");

          cartaFragmento.querySelector(".titulo").textContent = libro.titulo;
          cartaFragmento.querySelector(".autor").textContent = libro.autor;
          cartaFragmento.querySelector(".sinopsis").textContent =
            libro.sinopsis;
          cartaFragmento.querySelector(".anio").textContent = libro.anio;
          cartaFragmento.querySelector(".genero").textContent = libro.genero;

          if (libro.portada) {
            cartaFragmento.querySelector(".portada").src = libro.portada;
          }

          nodoCarta.classList.add("scroll-suave");
          contenedorLibros.appendChild(cartaFragmento);
          observer.observe(nodoCarta);
        });
      })
      .catch((error) => console.error("Error al obtener libros:", error));
  }

  // ==========================================
  // 4. LÓGICA PARA PREMIONOBEL.HTML (Flask + Filtros)
  // ==========================================
  const contenedorNobel = document.getElementById("contenedor-nobels");
  const templateNobel = document.getElementById("template-nobel");
  const selectNacionalidad = document.getElementById("nacionalidad");

  // Variable para no perder los datos originales
  let todosLosNobels = [];

  // Función para llenar las opciones del filtro de nacionalidad
  function llenarSelectNacionalidades(listaDeNobels) {
    // Usamos Set para que no haya países repetidos
    const nacionalidadesUnicas = [
      ...new Set(listaDeNobels.map((autor) => autor.nacionalidad)),
    ];
    nacionalidadesUnicas.sort(); // Ordenamos alfabéticamente

    nacionalidadesUnicas.forEach((nacionalidad) => {
      const option = document.createElement("option");
      option.value = nacionalidad.toLowerCase();
      option.textContent = nacionalidad;
      selectNacionalidad.appendChild(option);
    });
  }

  // Función para dibujar las cartas en el HTML
  function renderizarNobels(listaDeNobels) {
    contenedorNobel.innerHTML = ""; // Limpia resultados anteriores

    listaDeNobels.forEach((autor) => {
      const cartaFragmento = templateNobel.content.cloneNode(true);
      const nodoCarta = cartaFragmento.querySelector(".article-nobel");

      cartaFragmento.querySelector(".nombre").textContent = autor.nombre;
      cartaFragmento.querySelector(".anio").textContent = autor.anio;
      cartaFragmento.querySelector(".nacionalidad").textContent =
        autor.nacionalidad;
      cartaFragmento.querySelector(".motivo").textContent = autor.motivo;

      nodoCarta.classList.add("scroll-suave");
      contenedorNobel.appendChild(cartaFragmento);
      observer.observe(nodoCarta);
    });
  }

  // Llamada principal a Flask cuando carga premioNobel.html
  if (contenedorNobel && templateNobel) {
    fetch("http://127.0.0.1:5000/api/nobel")
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error("Error en la respuesta de Flask");
        return respuesta.json();
      })
      .then((nobels) => {
        todosLosNobels = nobels; // Guardamos en memoria
        renderizarNobels(todosLosNobels); // Mostramos todos al inicio
        llenarSelectNacionalidades(todosLosNobels); // Llenamos el select
      })
      .catch((error) => console.error("Error al obtener nobels:", error));
  }

  // Lógica del botón de Filtro
  window.filtrar = function () {
    const nacionalidadElegida = selectNacionalidad.value.toLowerCase();
    const inputAnio = document.querySelector('input[name="anio"]').value;

    const nobelsFiltrados = todosLosNobels.filter((autor) => {
      const nacionalidadDelAutor = autor.nacionalidad.toLowerCase();
      const coincideNacionalidad =
        nacionalidadElegida === "todos" ||
        nacionalidadDelAutor === nacionalidadElegida;

      const anioDelAutor = autor.anio.toString();
      const coincideAnio = inputAnio === "" || anioDelAutor === inputAnio;

      return coincideNacionalidad && coincideAnio;
    });

    renderizarNobels(nobelsFiltrados); // Dibujamos solo los que coinciden
  };
});
