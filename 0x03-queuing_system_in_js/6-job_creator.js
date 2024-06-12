import kue from 'kue';

const data = {
  phoneNumber: '0766649099',
  message: 'my phonenumber',
};

const queue = kue.createQueue();

const job = queue.create('push_notification_code', JSON.stringify(data));

job.save((err) => {
  if (err) {
    console.log('Notification job failed');
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => console.log('Notification job completed'));
