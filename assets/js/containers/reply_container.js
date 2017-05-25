import React from 'react';
import { connect } from 'react-redux';

import { fetchTweet } from '../actions';
import TitleRow from '../components/title_row';
import TweetBox from '../components/tweet_box';


class ReplyContainer extends React.Component {

  componentDidMount() {
    this.props.fetchTweet(this.props.match.params.tweet_id);
  }

  render() {
    return (
      <div>
        <TitleRow title="Reply" btn_class="default" btn_text="Back" url="/" />
        <TweetBox tweet={this.props.tweet} />
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    tweet: state.tweet,
  };
}

export default connect(mapStateToProps, { fetchTweet })(ReplyContainer);
