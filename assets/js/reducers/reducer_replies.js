import { FETCH_REPLIES } from '../constants';


export default function (state = {}, action) {
  switch (action.type) {
    case FETCH_REPLIES:
      return action.payload.data;
    default:
      return state;
  }
}
