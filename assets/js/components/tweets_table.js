import _ from 'lodash';
import React from 'react';
import { Link } from 'react-router-dom';


// eslint-disable-next-line react/prefer-stateless-function
class TweetsTable extends React.Component {

  renderTweets() {
    return _.map(this.props.tweets, (tweet) => {
      return (
        <tr key={tweet.id}>
          <td>{tweet.username}</td>
          <td>{tweet.created_at}</td>
          <td>{tweet.text}</td>
          <td>
            <Link className="btn btn-default pull-right" to={`/tweet/${tweet.id}`}>
              Reply
            </Link>
          </td>
        </tr>
      );
    });
  }

  render() {
    return (
      <table className="table table-striped">
        <thead>
          <tr>
            <th>User</th>
            <th>Date</th>
            <th>Text</th>
            <th />
          </tr>
        </thead>
        <tbody>
          {this.renderTweets()}
        </tbody>
      </table>
    );
  }

}

export default TweetsTable;
