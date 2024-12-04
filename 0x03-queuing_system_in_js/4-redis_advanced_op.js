import { createClient, print } from "redis";

const client  = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

function setData(hashName, fieldNames, data) {
  client.hset(hashName, fieldNames, data, print)
}
const data = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogata: 20,
  cali: 40,
  Paris: 2,
};

for (const [keys, values] of  Object.entries(data)) {
  setData('HolbertonSchools', keys, values);
}

client.hgetall('HolbertonSchools', (err, datas) => {
  if (err) {
    console.error(err);
  }
  console.log(datas);
})

client.on("connect", () => {
  console.log("Redis client connected to the server");
});
