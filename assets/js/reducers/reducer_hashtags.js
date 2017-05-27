import { FETCH_HASHTAGS } from '../constants';


export default function (state = {}, action) {
  switch (action.type) {
    case FETCH_HASHTAGS:
      return action.payload.data;
    default:
      return state;
  }
}
