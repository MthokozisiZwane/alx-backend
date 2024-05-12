import kue from 'kue';

// Creates a queue with Kue
const queue = kue.createQueue();

// Array containing blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs from the queue
queue.process('push_notification_code_2', 2, async (job, done) => {
    const { phoneNumber, message } = job.data;

    // Tracks progress of the job
    job.progress(0, 100);

    // Checks if phone number is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
        // Fail the job if the phone number is blacklisted
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Simulates sending notification
    setTimeout(() => {
        // Tracks progress to 50%
        job.progress(50, 100);

        // Sends notification
        sendNotification(phoneNumber, message);

        done();
    }, 1000);
});

console.log('Job processor is running...');
