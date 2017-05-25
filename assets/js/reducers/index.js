import { combineReducers } from 'redux';
import TweetsReducer from './reducer_tweets';
import UsersReducer from './reducer_users';
import TweetReducer from './reducer_tweet';

const rootReducer = combineReducers({
  tweets: TweetsReducer,
  users: UsersReducer,
  tweet: TweetReducer,
});

export default rootReducer;
