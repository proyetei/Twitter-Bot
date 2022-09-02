const rwClient = require("./twitterClient.js")

const tweet = async () => {
    try {
        await rwClient.v2.tweet("Hello, World!")
    } catch (e) {
        console.error(e)
    }
}

tweet()
