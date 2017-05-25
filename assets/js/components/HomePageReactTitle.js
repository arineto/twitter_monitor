import React from 'react';

const HomePageReactTitle = () => {
  const homeURL = window.Django.url('home');
  return <h2>React is rendering this page (this is page {homeURL})</h2>;
};

export default HomePageReactTitle;
