import React from 'react';
import PropTypes from 'prop-types';

import './index.scss';

const baseClassName = 'header';

class Header extends React.PureComponent {
    getClassNames = () => {
        return {
            component: baseClassName,
            content: `${baseClassName}__content`
        };
    };

    render() {
        const classNames = this.getClassNames();

        return (
            <div className={classNames.component}>
                <div className={classNames.content}>
                    header
                </div>
            </div>
        );
    }
}

Header.propTypes = {
    openForm: PropTypes.func.isRequired
};

export default Header;
