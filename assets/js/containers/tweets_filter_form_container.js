import _ from 'lodash';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { DateRangePicker } from 'react-dates';
import React, { Component } from 'react';
import Select from 'react-select';

import { fetchUsernames, fetchHashtags } from '../actions/index';


class TweetsFilterForm extends Component {

  constructor(props) {
    super(props);
    this.state = {
      username: '', startDate: null, endDate: null, term: '', hashtags: [],
    };
  }

  componentDidMount() {
    this.props.fetchUsernames();
    this.props.fetchHashtags();
  }

  renderUsernameOptions() {
    return _.map(this.props.usernames, (user) => {
      return { value: user.id, label: user.username }
    });
  }

  renderHashtagsOptions() {
    return _.map(this.props.hashtags, (hashtag) => {
      return { value: hashtag.id, label: hashtag.name }
    });
  }

  renderUsernameField() {
    return (
      <div className="col-sm-2">
        <Select
          name="username" placeholder="Username" value={this.state.username}
          options={this.renderUsernameOptions()}
          onChange={
            (username) => {
              this.setState({ username });
            }
          }
        />
      </div>
    );
  }

  renderDateField() {
    return (
      <div className="col-sm-3">
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

  renderTermField() {
    return (
      <div className="col-sm-3">
        <input
          type="text" placeholder="Term" className="form-control" value={this.state.term}
          onChange={(event) => { this.setState({ term: event.target.value }); }}
        />
      </div>
    );
  }

  renderHashtagsField() {
    return (
      <div className="col-sm-3">
        <Select
          name="hashtags" placeholder="Hashtags" value={this.state.hashtags}
          multi={true} options={this.renderHashtagsOptions()}
          onChange={
            (hashtags) => {
              console.log(hashtags);
              this.setState({ hashtags });
            }
          }
        />
      </div>
    );
  }

  render() {
    return (
      <div className="form row">
        {this.renderUsernameField()}
        {this.renderTermField()}
        {this.renderHashtagsField()}
        {this.renderDateField()}
        <div className="pull-right">
          <button type="submit" className="btn btn-primary pull-right">Filter</button>
        </div>
      </div>
    );
  }

}

function mapStateToProps(state) {
  return {
    usernames: state.usernames,
    hashtags: state.hashtags,
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({ fetchUsernames, fetchHashtags }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(TweetsFilterForm);
