import React from 'react';
import PropTypes from 'prop-types';

import icons from 'app/common/icons';
import timer from 'app/common/timer';
import Button from 'app/controls/button';

import './index.scss';

const baseClassName = 'form';

class Form extends React.PureComponent {
    constructor(props) {
        super(props);

        this.state = {
            opened: false,
            closed: true,
            transform: 0
        };
    }

    componentDidMount() {
        document.addEventListener('keydown', this.handleKeyDown);
    }

    componentWillUnmount() {
        document.removeEventListener('keydown', this.handleKeyDown);
    }

    componentDidUpdate(prevProps, prevState) {
        const { forms, name, onOpened, onClosed } = this.props;

        const opened = !!forms[name];

        if (prevState.opened !== opened) {
            this.setState({
                opened: opened
            });

            if (opened) {
                this.open();
            } else {
                this.close();
            }
        }
    }

    getClassNames = () => {
        return {
            component: baseClassName,
            header: `${baseClassName}__header`,
            back: `${baseClassName}__back`,
            backIcon: `${baseClassName}__back-icon`,
            title: `${baseClassName}__title`,
            content: `${baseClassName}__content`
        };
    };

    render() {
        const { title } = this.props;
        const { closed, transform } = this.state;

        if (closed) {
            return null;
        }

        const classNames = this.getClassNames();

        const style = {
            transform: `translateX(${transform - 100}%)`
        };

        return (
            <div className={classNames.component} style={style}>
                <div className={classNames.header}>
                    <Button className={classNames.back} theme="transparent" onClick={this.handleClose}>
                        <img className={classNames.backIcon} src={icons.arrowBack} alt="" />
                    </Button>

                    <div className={classNames.title}>{title}</div>
                </div>

                <div className={classNames.content}>
                    {this.props.children}
                </div>
            </div>
        );
    }

    handleKeyDown = (event) => {
        if (event.defaultPrevented) {
            return;
        }

        if (event.keyCode === 27) {
            this.handleClose();
        }
    };

    handleClose = () => {
        const { name, closeForm } = this.props;

        closeForm(name);
    };

    open = () => {
        const { onOpened } = this.props;

        this.setState({
            closed: false
        });

        timer.start((percent) => {
            const completed = percent === 100;

            this.setState({
                transform: percent
            });

            if (completed && onOpened) {
                onOpened();
            }
        }, 20, 10);
    };

    close = () => {
        const { onClosed } = this.props;

        timer.start((percent) => {
            const completed = percent === 100;

            this.setState({
                transform: 100 - percent,
                closed: completed
            });

            if (completed && onClosed) {
                onClosed();
            }
        }, 20, 10);
    };
}

Form.propTypes = {
    forms: PropTypes.object.isRequired,
    name: PropTypes.string.isRequired,
    closeForm: PropTypes.func.isRequired,
    title: PropTypes.string,
    onOpened: PropTypes.func,
    onClosed: PropTypes.func
};

export default Form;
