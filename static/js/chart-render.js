// ente1 = [
//     {value: "{{ Ag1Vit }}", category: "Vitórias"}, 
//     {value: "{{ ag1Qtd - Ag1Vit }}", category: "Derrotas"}
// ];
// dataAgente2 = [
//     {value: "{{ Ag2Vit }}", category: "Vitórias"}, 
//     {value: "{{ ag2Qtd - Ag2Vit }}", category: "Derrotas"}
// ];

// am5.ready(createChart("chartdiv", dataAgente1));
// am5.ready(createChart("chartdiv2", dataAgente2));

dados = [
    { value: "23.3", category: "Receitas" },
    { value: "52.2", category: "tiro" },
    { value: "11.2", category: "porrada" },
    { value: "12.2", category: "bomba" },
];

async function carregarPercentualDespesas(route) {
    try {
        const response = await fetch(route);
        const dados = await response.json();
        
        // Transforma os dados para o formato que amCharts espera
        return Object.entries(dados).map(([categoria, percentual]) => ({
            category: categoria,
            value: percentual
        }));
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
        return [];
    }
}
// setInterval(carregarPercentualDespesas, 200)
// setTimeout(carregarPercentualDespesas, 200)