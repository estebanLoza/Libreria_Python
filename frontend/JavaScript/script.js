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
  const inputBusqueda = document.getElementById("busqueda-autor-libro-section");
  const botonBuscar = document.getElementById("button-autor-libro-section");
  const botonReset = document.getElementById("button-reset-auto-libro");

  let todosLosLibros = [];

  function renderizarLibros(lista) {
    contenedorLibros.innerHTML = "";

    lista.forEach((libro) => {
      const cartaFragmento = templateLibro.content.cloneNode(true);
      const nodoCarta = cartaFragmento.querySelector(".carta-libro");

      cartaFragmento.querySelector(".titulo").textContent = libro.titulo;
      cartaFragmento.querySelector(".autor").textContent = libro.autor;
      cartaFragmento.querySelector(".sinopsis").textContent = libro.sinopsis;
      cartaFragmento.querySelector(".anio").textContent = libro.anio;
      cartaFragmento.querySelector(".genero").textContent = libro.genero;

      if (libro.portada) {
        cartaFragmento.querySelector(".portada").src = libro.portada;
      }

      nodoCarta.classList.add("scroll-suave");
      contenedorLibros.appendChild(cartaFragmento);
      observer.observe(nodoCarta);
    });
  }

  if (contenedorLibros && templateLibro) {
    fetch("http://127.0.0.1:5000/api/libros")
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error("Error en la respuesta de Flask");
        return respuesta.json();
      })
      .then((libros) => {
        todosLosLibros = libros;
        renderizarLibros(todosLosLibros);

        // Llena el datalist con autores únicos
        const autoresUnicos = [...new Set(libros.map((l) => l.autor))];
        const datalist = document.getElementById("sugerencias-autores");
        if (datalist) {
          autoresUnicos.forEach((autor) => {
            const option = document.createElement("option");
            option.value = autor;
            datalist.appendChild(option);
          });
        }
      })
      .catch((error) => console.error("Error al obtener libros:", error));

    // Busca al hacer click en Buscar
    if (botonBuscar) {
      botonBuscar.addEventListener("click", () => {
        const busqueda = inputBusqueda.value.toLowerCase().trim();
        if (busqueda === "") {
          renderizarLibros(todosLosLibros);
          return;
        }
        const filtrados = todosLosLibros.filter((libro) =>
          libro.autor.toLowerCase().includes(busqueda),
        );
        renderizarLibros(filtrados);
      });
    }

    // Reset — limpia y muestra todos
    if (botonReset) {
      botonReset.addEventListener("click", () => {
        inputBusqueda.value = "";
        renderizarLibros(todosLosLibros);
      });
    }
  }

  // ==========================================
  // 4. LÓGICA PARA PREMIONOBEL.HTML (Flask + Filtros)
  // ==========================================
  const contenedorNobel = document.getElementById("contenedor-nobels");
  const templateNobel = document.getElementById("template-nobel");
  const selectNacionalidad = document.getElementById("nacionalidad");

  let todosLosNobels = [];

  function llenarSelectNacionalidades(listaDeNobels) {
    const nacionalidadesUnicas = [
      ...new Set(listaDeNobels.map((autor) => autor.nacionalidad)),
    ];
    nacionalidadesUnicas.sort();

    nacionalidadesUnicas.forEach((nacionalidad) => {
      const option = document.createElement("option");
      option.value = nacionalidad.toLowerCase();
      option.textContent = nacionalidad;
      selectNacionalidad.appendChild(option);
    });
  }

  function renderizarNobels(listaDeNobels) {
    contenedorNobel.innerHTML = "";

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

  if (contenedorNobel && templateNobel) {
    fetch("http://127.0.0.1:5000/api/nobel")
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error("Error en la respuesta de Flask");
        return respuesta.json();
      })
      .then((nobels) => {
        todosLosNobels = nobels;
        renderizarNobels(todosLosNobels);
        llenarSelectNacionalidades(todosLosNobels);
      })
      .catch((error) => console.error("Error al obtener nobels:", error));
  }

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

    renderizarNobels(nobelsFiltrados);
  };

  // ==========================================
  // 5. LÓGICA PARA GENEROS.HTML (Flask + Filtro)
  // ==========================================
  const contenedorGenero = document.getElementById("contenedor-generos-libro");
  const templateGenero = document.getElementById("template-genero");
  const selectGenero = document.getElementById("genero-libros");

  const generos = [
    "Romance",
    "Ficción Filosófica",
    "Realismo Mágico",
    "Cuento",
    "Ficción Histórica",
    "Fábula",
    "Narrativa",
  ];

  if (selectGenero) {
    generos.forEach((genero) => {
      const option = document.createElement("option");
      option.value = genero;
      option.textContent = genero;
      selectGenero.appendChild(option);
    });
  }

  window.filtrarGenero = function () {
    const generoElegido = selectGenero.value;

    if (generoElegido === "todos") {
      document.getElementById("genero-seleccionado").textContent =
        "Todos los géneros aquí en uno solo";

      fetch("http://127.0.0.1:5000/api/libros")
        .then((respuesta) => respuesta.json())
        .then((libros) => {
          contenedorGenero.innerHTML = "";
          libros.forEach((libro) => {
            const fragmento = templateGenero.content.cloneNode(true);
            const nodo = fragmento.querySelector(".libro-box-genero");
            fragmento.querySelector(".titulo-genero-libros").textContent =
              libro.titulo;
            fragmento.querySelector(".libro-escrito-autor").textContent =
              libro.autor;
            if (libro.portada) {
              fragmento.querySelector(".portada-genero").src = libro.portada;
            }
            nodo.classList.add("scroll-suave");
            nodo.classList.add("visible");
            contenedorGenero.appendChild(fragmento);
            observer.observe(nodo);
          });
        });
      return;
    }

    document.getElementById("genero-seleccionado").textContent =
      `Libros de '${generoElegido}'`;

    fetch(
      `http://127.0.0.1:5000/api/libros/genero/${encodeURIComponent(generoElegido)}`,
    )
      .then((respuesta) => respuesta.json())
      .then((libros) => {
        contenedorGenero.innerHTML = "";
        libros.forEach((libro) => {
          const fragmento = templateGenero.content.cloneNode(true);
          const nodo = fragmento.querySelector(".libro-box-genero");
          fragmento.querySelector(".titulo-genero-libros").textContent =
            libro.titulo;
          fragmento.querySelector(".libro-escrito-autor").textContent =
            libro.autor;
          if (libro.portada) {
            fragmento.querySelector(".portada-genero").src = libro.portada;
          }
          nodo.classList.add("scroll-suave");
          nodo.classList.add("visible");
          contenedorGenero.appendChild(fragmento);
          observer.observe(nodo);
        });
      })
      .catch((error) => console.error("Error al obtener géneros:", error));
  };

  // ==========================================
  // 6. LÓGICA PARA ADMINSTRADORES.html
  // ==========================================

  // En script.js — sección 6
  const loginForm = document.querySelector(".login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault(); // evita que recargue la página

      const usuario = document.querySelector(
        ".login-form input[type='text']",
      ).value;
      const password = document.querySelector(
        ".login-form input[type='password']",
      ).value;

      fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ usuario, password }),
      })
        .then((respuesta) => respuesta.json())
        .then((datos) => {
          if (datos.ok) {
            // Redirige al panel de admin
            window.location.href = "loginSection/menuLogin.html";
          } else {
            alert(datos.mensaje);
          }
        })
        .catch((error) => console.error("Error en login:", error));
    });
  }

  // ==========================================
  //                SECTION ADMINISTRADOR
  // ==========================================

  //==================================
  //      1.- menuLogin.html LOGICA
  //==================================

  //=======================================================
  //navegación a Buscar Usuarios (buscarUsuariosAdmin.html)
  //=======================================================

  // Navegación a Buscar Usuarios
  const btnBuscar = document.getElementById("button-buscarUsuario");
  if (btnBuscar) {
    btnBuscar.onclick = function () {
      window.location.href = "buscarUsuariosAdmin.html";
    };
  }

  // Navegación Libros Vencidos (Ojo: sin la "s" extra para que coincida con tu HTML)
  const btnVencidos = document.getElementById("button-libroVencidos");
  if (btnVencidos) {
    btnVencidos.onclick = function () {
      window.location.href = "librosVencidosAdmin.html";
    };
  }

  // Navegación Libros Activos
  const btnActivos = document.getElementById("button-libroActivos");
  if (btnActivos) {
    btnActivos.onclick = function () {
      window.location.href = "librosActivosAdmin.html";
    };
  }

  // Navegación Multas (Cambiado a getElementById y cerrada la llave)
  const btnMultas = document.getElementById("button-multasAdmin");
  if (btnMultas) {
    btnMultas.onclick = function () {
      window.location.href = "multasAdmin.html";
    };
  }

  // =============================================
  // LÓGICA PARA buscarUsuariosAdmin.html
  // =============================================

  const listaUsuarios = document.getElementById("lista-usuarios-UsuariosAdm");
  const templateUsuario = document.getElementById("template-usuario");

  if (listaUsuarios && templateUsuario) {
    fetch("http://127.0.0.1:5000/api/usuarios")
      .then((respuesta) => respuesta.json())
      .then((usuarios) => {
        usuarios.forEach((usuario) => {
          const fragmento = templateUsuario.content.cloneNode(true);

          fragmento.querySelector(".nombre-usuario-admin").textContent =
            usuario.nombre;
          fragmento.querySelector(".id-usuario-admin").textContent =
            `     ID:      ${usuario.id}`;

          //Llena los libros prestados de cada usuario
          const lista = fragmento.querySelector(".lista-libros-prestados");
          usuario.librosPrestados.forEach((prestamo) => {
            const li = document.createElement("li");
            li.textContent = `📕 ${prestamo.libro} - 📜 VENCE: ${prestamo.fecha_vencimiento}`;
            lista.appendChild(li);
          });

          listaUsuarios.appendChild(fragmento);
        });
      })

      .catch((error) => console.error("Error al obtener usuarios:", error));
  }

  //========================================================
  // LÓGICA PARA librosVencidosAdmin.html
  //=======================================================

  const listaVencidos = document.getElementById(
    "menu-administracion-librosVencidos",
  );
  const templateVencidos = document.getElementById("template-libros-vencidos");

  if (listaVencidos && templateVencidos) {
    fetch("http://127.0.0.1:5000/api/usuarios/vencidos")
      .then((respuesta) => respuesta.json())
      .then((vencidos) => {
        vencidos.forEach((prestamo) => {
          const fragmento = templateVencidos.content.cloneNode(true);

          fragmento.querySelector(".nombre-Usuario-adminUsuario").textContent =
            `🙍‍♂ Usuario: ${prestamo.nombre}`;
          fragmento.querySelector(
            ".libroVencido-Usuario-adminUsuario",
          ).textContent = `📖 Libro:  ${prestamo.libro}`;
          fragmento.querySelector(
            ".fechaVencido-Usuario-adminUsuario",
          ).textContent = `📅 Vencido: 2026-04-01`;

          listaVencidos.appendChild(fragmento);
        });
      })
      .catch((error) => console.error("Error al obtener vencidos:", error));
  }

  // ========================================
  // LÓGICA PARA librosActivosAdmin.html
  // ========================================

  const listaActivos = document.getElementById(
    "menu-administracion-librosActivos",
  );
  const templateActivos = document.getElementById("template-libros-activos");

  if (listaActivos && templateActivos) {
    fetch("http://127.0.0.1:5000/api/usuarios/activos")
      .then((respuesta) => respuesta.json())
      .then((activos) => {
        activos.forEach((prestamo) => {
          const fragmento = templateActivos.content.cloneNode(true);

          fragmento.querySelector(".nombre-Usuario-adminUsuario").textContent =
            `🙍‍♂️ Usuario: ${prestamo.nombre}`;
          fragmento.querySelector(
            ".libroActivos-Usuario-adminUsuario",
          ).textContent = `📖 Libro: ${prestamo.libro}`;
          fragmento.querySelector(
            ".fechaProxVencer-Usuario-adminUsuario",
          ).textContent = `📅 Vence: ${prestamo.fecha_vencimiento}`;

          listaActivos.appendChild(fragmento);
        });
      })
      .catch((error) => console.error("Error al obtener activos:", error));
  }

  //==============================================
  // LÓGICA PARA multasAdmin.html
  //==============================================

  const listaMultas = document.getElementById("menu-administracion-multas");
  const templateMultas = document.getElementById("template-multas");

  if (listaMultas && templateMultas) {
    fetch("http://127.0.0.1:5000/api/usuarios/multas")
      .then((respuesta) => respuesta.json())
      .then((multas) => {
        multas.forEach((usuario) => {
          const fragmento = templateMultas.content.cloneNode(true);

          fragmento.querySelector(".nombre-Usuario-multa").textContent =
            `🙍‍♂️ Usuario: ${usuario.nombre}`;
          fragmento.querySelector(".total-multa-Usuario").textContent =
            `💰 Multa total: $${usuario.multa_total}`;

          listaMultas.appendChild(fragmento);
        });
      })
      .catch((error) => console.error("Error al obtener multas:", error));
  }
});
