import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import HomePageReactTitle from '../components/HomePageReactTitle';


// eslint-disable-next-line react/prefer-stateless-function
class AppRoutes extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/" component={HomePageReactTitle} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default AppRoutes;
