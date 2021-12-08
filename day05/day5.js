const { readFileSync } = require("fs");

const buildVents = (data, blockDiag = true) => {
  vents = {};
  data.forEach(([a, b, x, y]) => {
    if (blockDiag && a != x && b != y) return;
    let i = a,
      j = b;
    const xDir = Math.sign(x - a);
    const yDir = Math.sign(y - b);
    while (i != x || j != y) {
      const k = `${i},${j}`;
      if (!(k in vents)) vents[k] = 0;
      vents[k]++;
      i += xDir;
      j += yDir;
    }
    const k = `${i},${j}`;
    if (!(k in vents)) vents[k] = 0;
    vents[k]++;
  });
  let hot = 0;
  for (const [_, laps] of Object.entries(vents)) {
    if (laps > 1) hot++;
  }
  return hot;
};

const part1 = (data) => {
  return buildVents(data);
};
const part2 = (data) => {
  return buildVents(data, (blockDiag = false));
};

const input = readFileSync("./input.txt", "utf-8");
const data = [...input.matchAll(/(\d+),(\d+) -> (\d+),(\d+)/g, input)].map(
  (match) => match.splice(1, 5).map((i) => parseInt(i))
);

console.log(`Part 1: ${part1(data)}`);
console.log(`Part 2: ${part2(data)}`);
