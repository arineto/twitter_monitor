import { combineReducers } from 'redux';
import TweetsReducer from './reducer_tweets';

const rootReducer = combineReducers({
  tweets: TweetsReducer,
});

export default rootReducer;
