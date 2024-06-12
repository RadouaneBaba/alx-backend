import { createClient, print } from 'redis';
import { promisify } from 'util'

const client = createClient()
	.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
	.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync(schoolName);
  console.log(value);
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
