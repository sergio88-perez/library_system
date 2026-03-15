document.getElementById("form-libro").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const res = await fetch("/libros", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
    e.target.reset();
});

document.getElementById("form-usuario").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const res = await fetch("/usuarios", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
    e.target.reset();
});

document.getElementById("form-prestamo").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const res = await fetch("/prestamos", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
    e.target.reset();
});

document.getElementById("form-devolucion").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    formData.append('codigo_libro', document.getElementById('codigo_libro').value);

    const res = await fetch("/devoluciones", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
    e.target.reset();
});

async function cargarLibros() {
    const res = await fetch("/libros");
    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
}

async function cargarUsuarios() {
    const res = await fetch("/usuarios");
    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
}

async function cargarPrestamos() {
    const res = await fetch("/prestamos");
    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
}