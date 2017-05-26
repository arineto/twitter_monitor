import { combineReducers } from 'redux';
import TweetsReducer from './reducer_tweets';
import UsersReducer from './reducer_users';
import TweetReducer from './reducer_tweet';
import TokenReducer from './reducer_token';
import RepliesReducer from './reducer_replies';

const rootReducer = combineReducers({
  tweets: TweetsReducer,
  users: UsersReducer,
  tweet: TweetReducer,
  token: TokenReducer,
  replies: RepliesReducer,
});

export default rootReducer;
