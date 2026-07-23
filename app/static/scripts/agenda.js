const table = new Tabulator("#agenda-table", {
    data: agendamentos,
    layout: "fitColumns",
    placeholder: "Nenhum agendamento disponível",
    columns: [
        { title: "Paciente", field: "paciente" },
        { title: "CPF", field: "cpf" },
        { title: "Médico", field: "medico" },
        { title: "Especialidade", field: "especialidade" },
        { title: "Data", field: "data" },
        { title: "Horário", field: "horario" },
        { title: "Convênio", field: "convenio" },
        { title: "Status", field: "status" },
    ],
});

const busca = document.getElementById("busca");

busca.addEventListener("input", function () {
    const texto = busca.value.toLowerCase().trim();

    if (texto === "") {
        table.clearFilter();
        return;
    }

    table.setFilter(function (data) {
        return (
            data.paciente.toLowerCase().includes(texto) ||
            data.cpf.toLowerCase().includes(texto) ||
            data.medico.toLowerCase().includes(texto)
        );
    });
});