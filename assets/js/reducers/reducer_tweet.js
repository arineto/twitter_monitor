import { FETCH_TWEET } from '../constants';


export default function (state = {}, action) {
  switch (action.type) {
    case FETCH_TWEET:
      return action.payload.data;
    default:
      return state;
  }
}
