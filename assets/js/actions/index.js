import { getData, postData } from '../utils';
import { API_URL, FETCH_TWEETS, FETCH_USERS, FETCH_TWEET, FETCH_TOKEN } from '../constants';


export function fetchTweets() {
  const request = getData(`${API_URL}tweets/`);

  return {
    type: FETCH_TWEETS,
    payload: request,
  };
}


export function fetchUsers() {
  const request = getData(`${API_URL}users/`);

  return {
    type: FETCH_USERS,
    payload: request,
  };
}

export function fetchTweet(tweetId) {
  const request = getData(`${API_URL}tweet/${tweetId}/`);

  return {
    type: FETCH_TWEET,
    payload: request,
  };
}

export function fetchToken() {
  const request = getData(`${API_URL}token/`);

  return {
    type: FETCH_TOKEN,
    payload: request,
  };
}

export function submitUser(data, token) {
  const request = postData(`${API_URL}users/`, data, token);
  request.then(() => {
    fetchUsers();
  });
}
