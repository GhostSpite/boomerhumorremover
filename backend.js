var tweet = {
    name:"username",
    text:"Some other tweet text"
};

function start(username){
    var name = username;
    //Run name through twitter api

    //Run return contents through watson

    //Parse contents into one object

    var response = {
        name:username,
        tweet:"some string",
        analysis:"Okay, boomer",
        similar:[]
    };

    //Search twitter for similar tweets
    var simTweets = [];

    //Parse similar tweet data
    simTweets.forEach(function add(item) 
    {
        //From item.name
        tweet.name = "@OldGuy1922";
        //From item.text
        tweet.text = "I just get back from my colonoscopy #crappytime"
        response.similar.push(tweet)
    });

    //Get interest analysis from watson
    var interests = ["old people", "old stuff", "dinosaurs"];
}
