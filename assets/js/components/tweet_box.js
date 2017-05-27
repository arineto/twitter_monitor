import React from 'react';


// eslint-disable-next-line react/prefer-stateless-function
class TweetBox extends React.Component {

  render() {
    const tweet = this.props.tweet;

    return (
      <div className="row">
        <div className="col-sm-12">
          <div className="tweet-box">
            <p>@{tweet.username} - {tweet.date ? tweet.date : tweet.created_at}</p>
            <p>{tweet.text}</p>
          </div>
        </div>
      </div>
    );
  }
}

export default TweetBox;
