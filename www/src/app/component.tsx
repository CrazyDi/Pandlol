import React from 'react'
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom'

import routes from 'app/common/routes'
import HomePage from 'app/pages/home'

interface Props {
}

const App = (props: Props) => {
    return (
        <BrowserRouter>
            <Switch>
                <Route
                    exact path={routes.home}
                    component={HomePage} />
                <Redirect
                    to={routes.home} />
            </Switch>
        </BrowserRouter>
    )
}

export default App
