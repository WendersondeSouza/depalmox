const scanner = new Html5QrcodeScanner(
    "reader",
    {
        fps: 10,
        qrbox: 250
    }
);

scanner.render(
    (texto) => {
        console.log("QR Code:", texto);
    },
    (erro) => {
        // Ignora os erros enquanto procura um QR Code
    }
);