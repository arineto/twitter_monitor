import _ from 'lodash';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { DateRangePicker } from 'react-dates';
import React, { Component } from 'react';
import Select from 'react-select';

import { fetchUsernames } from '../actions/index';


class TweetsFilterForm extends Component {

  constructor(props) {
    super(props);
    this.state = { username: '', startDate: null, endDate: null };
  }

  componentDidMount() {
    this.props.fetchUsernames();
  }

  renderUsernameOptions() {
    return _.map(this.props.usernames, (user) => {
      return { value: user.id, label: user.username }
    });
  }

  renderUsernameField() {
    return (
      <div className="col-sm-3">
        <Select
          name="username" placeholder="Username" value={this.state.username}
          options={this.renderUsernameOptions()}
          onChange={
            (option) => {
              this.setState({ username: option == null ? '' : option.value })
            }
          }
        />
      </div>
    );
  }

  renderDateField() {
    return (
      <div className="">
        <DateRangePicker
          startDate={this.state.startDate}
          endDate={this.state.endDate}
          onDatesChange={({ startDate, endDate }) => this.setState({ startDate, endDate })}
          focusedInput={this.state.focusedInput}
          onFocusChange={focusedInput => this.setState({ focusedInput })}
        />
      </div>
    );
  }

  render() {
    return (
      <div className="form row">
        {this.renderUsernameField()}
        {this.renderDateField()}
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
