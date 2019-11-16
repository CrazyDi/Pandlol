import React from 'react';
import PropTypes from 'prop-types';
import get from 'lodash/get';

import api from 'app/common/api';
import constants from 'app/common/constants';

import './index.scss';

const baseClassName = 'home-page-filter';

class HomePageFilter extends React.PureComponent {
    constructor(props) {
        super(props);

        this.state = {
        };
    }

    getClassNames = () => {
        return {
            component: baseClassName
        };
    };

    render() {
        const classNames = this.getClassNames();

        return (
            <div className={classNames.component}>
                filter
            </div>
        );
    }
}

HomePageFilter.propTypes = {
};

export default HomePageFilter;
