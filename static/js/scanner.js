const resultado = document.getElementById("resultado")
const scanner = new Html5QrcodeScanner(
    "reader",
    {
        fps: 10,
        qrbox: 250
    }
);

scanner.render(
    (texto) => {
        resultado.textContent = texto;
    },
    (erro) => {
        // Ignora os erros enquanto procura um QR Code
    }
);