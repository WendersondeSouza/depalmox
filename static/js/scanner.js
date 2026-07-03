const resultado = document.getElementById("resultado")
const scanner = new Html5QrcodeScanner(
    "reader",
    {
        fps: 10,
        qrbox: 250
    }
);
let podeLer = true;


scanner.render(
    (texto) => {
        if (!podeLer) {
            return;
        }

        podeLer = false;

        resultado.textContent = texto;

        fetch("/scanner/read", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                ref: texto
            })
        });

        setTimeout(() => {
            podeLer = true
        }, 800);
    },
    (erro) => {}
);