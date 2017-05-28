import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { replyTweet } from '../actions/index';


class ReplyForm extends Component {
  constructor(props) {
    super(props);
    this.state = { text: '' };
    this.onInputChange = this.onInputChange.bind(this);
    this.onFormSubmit = this.onFormSubmit.bind(this);
  }

  onInputChange(event) {
    this.setState({ text: event.target.value });
  }

  onFormSubmit(event) {
    event.preventDefault();

    const values = { text: this.state.text };
    this.props.replyTweet(this.props.tweet.id, values, this.props.token.key, () => {
      this.props.handler();
    });
  }

  render() {
    return (
      <div className="row">
        <form className="input-group form" onSubmit={this.onFormSubmit}>
          <div className="col-lg-11 col-md-10 col-sm-9 col-xs-8">
            <input
              value={this.state.text} placeholder="Tweet"
              className="form-control" onChange={this.onInputChange}
              required="True"
            />
          </div>
          <div className="col-sm-1">
            <button type="submit" className="btn btn-primary pull-right">Submit</button>
          </div>
        </form>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    token: state.token,
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({ replyTweet }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(ReplyForm);
