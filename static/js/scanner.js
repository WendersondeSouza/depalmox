const resultado = document.getElementById("resultado")
const scanner = new Html5QrcodeScanner(
    "reader",
    {
        fps: 10,
        qrbox: 250
    }
);
const beep_sound = new Audio("/static/sounds/beep.mp3");
const error_sound = new Audio("/static/sounds/error.mp3")
let podeLer = true;


scanner.render(
    (texto) => {
        if (!podeLer) {
            return;
        }

        podeLer = false;

        resultado.textContent = texto;

        beep_sound.currentTime = 0;
        beep_sound.play();

        fetch("/scanner/read", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                ref: texto
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "ok") {
                beep_sound.play();
            } else {
                error_sound.play();
                resultado.textContent = data.mensagem;
            }
        });

        setTimeout(() => {
            podeLer = true
        }, 1300);
    },
    (erro) => {}
);