import _ from 'lodash';
import React from 'react';
import { connect } from 'react-redux';

import { fetchTweet, fetchReplies } from '../actions';

import TitleRow from '../components/title_row';
import TweetBox from '../components/tweet_box';
import ReplyForm from '../containers/reply_form_container';


class ReplyContainer extends React.Component {

  componentDidMount() {
    this.props.fetchTweet(this.props.match.params.tweet_id);
    this.props.fetchReplies(this.props.match.params.tweet_id);
  }

  renderReplies() {
    return _.map(this.props.replies, (reply) => {
      return (
        <div className="col-sm-12" key={reply.id}>
          <TweetBox tweet={reply} />
        </div>
      );
    });
  }

  render() {
    return (
      <div>
        <TitleRow title="Reply" btn_id="back_btn" btn_class="default" btn_text="Back" url="/" />
        <TweetBox tweet={this.props.tweet} />
        <ReplyForm tweet={this.props.tweet} />
        <h3>Replies</h3>
        {this.renderReplies()}
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    tweet: state.tweet,
    replies: state.replies,
  };
}

export default connect(mapStateToProps, { fetchTweet, fetchReplies })(ReplyContainer);
