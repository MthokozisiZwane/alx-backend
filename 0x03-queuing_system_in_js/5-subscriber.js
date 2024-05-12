import redis from 'redis';

// Creates a Redis client for subscribing
const subscriber = redis.createClient();

// Subscribes to the channel
subscriber.on('subscribe', (channel, count) => {
  console.log(`Subscribed to ${channel}`);
});

// Handles incoming messages
subscriber.on('message', (channel, message) => {
  console.log(`Received message from channel ${channel}: ${message}`);
});

// Logs errors
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Connects to Redis server
subscriber.subscribe('holberton school channel');
