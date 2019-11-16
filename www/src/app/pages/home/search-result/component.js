import React from 'react';
import PropTypes from 'prop-types';
import get from 'lodash/get';

import api from 'app/common/api';
import constants from 'app/common/constants';

import SearchResultItem from './item';

import './index.scss';

const baseClassName = 'home-page-search-result';

class HomePageSearchResult extends React.PureComponent {
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

        const itemsOutput = this.renderItems(classNames);

        return (
            <div className={classNames.component}>
                {itemsOutput}
            </div>
        );
    }

    renderItems = (classNames) => {
        const { items } = this.props;

        return items.map((item, index) => {
            return (
                <SearchResultItem key={index} item={item} />
            );
        });
    };
}

HomePageSearchResult.propTypes = {
    items: PropTypes.arrayOf(PropTypes.object).isRequired
};

export default HomePageSearchResult;
