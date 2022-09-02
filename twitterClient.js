const {TwitterApi} = require("twitter-api-v2")
const tokens = require("./twitterKeys.json")
console.log(tokens)


// Instantiate with desired auth type (here's Bearer v2 auth)
const twitterClient = new TwitterApi({
    appKey: tokens.keys.API_Key,
    appSecret: tokens.keys.API_Key_Secret,
    accessToken: tokens.keys.Access_Token,
    accessSecret: tokens.keys.Access_Token_Secret
});

// Tell typescript it's a read and write app
const rwClient = twitterClient.readWrite;

module.exports = rwClient