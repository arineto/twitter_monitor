import _ from 'lodash';
import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

import { fetchTweets } from '../actions';


class TweetsContainer extends React.Component {

  componentDidMount() {
    this.props.fetchTweets();
  }

  renderTweets() {
    return _.map(this.props.tweets, (tweet) => {
      return (
        <tr key={tweet.id}>
          <td>{tweet.username}</td>
          <td>{tweet.created_at}</td>
          <td>{tweet.text}</td>
        </tr>
      );
    });
  }

  render() {
    return (
      <div>
        <div className="row">
          <div className="col-sm-6">
            <h3>Tweets</h3>
          </div>

          <div className="col-sm-6">
            <Link className="btn btn-primary pull-right" to="/users/">
              Add an User
            </Link>
          </div>
        </div>

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
