const html = document.querySelector('html');
const checkboxDarkMode = document.querySelector('#dark-mode');

checkboxDarkMode.checked = false;

checkboxDarkMode.addEventListener('change', () => {
    html.classList.toggle('dark-mode')
})

function render_container(route, containerID) {
    fetch(route)
        .then(response => {
            if (!response.ok) {
                alert('Erro ao carregar os controles')
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text(); // Retorna a resposta como texto
        })
        .then(data => {
            document.getElementById(containerID).innerHTML = ''; // Limpa o container
            document.getElementById(containerID).innerHTML = data; // Insere o HTML retornado no container
        })
        .catch(error => {
            console.error('Erro ao carregar conteúdo:', error);
        });
}

render_container('/controls', 'controls')

// dataAgente1 = [
//     {value: "{{ Ag1Vit }}", category: "Vitórias"}, 
//     {value: "{{ ag1Qtd - Ag1Vit }}", category: "Derrotas"}
// ];
// dataAgente2 = [
//     {value: "{{ Ag2Vit }}", category: "Vitórias"}, 
//     {value: "{{ ag2Qtd - Ag2Vit }}", category: "Derrotas"}
// ];

// am5.ready(createChart("chartdiv", dataAgente1));
// am5.ready(createChart("chartdiv2", dataAgente2));