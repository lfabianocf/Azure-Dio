const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let marioImage = new Image();
marioImage.src = 'path/to/mario-image.png'; // Update this path to the correct location of the Mario image

const gravity = 0.25;
const jumpStrength = 4.5;
let mario = {
    x: 50,
    y: canvas.height / 2,
    width: 34, // Adjust based on the Mario image size
    height: 34, // Adjust based on the Mario image size
    velocity: 0,
    jump: function() {
        this.velocity = -jumpStrength;
    },
    update: function() {
        this.velocity += gravity;
        this.y += this.velocity;

        // Prevent Mario from falling off the canvas
        if (this.y + this.height >= canvas.height) {
            this.y = canvas.height - this.height;
            this.velocity = 0;
        }
        if (this.y < 0) {
            this.y = 0;
            this.velocity = 0;
        }
    },
    render: function() {
        ctx.drawImage(marioImage, this.x, this.y, this.width, this.height);
    }
};

function render() {
    if (marioImage.complete) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        mario.update();
        mario.render();
    } else {
        console.error("Mario image not loaded yet.");
    }
}

function gameLoop() {
    render();
    requestAnimationFrame(gameLoop);
}

document.addEventListener('keydown', function(event) {
    if (event.code === 'Space') {
        mario.jump();
    }
});

marioImage.onload = function() {
    gameLoop();
};