
const canvas = document.getElementById("tetris");
const ctx = canvas.getContext("2d");
const startButton = document.getElementById("start");
const resetButton = document.getElementById("reset");
const modal = document.getElementById("myModal");
const instructionsButton = document.getElementById("instructions");
const span = document.getElementsByClassName("close")[0];

ctx.scale(20, 20);

startButton.addEventListener("click", () => {
  update();
  startButton.style.display = "none";
});

resetButton.addEventListener("click", () => {
  location.reload();
});

instructionsButton.addEventListener("click", () => {
  modal.style.display = "block";
});

span.addEventListener("click", () => {
  modal.style.display = "none";
});

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

const piece = [
  [0, 0, 0],
  [0, 1, 1],
  [1, 1, 0],
];

function createMatrix(w, h) {
  const matrix = [];
  while (h--) {
    matrix.push(new Array(w).fill(0));
  }
  return matrix;
}

const field = createMatrix(12, 20);
console.log(field);
console.table(field);

const player = {
  pos: { x: 5, y: -2 },
  piece: piece,
};

function drawPiece(piece, offset) {
  piece.forEach((row, y) => {
    row.forEach((value, x) => {
      if (value !== 0) {
        ctx.fillStyle = "blue";
        ctx.fillRect(x + offset.x, y + offset.y, 1, 1);
      }
    });
  });
}

function draw() {
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  drawPiece(field, { x: 0, y: 0 });
  drawPiece(player.piece, player.pos);
}


let dCounter = 0;
let dropInterval = 500;
let lastTime = 0;

function update(time = 0) {
  const deltaTime = time - lastTime;
  lastTime = time;
  dCounter += deltaTime;
  if (dCounter > dropInterval) {
    player.pos.y++;
    if (collide(field, player)) {
      player.pos.y--;
      join(field, player);
      player.pos.y = 0;
    }
    dCounter = 0;
  }

  draw();
  requestAnimationFrame(update);
}

function join(field, player) {
  player.piece.forEach((row, y) => {
    row.forEach((value, x) => {
      if (value !== 0) {
        field[y + player.pos.y][x + player.pos.x] = value;
      }
    });
  });
}

function collide(field, player) {
  const b = player.piece;
  const o = player.pos;
  for (let y = 0; y < b.length; y++) {
    for (let x = 0; x < b[y].length; x++) {
      if (b[y][x] !== 0 && (field[y + o.y] && field[y + o.y][x + o.x]) !== 0) {
        return true;
      }
    }
  }
  return false;
}

document.addEventListener("keydown", (e) => {
  if (e.keyCode === 37) {
    function playerMove(control) {
      player.pos.x += control;
      if (collide(field, player)) {
        player.pos.x -= control;
      }
    }
    playerMove(-1);
  } else if (e.keyCode === 39) {
    function playerMove(control) {
      player.pos.x += control;
      if (collide(field, player)) {
        player.pos.x -= control;
      }
    }
    playerMove(+1);
  } else if (e.keyCode === 40) {
    player.pos.y++;
    if (collide(field, player)) {
      player.pos.y--;
      join(field, player);
      player.pos.y = -2;
    }
    dCounter = 0;
  } else if (e.keyCode === 65) {
    const pos = player.pos.x;
    let offset = 1;
    function playerRotate(control) {
      rotate(player.piece, control);
    }
    playerRotate(-1);
    while (collide(field, player)) {
      player.pos.x += offset;
      offset = -(offset + (offset > 0 ? 1 : -1));
      if (offset > player.piece[0].length) {
        rotate(player.piece, control);
        player.pos.x = pos;
        return;
      }
    }
  } else if (e.keyCode === 68) {
    const pos = player.pos.x;
    let offset = 1;
    function playerRotate(control) {
      rotate(player.piece, control);
    }
    playerRotate(+1);
    while (collide(field, player)) {
      player.pos.x += offset;
      offset = -(offset + (offset > 0 ? 1 : -1));
      if (offset > player.piece[0].length) {
        rotate(player.piece, control);
        player.pos.x = pos;
        return;
      }
    }
  }
  console.log(field);
  console.table(field);
});

function rotate(piece, control) {
  for (let y = 0; y < piece.length; y++) {
    for (let x = 0; x < y; x++) {
      [piece[x][y], piece[y][x]] = [piece[y][x], piece[x][y]];
    }
  }
  if (control > 0) {
    piece.forEach((row) => row.reverse());
  } else {
    piece.reverse();
  }
}
