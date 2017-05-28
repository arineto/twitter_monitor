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
      username: null, startDate: null, endDate: null, term: '', hashtags: [],
    };
    this.onFormSubmit = this.onFormSubmit.bind(this);
  }

  componentDidMount() {
    this.props.fetchUsernames();
    this.props.fetchHashtags();
  }

  onFormSubmit(event) {
    event.preventDefault();

    const { username, startDate, endDate, term, hashtags } = this.state;

    let querystring = '';

    if (username) {
      querystring = `${querystring}username=${username.value}&`;
    }

    if (startDate) {
      const startDateStr = startDate._d.toISOString().substring(0, 10);
      querystring = `${querystring}start_date=${startDateStr}&`;
    }

    if (endDate) {
      const endDateStr = endDate._d.toISOString().substring(0, 10);
      querystring = `${querystring}end_date=${endDateStr}&`;
    }

    if (term) {
      querystring = `${querystring}term=${term}&`;
    }

    const hashtagsList = _.map(this.state.hashtags, (hashtag) => {
      return hashtag.value;
    });
    if (hashtagsList.length !== 0) {
      querystring = `${querystring}hashtags=${hashtagsList}`;
    }

    this.props.handler(querystring);
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
          isOutsideRange={() => false}
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
              this.setState({ hashtags });
            }
          }
        />
      </div>
    );
  }

  render() {
    return (
      <form className="form row" onSubmit={this.onFormSubmit}>
        {this.renderUsernameField()}
        {this.renderTermField()}
        {this.renderHashtagsField()}
        {this.renderDateField()}
        <div className="pull-right">
          <button type="submit" className="btn btn-primary pull-right">Filter</button>
        </div>
      </form>
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
