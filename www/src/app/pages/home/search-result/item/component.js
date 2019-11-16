import React from 'react';
import PropTypes from 'prop-types';
import get from 'lodash/get';

import api from 'app/common/api';
import constants from 'app/common/constants';

import './index.scss';

const baseClassName = 'home-page-search-result-item';

class HomePageSearchResultItem extends React.PureComponent {
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
                search result item
            </div>
        );
    }
}

HomePageSearchResultItem.propTypes = {
};

export default HomePageSearchResultItem;
