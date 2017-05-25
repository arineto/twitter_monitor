import React from 'react';
import { connect } from 'react-redux';

import { fetchTweets } from '../actions';
import TitleRow from '../components/title_row';
import TweetsTable from '../components/tweets_table';


class TweetsContainer extends React.Component {

  componentDidMount() {
    this.props.fetchTweets();
  }

  render() {
    return (
      <div>
        <TitleRow title="Tweets" btn_class="primary" btn_text="Add an User" url="/users/" />
        <TweetsTable tweets={this.props.tweets} />
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { tweets: state.tweets };
}

export default connect(mapStateToProps, { fetchTweets })(TweetsContainer);
