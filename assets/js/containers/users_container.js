import React from 'react';
import { connect } from 'react-redux';

import { fetchUsers } from '../actions';
import TitleRow from '../components/title_row';
import UsersTable from '../components/users_table';


class UsersContainer extends React.Component {

  componentDidMount() {
    this.props.fetchUsers();
  }

  render() {
    return (
      <div>
        <TitleRow title="Users" btn_class="default" btn_text="Back" url="/" />
        <UsersTable users={this.props.users} />
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { users: state.users };
}

export default connect(mapStateToProps, { fetchUsers })(UsersContainer);
