let colors = [];
colors["Red"] = "#FF0000";

let filteredColors = [];
Object.keys(colors).forEach((colorName) => {
  if (true) {
    filteredColors[colorName] = colors[colorName];
  }
});

for (const [key, value] of Object.entries(filteredColors)) {
  console.log(key, value);
}

console.log(colors.colorName);
