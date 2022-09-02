const rwClient = require("./twitterClient.js")

const tweet = async () => {
    try {
        await rwClient.v1.tweet("Hello, World!")
    } catch (e) {
        console.error(e)
    }
}

tweet()
