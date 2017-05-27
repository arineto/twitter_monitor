import React from 'react';
import { connect } from 'react-redux';

import { fetchTweets, fetchToken } from '../actions';
import TitleRow from '../components/title_row';
import TweetsTable from '../components/tweets_table';
import TweetsFilterForm from './tweets_filter_form_container';


class TweetsContainer extends React.Component {

  componentDidMount() {
    this.props.fetchTweets();
    this.props.fetchToken();
  }

  render() {
    return (
      <div>
        <TitleRow title="Tweets" btn_class="primary" btn_text="Add an User" url="/users/" />
        <TweetsFilterForm />
        <TweetsTable tweets={this.props.tweets} />
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { tweets: state.tweets };
}

export default connect(mapStateToProps, { fetchTweets, fetchToken })(TweetsContainer);
