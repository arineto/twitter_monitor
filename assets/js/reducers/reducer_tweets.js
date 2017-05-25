import { FETCH_TWEETS } from '../constants';


export default function (state = {}, action) {
  switch (action.type) {
    case FETCH_TWEETS:
      return action.payload.data;
    default:
      return state;
  }
}
