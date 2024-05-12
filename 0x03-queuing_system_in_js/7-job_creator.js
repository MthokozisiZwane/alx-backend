import kue from 'kue';

const queue = kue.createQueue();

// Array of jobs data
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Function to create jobs and add them to the queue
const createJobs = (jobs) => {
    jobs.forEach((jobData, index) => {
        const job = queue.create('push_notification_code_2', jobData)
            .save((err) => {
                if (err) {
                    console.error(`Failed to create job ${index + 1}: ${err}`);
                } else {
                    console.log(`Notification job created: ${job.id}`);
                }
            });

        // Event listener for job completion
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });

        // Event listener for job failure
        job.on('failed', (err) => {
            console.error(`Notification job ${job.id} failed: ${err}`);
        });

        // Event listener for job progress
        job.on('progress', (progress) => {
            console.log(`Notification job #${job.id} ${progress}% complete`);
        });
    });
};

// Calls the function to create jobs
createJobs(jobs);
