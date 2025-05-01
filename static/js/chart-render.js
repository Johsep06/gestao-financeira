// ente1 = [
//     {value: "{{ Ag1Vit }}", category: "Vitórias"}, 
//     {value: "{{ ag1Qtd - Ag1Vit }}", category: "Derrotas"}
// ];
// dataAgente2 = [
//     {value: "{{ Ag2Vit }}", category: "Vitórias"}, 
//     {value: "{{ ag2Qtd - Ag2Vit }}", category: "Derrotas"}
// ];

dados = [
    { value: "23.3", category: "Receitas" },
    { value: "52.2", category: "tiro" },
    { value: "11.2", category: "porrada" },
    { value: "12.2", category: "bomba" },
];

async function pegarDadosGraficos(route) {
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

function getCurrentYearMonth() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // +1 porque janeiro é 0
    return `${year}-${month}`;
}

async function loadPieChart() {
    data = getCurrentYearMonth();
    rotaDespesas = `/data/percental/despesas/${data}`;
    const percentualDespesasPorMes = await pegarDadosGraficos(rotaDespesas);

    am5.ready(createChart("percentual-despesas", percentualDespesasPorMes));
}
async function loadPieChart2() {
    data = getCurrentYearMonth();
    rotaReceitas = `/data/percental/receitas/${data}`;
    const percentualReceitasPorMes = await pegarDadosGraficos(rotaReceitas);

    am5.ready(createChart("percentual-receitas", percentualReceitasPorMes));
}