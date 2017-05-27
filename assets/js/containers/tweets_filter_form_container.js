import _ from 'lodash';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import Select from 'react-select';

import { fetchUsernames } from '../actions/index';


class TweetsFilterForm extends Component {

  constructor(props) {
    super(props);
    this.state = { username: '' };
    this.onInputChange = this.onInputChange.bind(this);
  }

  componentDidMount() {
    this.props.fetchUsernames();
  }

  onInputChange(option) {
    const value = option == null ? '' : option.value;
    this.setState({ username: value });
  }

  renderUsernamesOptions() {
    return _.map(this.props.usernames, (user) => {
      return { value: user.id, label: user.username }
    });
  }

  renderUsernames() {
    return (
      <div className="col-sm-6 input-group">
        <Select
          name="username" placeholder="Username" value={this.state.username}
          options={this.renderUsernamesOptions()} onChange={this.onInputChange}
        />
      </div>
    );
  }

  render() {
    return (
      <div className="form">
        {this.renderUsernames()}
      </div>
    );
  }

}

function mapStateToProps(state) {
  return {
    usernames: state.usernames,
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({ fetchUsernames }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(TweetsFilterForm);
