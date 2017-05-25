import _ from 'lodash';
import { connect } from 'react-redux';
import React from 'react';

import { fetchTweets } from '../actions';


class TweetsContainer extends React.Component {

  componentDidMount() {
    this.props.fetchTweets();
  }

  renderTweets() {
    return _.map(this.props.tweets, (tweet) => {
      return (
        <tr key={tweet.id}>
          <td>{tweet.user}</td>
          <td>{tweet.created_at}</td>
          <td>{tweet.text}</td>
        </tr>
      );
    });
  }

  render() {
    return (
      <div>
        <h3>Tweets</h3>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>User</th>
              <th>Date</th>
              <th>Text</th>
            </tr>
          </thead>
          <tbody>
            {this.renderTweets()}
          </tbody>
        </table>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { tweets: state.tweets };
}

export default connect(mapStateToProps, { fetchTweets })(TweetsContainer);
