import React from 'react';

import './index.scss';

const baseClassName = 'loader';

class Loader extends React.PureComponent {
    getClassNames = () => {
        return {
            component: baseClassName
        };
    };

    render() {
        const classNames = this.getClassNames();

        return (
            <div className={classNames.component}>
            </div>
        );
    }
}

export default Loader;
