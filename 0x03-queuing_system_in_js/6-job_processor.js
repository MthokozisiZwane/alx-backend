import kue from 'kue';

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
const sendNotification = async (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs
queue.process('push_notification_code_2', 2, async (job, done) => {
    const { phoneNumber, message } = job.data;

    // Check if phone number is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
        // Fail the job if the phone number is blacklisted
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    } else {
        // Track the progress of the job
        job.progress(0, 100);

        // Simulate sending notification
        await sendNotification(phoneNumber, message);

        // Update job progress
        job.progress(50, 100);

        // Mark the job as completed
        done();
    }
});

console.log('Job processor is running...');
