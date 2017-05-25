import _ from 'lodash';
import React from 'react';


// eslint-disable-next-line react/prefer-stateless-function
class UsersTable extends React.Component {

  renderUsers() {
    return _.map(this.props.users, (user) => {
      return (
        <tr key={user.id}>
          <td>{user.username}</td>
          <td>{user.created_at}</td>
          <td>{user.status}</td>
        </tr>
      );
    });
  }

  render() {
    return (
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Username</th>
            <th>Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {this.renderUsers()}
        </tbody>
      </table>
    );
  }
}

export default UsersTable;
