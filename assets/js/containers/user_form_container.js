import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { submitUser } from '../actions/index';


class UserForm extends Component {
  constructor(props) {
    super(props);
    this.state = { username: '' };
    this.onInputChange = this.onInputChange.bind(this);
    this.onFormSubmit = this.onFormSubmit.bind(this);
  }

  onInputChange(event) {
    this.setState({ username: event.target.value });
  }

  onFormSubmit(event) {
    event.preventDefault();

    const values = { username: this.state.username };
    this.props.submitUser(values, this.props.token.key, () => {
      this.props.handler();
    });
  }

  render() {
    return (
      <div className="row">
        <form className="input-group form" onSubmit={this.onFormSubmit}>
          <div className="col-lg-11 col-md-10 col-sm-9 col-xs-8">
            <input
              value={this.state.username} placeholder="Username"
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
  return bindActionCreators({ submitUser }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(UserForm);
