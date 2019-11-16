import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { combineReducers, createStore } from 'redux';

import formsReducer from 'app/reducers/forms';
import App from 'app';

import './index.scss';

const reducers = combineReducers({
    forms: formsReducer
});

const store = createStore(reducers);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);
