import React from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';

import routes from 'app/common/routes';
import MasterPage from 'app/components/master-page';
import HomePage from 'app/pages/home';

class App extends React.PureComponent {
    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route
                        exact path={routes.home}
                        component={this.getPageComponent(<HomePage />)} />
                    <Redirect
                        to={routes.home} />
                </Switch>
            </BrowserRouter>
        );
    }

    getPageComponent = (component) => () => {
        return (
            <MasterPage>
                {component}
            </MasterPage>
        );
    };
}

export default App;
