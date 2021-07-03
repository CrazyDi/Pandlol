import React from 'react'
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom'

import routes from 'app/common/routes'
import HomePage from 'app/pages/HomePage'
import ControlsPage from 'app/pages/ControlsPage'

import useStyles from './styles'

interface Props {
}

const App = (props: Props) => {
    useStyles()

    return (
        <BrowserRouter>
            <Switch>
                <Route
                    exact path={routes.home}
                    component={HomePage} />
                <Route
                    path={routes.controls}
                    component={ControlsPage}/>
                <Redirect
                    to={routes.home} />
            </Switch>
        </BrowserRouter>
    )
}

export default App
