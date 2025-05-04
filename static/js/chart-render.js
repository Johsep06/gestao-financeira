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

async function pegarDadosGraficos(route, formato) {
    try {
        const response = await fetch(route);
        const dados = await response.json();

        if (formato === "pie-chart") {
            // Transforma os dados para o formato que amCharts espera
            return Object.entries(dados).map(([categoria, percentual]) => ({
                category: categoria,
                value: percentual
            }));
        }

        else if (formato === "line-chart") {
            // Transforme seus dados da API para o formato esperado
            return Object.entries(dados).map(([date, value]) => ({
                date: new Date(date).getTime(), // Converte string de data para timestamp
                value: value
            }));
        }
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

async function loadPercentualDespesasMes() {
    data = getCurrentYearMonth();
    rotaDespesas = `/data/percental/despesas/${data}`;
    const percentualDespesasPorMes = await pegarDadosGraficos(rotaDespesas, "pie-chart");

    am5.ready(createChart("percentual-despesas", percentualDespesasPorMes));
}
async function loadPercentualReceitasMes() {
    data = getCurrentYearMonth();
    rotaReceitas = `/data/percental/receitas/${data}`;
    const percentualReceitasPorMes = await pegarDadosGraficos(rotaReceitas, "pie-chart");

    am5.ready(createChart("percentual-receitas", percentualReceitasPorMes));
}

async function loadHistoricoReceitasMes() {
    data = '2025-04'//getCurrentYearMonth();
    rotaHistoricoReceitas = `/data/historico/receitas/${data}`;
    const historicoReceitasPorMes = await pegarDadosGraficos(rotaHistoricoReceitas, "line-chart");

    am5.ready(lineChart("historico-receitas-mes", historicoReceitasPorMes));
}
async function loadHistoricoDespesasMes() {
    data = "2025-04" //getCurrentYearMonth();
    rotaHistoricoDespesas = `/data/historico/despesas/${data}`;
    const historicoDespesasPorMes = await pegarDadosGraficos(rotaHistoricoDespesas, "line-chart");

    // const historicoDespesasPorMes = [
    //     { date: new Date(2024, 3, 2).getTime(), value: 100 },
    //     { date: new Date(2024, 3, 3).getTime(), value: 120 },
    //     { date: new Date(2024, 3, 10).getTime(), value: 150 },
    //     { date: new Date(2024, 3, 12).getTime(), value: 100 },
    //     { date: new Date(2024, 3, 17).getTime(), value: 200 },
    // ]
    am5.ready(lineChart("historico-despesas-mes", historicoDespesasPorMes));
}