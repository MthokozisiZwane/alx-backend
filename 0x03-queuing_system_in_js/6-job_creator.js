import kue from 'kue';

const queue = kue.createQueue();

// Create a job with Kue
function createJob() {
  const job = queue.create('push_notification_code', {
    phoneNumber: '1234567890',
    message: 'This is a notification message',
  });

  job.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  job.on('complete', () => {
    console.log(`Notification job completed`);
  });

  job.on('failed', () => {
    console.log(`Notification job failed`);
  });
}

createJob();
