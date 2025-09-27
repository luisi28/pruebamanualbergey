async function buscar() {
  const query = document.getElementById("buscador").value.toLowerCase();
  const resp = await fetch("bal.json");
  const data = await resp.json();

  const encontrado = data.find(b => b.nombre.toLowerCase().includes(query));

  if (encontrado) {
    document.getElementById("resultado").innerHTML = `
      <h2>${encontrado.nombre}</h2>
      <p><b>Morfología:</b> ${encontrado.morfologia}</p>
      <p><b>Metabolismo:</b> ${encontrado.metabolismo}</p>
      <p><b>Hábitat:</b> ${encontrado.habitat}</p>
      <p><b>Importancia:</b> ${encontrado.importancia}</p>
      <img src="${encontrado.imagen}" alt="Imagen de ${encontrado.nombre}" width="250">
    `;
  } else {
    document.getElementById("resultado").innerHTML = "<p>No se encontró la bacteria.</p>";
  }
}
