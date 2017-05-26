import { FETCH_TOKEN } from '../constants';


export default function (state = {}, action) {
  switch (action.type) {
    case FETCH_TOKEN:
      return action.payload.data;
    default:
      return state;
  }
}
