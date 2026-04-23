document.addEventListener("DOMContentLoaded", () => {
  // 1. CREAMOS EL OBSERVADOR UNA SOLA VEZ
  // Esto evita crear cientos de observadores en memoria cuando Flask devuelve muchos libros
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
  // LÓGICA PARA INDEX.HTML (Elementos estáticos)
  // ==========================================
  // Seleccionamos todo lo que queremos animar en el index
  const elementosEstaticos = document.querySelectorAll(
    ".card, #latinoAmerica, #renovacionID",
  );

  elementosEstaticos.forEach((elemento) => {
    // Les inyectamos la clase base y los mandamos a observar
    elemento.classList.add("scroll-suave");
    observer.observe(elemento);
  });

  // ==========================================
  // LÓGICA PARA LIBROS.HTML (Llamada a Flask)
  // ==========================================
  const contenedor = document.getElementById("contenedor-libros");
  const template = document.getElementById("template-libro");

  // El fetch solo se ejecuta si estamos en la página que tiene el contenedor y el template
  if (contenedor && template) {
    fetch("http://127.0.0.1:5000/api/libros")
      .then((respuesta) => {
        if (!respuesta.ok) {
          throw new Error("Error en la respuesta de red de Flask");
        }
        return respuesta.json();
      })
      .then((libros) => {
        libros.forEach((libro) => {
          // 2. Clonamos el template
          const cartaFragmento = template.content.cloneNode(true);

          // IMPORTANTÍSIMO: Capturamos el div contenedor de la carta ANTES de insertarlo
          const nodoCarta = cartaFragmento.querySelector(".carta-libro");

          // 3. Llenamos los datos desde la API
          cartaFragmento.querySelector(".titulo").textContent = libro.titulo;
          cartaFragmento.querySelector(".autor").textContent = libro.autor;
          cartaFragmento.querySelector(".sinopsis").textContent =
            libro.sinopsis;
          cartaFragmento.querySelector(".anio").textContent = libro.anio;
          cartaFragmento.querySelector(".genero").textContent = libro.genero;

          // Prevenimos un error si la API no devuelve una URL de portada válida
          if (libro.portada) {
            cartaFragmento.querySelector(".portada").src = libro.portada;
          }

          // Le agregamos la clase de la animación al nodo principal de esta carta
          nodoCarta.classList.add("scroll-suave");

          // 4. Insertamos la carta completa en el contenedor
          contenedor.appendChild(cartaFragmento);

          // 5. Le decimos al observador general que comience a vigilar esta nueva carta
          observer.observe(nodoCarta);
        });
      })
      .catch((error) =>
        console.error("Error al obtener libros desde Flask:", error),
      );
  }

  // ==========================================
  // LÓGICA PARA PREMIONONOBEL.HTML (Llamada a Flask)
  // ==========================================
  const contenedorNobel = document.getElementById("contenedor-nobels");
  const templateNobel = document.getElementById("template-nobel");

  if (contenedorNobel && templateNobel) {
    fetch("http://127.0.0.1:5000/api/nobel")
      .then((respuesta) => {
        if (!respuesta.ok) {
          throw new Error("Error en la respuesta de Flask");
        }
        return respuesta.json();
      })
      .then((nobels) => {
        nobels.forEach((autor) => {
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
      })
      .catch((error) =>
        console.error("Error al obtener nobels desde Flask:", error),
      );
  }
});
