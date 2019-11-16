import React from 'react';
import PropTypes from 'prop-types';

import Header from 'app/components/header';

import './index.scss';

class MasterPage extends React.PureComponent {
    constructor(props) {
        super(props);

        this.state = {
        };
    }

    getClassNames = () => {
        return {
            component: 'page'
        };
    };

    render() {
        const classNames = this.getClassNames();

        return (
            <>
                <Header />
                {this.props.children}
            </>
        );
    }
}

MasterPage.propTypes = {
};

export default MasterPage;
