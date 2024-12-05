import { createQueue } from "kue";

const Queue = createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

Queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  try {
    sendNotification(phoneNumber, message);
    done()
  } catch (error) {
    done(new Error(`Failed to send notification: ${error.message}`));
  }
})