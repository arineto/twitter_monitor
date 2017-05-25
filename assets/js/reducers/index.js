import { combineReducers } from 'redux';
import TweetsReducer from './reducer_tweets';
import UsersReducer from './reducer_users';

const rootReducer = combineReducers({
  tweets: TweetsReducer,
  users: UsersReducer,
});

export default rootReducer;
