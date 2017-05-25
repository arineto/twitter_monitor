import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import TweetsContainer from '../containers/tweets_container';
import UsersContainer from '../containers/users_container';


// eslint-disable-next-line react/prefer-stateless-function
class AppRoutes extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/users/" component={UsersContainer} />
          <Route path="/" component={TweetsContainer} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default AppRoutes;
