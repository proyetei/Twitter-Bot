const rwClient = require("./twitterClient.js");
const CronJob = require("cron").CronJob;
//runs a promise
const tweet = async () => {
    try{
        //tweet message
        await rwClient.v1.tweet(status: "Movie information")
    }
    catch(e){
        console.error(e)
    }
}

//the time that this bot is going to post
const job = new CronJob("0 5 * * *", () => {
    tweet()
})

job.start();