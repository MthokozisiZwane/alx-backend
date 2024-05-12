import redis from 'redis';

// Connect to Redis server
const client = redis.createClient();

// Display a message upon successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Function to store a hash value
function createHash() {
  client.hset(
    'HolbertonSchools',
    'Portland',
    50,
    'Seattle',
    80,
    'New York',
    20,
    'Bogota',
    20,
    'Cali',
    40,
    'Paris',
    2,
    (err, reply) => {
      if (!err) {
        console.log(reply);
      }
    }
  );
}

// Function to display the hash values
function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (!err) {
      console.log(reply);
    }
  });
}

createHash();
displayHash();
