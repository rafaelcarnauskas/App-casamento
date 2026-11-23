
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Uma perguntinha ❤️",
    page_icon="❤️",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        background: #fff0f3;
        font-family: 'Georgia', serif;
        overflow: hidden;
    }

    .container {
        height: 95vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .heart {
        position: relative;
        width: 230px;
        height: 210px;
        margin-bottom: 45px;
        animation: pulse 1.5s infinite;
    }

    .heart::before,
    .heart::after {
        content: "";
        position: absolute;
        width: 115px;
        height: 180px;
        background: #e63965;
        border-radius: 115px 115px 0 0;
    }

    .heart::before {
        left: 115px;
        transform: rotate(-45deg);
        transform-origin: 0 100%;
    }

    .heart::after {
        left: 0;
        transform: rotate(45deg);
        transform-origin: 100% 100%;
    }

    .ribbon {
        position: absolute;
        z-index: 2;
        top: 85px;
        left: -30px;
        width: 290px;
        padding: 13px 0;
        background: #ffcf70;
        color: #8b1e3f;
        font-family: Arial, sans-serif;
        font-size: 22px;
        font-weight: bold;
        letter-spacing: 2px;
        box-shadow: 0 3px 8px #8b1e3f55;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.06); }
    }

    h2 {
        color: #9d174d;
        font-size: 25px;
        margin-bottom: 25px;
    }

    .buttons {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;
        min-height: 100px;
        width: 100%;
    }

    button {
        border: none;
        border-radius: 30px;
        padding: 14px 32px;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.25s ease;
    }

    #yes {
        background: #e63965;
        color: white;
        box-shadow: 0 4px 12px #e6396560;
        z-index: 5;
    }

    #no {
        background: #eeeeee;
        color: #555;
        position: relative;
        z-index: 10;
    }

    .invitation {
        display: none;
        animation: appear 1s ease;
        color: #9d174d;
    }

    .invitation h1 {
        font-size: 36px;
    }

    .invitation p {
        font-size: 22px;
        line-height: 1.7;
    }

    .invitation .emoji {
        font-size: 65px;
    }

    @keyframes appear {
        from { opacity: 0; transform: scale(0.7); }
        to { opacity: 1; transform: scale(1); }
    }
</style>
</head>

<body>

<div class="container" id="main">

    <div class="heart">
        <div class="ribbon">CASA COMIGO?</div>
    </div>

    <h2>Você aceita passar o resto da vida comigo?</h2>

    <div class="buttons">
        <button id="yes" onclick="accept()">SIM ❤️</button>
        <button id="no" onclick="runAway()">NÃO</button>
    </div>

</div>

<div class="container invitation" id="invitation">
    <div class="emoji">💍❤️</div>
    <h1>EU SABIA!!!</h1>
    <p>
        Então está oficialmente convidada<br>
        para o nosso casamento! 💒
    </p>
    <p>
        <strong>Sexta-feira</strong><br>
        🍣 Bar Grill e Sushi<br>
        🕗 Às 20h
    </p>
    <h2>Mal posso esperar! ❤️</h2>
</div>

<script>
    let scale = 1;

    function runAway() {
        const no = document.getElementById("no");
        const yes = document.getElementById("yes");

        scale += 0.25;

        // Aumenta o botão SIM
        yes.style.transform = `scale(${scale})`;

        // Faz o NÃO fugir pela tela
        no.style.position = "fixed";

        const maxX = window.innerWidth - no.offsetWidth - 20;
        const maxY = window.innerHeight - no.offsetHeight - 20;

        const x = Math.random() * maxX;
        const y = Math.random() * maxY;

        no.style.left = Math.max(10, x) + "px";
        no.style.top = Math.max(10, y) + "px";
    }

    function accept() {
        document.getElementById("main").style.display = "none";
        document.getElementById("invitation").style.display = "flex";
    }
</script>

</body>
</html>
"""

components.html(html, height=750, scrolling=False)
