import _ from 'lodash';
import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

import { fetchUsers } from '../actions';


class UsersContainer extends React.Component {

  componentDidMount() {
    this.props.fetchUsers();
  }

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
      <div>
        <div className="row">
          <div className="col-sm-6">
            <h3>Users</h3>
          </div>

          <div className="col-sm-6">
            <Link className="btn btn-default pull-right" to="/">
              Back
            </Link>
          </div>
        </div>
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

      </div>
    );
  }
}

function mapStateToProps(state) {
  return { users: state.users };
}

export default connect(mapStateToProps, { fetchUsers })(UsersContainer);
