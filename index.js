const rwClient = require("./twitterClient.js");

const tweet = async () => {
    try{
        await rwClient.v1.tweet(status: "")
    }
    catch(e){
        console.error(e)
    }
}

