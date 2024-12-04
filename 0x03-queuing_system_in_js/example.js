const data = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogata: 20,
  cali: 40,
  Paris: 2,
};

for (const [keys, values] of Object.entries(data)) {
  console.log(keys, values);
}