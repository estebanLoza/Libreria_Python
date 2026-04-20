//1 Cuando cargue la página. LLama a flask

fetch("http://127.0.0.1:5000/api/libros")
  .then((respuesta) => respuesta.json())
  .then((libros) => {
    const contenedor = document.getElementById("contenedor-libros");
    const template = document.getElementById("template-libro");

    libros.forEach((libro) => {
      // 2. Clona el template
      const carta = template.content.cloneNode(true);

      //3. LLena los datos
      carta.querySelector(".titulo").textContent = libro.titulo;
      carta.querySelector(".autor").textContent = libro.autor;
      carta.querySelector(".sinopsis").textContent = libro.sinopsis;
      carta.querySelector(".anio").textContent = libro.anio;
      carta.querySelector(".genero").textContent = libro.genero;
      carta.querySelector(".portada").src = libro.portada;
      contenedor.appendChild(carta);

      // Efecto scroll
      const observer = new IntersectionObserver(
        (entradas) => {
          entradas.forEach((entrada) => {
            if (entrada.isIntersecting) {
              entrada.target.classList.add("visible");
            } else {
              entrada.target.classList.remove("visible"); // se esconde al subir
            }
          });
        },
        { threshold: 0.1 },
      );

      // Observa cada carta
      document.querySelectorAll(".carta-libro").forEach((carta) => {
        observer.observe(carta);
      });
    });
  });
