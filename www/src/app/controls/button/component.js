import React from 'react';
import PropTypes from 'prop-types';

import utils from 'app/common/utils';

import './index.scss';

const baseClassName = 'button';

class Button extends React.PureComponent {
    constructor(props) {
        super(props);

        this.buttonRef = React.createRef();
    }

    getClassNames = () => {
        const { theme, disabled, className } = this.props;

        const componentClassName = utils.getClassName(
            baseClassName,
            [`${baseClassName}--theme-${theme}`, !!theme],
            className,
            [`${baseClassName}--disabled`, disabled]
    );

        return {
            component: componentClassName
        };
    };

    render() {
        const { disabled } = this.props;
        const classNames = this.getClassNames();

        return (
            <button className={classNames.component} ref={this.buttonRef} aria-disabled={disabled} disabled={disabled} onClick={this.handleClick}>
                {this.props.children}
            </button>
        );
    }

    handleClick = (event) => {
        const { disabled, onClick } = this.props;

        if (disabled) {
            event.preventDefault();
            event.stopPropagation();
            return;
        }

        if (onClick) {
            onClick(event);
        }
    };

    focus = () => {
        this.buttonRef.current.focus();
    };
}

Button.propTypes = {
    className: PropTypes.string,
    disabled: PropTypes.bool,
    theme: PropTypes.string,
    onClick: PropTypes.func
};

export default Button;
