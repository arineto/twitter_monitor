import axios from 'axios';

import { API_URL, FETCH_TWEETS } from '../constants';


export function fetchTweets() {
  const request = axios.get(`${API_URL}tweets/`);

  return {
    type: FETCH_TWEETS,
    payload: request,
  };
}
