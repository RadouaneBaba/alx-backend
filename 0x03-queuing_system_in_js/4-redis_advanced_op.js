import { createClient, print } from 'redis';
import { promisify } from 'util';
const client = createClient();

const schools = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

for (const [key, value] of Object.entries(schools)) {
  client.hset('HolbertonSchools', key, value, print);
}
client.hgetall('HolbertonSchools', (err, reply) => {
  if (!err) console.log(reply);
});
