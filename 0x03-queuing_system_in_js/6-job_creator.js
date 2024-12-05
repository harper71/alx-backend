import { createQueue } from "kue";

const Queue = createQueue();

const data = {
  phoneNumber: '08130718156',
  message: 'Registered',
};

const job = Queue.create('push_notification_code', data);

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', (errorMessage) => {
    console.log(`Notification job failed: ${errorMessage}`);
  });

job.save((err) => {
  if (err) {
    console.error('Failed to save job:', err);
  }
});
