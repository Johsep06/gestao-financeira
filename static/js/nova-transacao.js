const inputCategoria = document.querySelector('#categoria');
const inputValor = document.querySelector('#valor');
const inputDescricao = document.querySelector('#descricao');
const inputData = document.querySelector('#data');
const inputTipo = document.querySelector('#tipo');
const btnSalvar = document.querySelector('#btn-salvar');
const formularioNovaTransacao = document.querySelector('#form-nova-transacao');

function avaliarCampoValor(string) {
    const valorPattern = /^\d{1,3}(?:,\d{3})*(?:\.\d\d?)?$/;
    return valorPattern.test(string.trim());
}

formularioNovaTransacao.addEventListener('submit', (event) => {
    event.preventDefault();

    const tipoTransacao = document.querySelector('input[name="tipo"]:checked').value;
    transacao = {
        'categoria': inputCategoria.value,
        'descricao': inputDescricao.value,
        'data': inputData.value,
        'tipo': parseInt(tipoTransacao),
    };
    let resultado = avaliarCampoValor(inputValor.value);
    if (resultado) {
        let valor = inputValor.value.replace(',', '');
        while (valor.includes(',')) {
            valor = valor.replace(',', '');
        }
        transacao['valor'] = parseFloat(valor);
    } else {
        alert('O campo valor deve ser preenchido com um número válido.');
        return;
    }
    
    const resposta = fetch('/forms/nova-transacao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(transacao)
    })

    .then(response => {
        if (response.ok) {
            inputCategoria.value = '';
            inputValor.value = '';
            inputDescricao.value = '';
            inputData.value = '';
            return response.json();
        } else {
            throw new Error('Erro ao salvar a transação.');
        }
    })
});