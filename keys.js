var webpush = require('web-push');

console.log('tetsas')

const vapidKeys = webpush.generateVAPIDKeys();

// Prints 2 URL Safe Base64 Encoded Strings
console.log(vapidKeys.publicKey, '....',vapidKeys.privateKey);

webpush.setGCMAPIKey('AIzaSyAoeCJw9ev688quiD5x_DM49-CKOxnFp-Y');

// console.log('gcm',xxx)

// BNZJv3zP9ZOKnr1Ptgr139rFuyfkLa3BlsOpBd_vUYBRoYSkwHL_J7n1AU0FhcyzE0ZEaZVdial5xGcjYGr7aXo .... y9Uf1lwecS_gGsBGNDd75BgEeIr1MYzO8-oiWYzGB6Y
