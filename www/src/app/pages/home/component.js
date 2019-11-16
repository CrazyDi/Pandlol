import React from 'react';
import PropTypes from 'prop-types';
import get from 'lodash/get';

import api from 'app/common/api';
import constants from 'app/common/constants';
import Loader from 'app/components/loader';

import Filter from './filter';
import SearchResult from './search-result';

import './index.scss';

const baseClassName = 'home-page';

class HomePage extends React.PureComponent {
    constructor(props) {
        super(props);

        this.state = {
            searching: false,
            searchResult: null
        };
    }

    componentDidMount() {
        this.loadData();
    }

    getClassNames = () => {
        return {
            component: baseClassName,
            title: `${baseClassName}__title`,
            content: `${baseClassName}__content`,
            search: `${baseClassName}__search`
        };
    };

    render() {
        const classNames = this.getClassNames();

        const searchResultOutput = this.renderSearchResult();

        return (
            <div className={classNames.component}>
                <div className={classNames.title}>
                    home page
                </div>

                <div className={classNames.content}>
                    <Filter />
                    <div className={classNames.search}>
                        {searchResultOutput}
                    </div>
                </div>
            </div>
        );
    }

    renderSearchResult = () => {
        const { searching, searchResult } = this.state;

        if (searching) {
            return (
                <Loader />
            );
        }

        let output;

        if (searchResult) {
            output = (
                <SearchResult items={searchResult} />
            );
        }

        return output;
    };

    loadData = () => {
        this.setState({
            searching: true
        });

        api.search()
            .then((response) => {
                this.setState({
                    searching: false,
                    searchResult: response.data
                });
            });
    };
}

HomePage.propTypes = {
};

export default HomePage;
