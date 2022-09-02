const rwClient = require("./twitterClient.js")

const tweet = async () => {
    try {
        await rwClient.v2.tweet("fuck mohsin hes dumb!")
    } catch (e) {
        console.error(e)
    }
}

tweet()
