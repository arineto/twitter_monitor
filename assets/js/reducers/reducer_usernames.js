import { FETCH_USERNAMES } from '../constants';


export default function (state = {}, action) {
  switch (action.type) {
    case FETCH_USERNAMES:
      return action.payload.data;
    default:
      return state;
  }
}
