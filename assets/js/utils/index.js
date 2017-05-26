import axios from 'axios';

export function getData(url) {
  return axios.get(url);
}

export function postData(url, data, token) {
  return axios.post(
    url, data, { headers: { Authorization: `Token ${token}` } }
  );
}
