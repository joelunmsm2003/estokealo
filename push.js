var webpush = require('web-push');


endpoint=process.argv[2]
auth =process.argv[3]
p256dh=process.argv[4]
body=process.argv[5]
title=process.argv[6]
photo=process.argv[7]
photo_user=process.argv[8]

webpush.setGCMAPIKey('AIzaSyAoeCJw9ev688quiD5x_DM49-CKOxnFp-Y');

const pushSubscription ={"endpoint":endpoint,"keys":{"p256dh":p256dh,"auth":auth}}
const payload = body +'-/-'+title+'-/-'+photo+'-/-'+photo_user;

const options = {
  vapidDetails: {
    subject: 'mailto:joelunmsm@gmail.com',
    publicKey: 'BMyctZxzhZjzioDQckl5DWiKfZQA3DJO12B3rs7SHFcLHK_O92wQptOOfy-4igA5R1dCGcC-23noGougMEDsuY0',
    privateKey: '-kjMEQOG7sy2AcCM1XMBQ29ipQaD7d6q9K_vYJOQBJ0'
  }
}


webpush.sendNotification(
  pushSubscription,
  payload,
  options
);



