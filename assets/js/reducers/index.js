import { combineReducers } from 'redux';
import TweetsReducer from './reducer_tweets';
import UsersReducer from './reducer_users';
import TweetReducer from './reducer_tweet';
import TokenReducer from './reducer_token';
import RepliesReducer from './reducer_replies';
import UsernamesReducer from './reducer_usernames';

const rootReducer = combineReducers({
  tweets: TweetsReducer,
  users: UsersReducer,
  tweet: TweetReducer,
  token: TokenReducer,
  replies: RepliesReducer,
  usernames: UsernamesReducer,
});

export default rootReducer;
