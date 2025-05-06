const canvas = document.getElementById('rouletteCanvas');
const ctx = canvas.getContext('2d');

const wheelRadius = 200;
const ballRadius = 10;
let angle = 0;
let speed = 0;
let ballAngle = 0;
let ballSpeed = 0;
let isSpinning = false;

function drawWheel() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate(angle);

    // Draw the wheel segments
    for (let i = 0; i < 36; i++) {
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.arc(0, 0, wheelRadius, (i * Math.PI) / 18, ((i + 1) * Math.PI) / 18);
        ctx.fillStyle = i % 2 === 0 ? '#FF0000' : '#000000';
        ctx.fill();
        ctx.stroke();
    }

    ctx.restore();
}

function drawBall() {
    ctx.save();
    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate(ballAngle);
    ctx.beginPath();
    ctx.arc(0, -wheelRadius + ballRadius, ballRadius, 0, Math.PI * 2);
    ctx.fillStyle = '#FFFFFF';
    ctx.fill();
    ctx.restore();
}

function update() {
    if (isSpinning) {
        angle += speed;
        ballAngle += ballSpeed;

        // Simulate friction
        speed *= 0.99;
        ballSpeed *= 0.99;

        // Stop spinning when speed is low
        if (Math.abs(speed) < 0.01) {
            isSpinning = false;
            speed = 0;
            ballSpeed = 0;
        }
    }

    drawWheel();
    drawBall();
    requestAnimationFrame(update);
}

function startSpin() {
    if (!isSpinning) {
        speed = Math.random() * 0.1 + 0.1; // Random initial speed
        ballSpeed = Math.random() * 0.05 + 0.05; // Random ball speed
        isSpinning = true;
    }
}

canvas.width = 400;
canvas.height = 400;
canvas.addEventListener('click', startSpin);
update();
