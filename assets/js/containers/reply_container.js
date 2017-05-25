import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

import { fetchTweet } from '../actions';


class ReplyContainer extends React.Component {

  componentDidMount() {
    this.props.fetchTweet(this.props.match.params.tweet_id);
  }

  renderTweet() {
    const tweet = this.props.tweet;

    return (
      <div className="row">
        <div className="col-sm-12">
          <div className="tweet-box">
            <p>@{tweet.username} - {tweet.created_at}</p>
            <p>{tweet.text}</p>
          </div>
        </div>
      </div>
    );
  }

  render() {
    return (
      <div>
        <div className="row">
          <div className="col-sm-6">
            <h3>Reply</h3>
          </div>

          <div className="col-sm-6">
            <Link className="btn btn-default pull-right" to="/">
              Back
            </Link>
          </div>
        </div>

        {this.renderTweet()}
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    tweet: state.tweet,
  };
}

export default connect(mapStateToProps, { fetchTweet })(ReplyContainer);
