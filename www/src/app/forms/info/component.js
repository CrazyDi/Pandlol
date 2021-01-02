import React from 'react';
import PropTypes from 'prop-types';

import icons from 'app/common/icons';
import api from 'app/common/api';
import constants from 'app/common/constants';
import Button from 'app/controls/button';
import Form from 'app/components/form';
import Loader from 'app/components/preloader';
import Pipe from 'app/components/pipe';

import './index.scss';

const baseClassName = 'info-form';

class InfoForm extends React.PureComponent {
    constructor(props) {
        super(props);

        this.state = {
            locking: false,
            pipe: props.pipe
        };
    }

    componentDidUpdate(prevProps) {
        const pipeChanged = (prevProps.pipe !== this.props.pipe);

        const shouldUpdatePipe = pipeChanged && this.state.pipe !== this.props.pipe;

        if (shouldUpdatePipe) {
            this.setState({
                pipe: this.props.pipe
            });
        }
    }

    getClassNames = () => {
        return {
            component: baseClassName,
            detail: `${baseClassName}__detail`,
            info: `${baseClassName}__info`,
            infoDistance: `${baseClassName}__info-distance`,
            infoDistanceIcon: `${baseClassName}__info-distance-icon`,
            infoSize: `${baseClassName}__info-size`,
            infoSizeIcon: `${baseClassName}__info-size-icon`,
            infoType: `${baseClassName}__info-type`,
            infoTypeIcon: `${baseClassName}__info-type-icon`,
            status: `${baseClassName}__status`,
            statusText: `${baseClassName}__status-text`,
            statusIcon: `${baseClassName}__status-icon`,
            description: `${baseClassName}__description`,
            descriptionText: `${baseClassName}__description-text`,
            lock: `${baseClassName}__lock`,
            lockIcon: `${baseClassName}__lock-icon`,
            history: `${baseClassName}__history`,
            historyItems: `${baseClassName}__history-items`,
            historyItem: `${baseClassName}__history-item`
        };
    };

    render() {
        const classNames = this.getClassNames();

        const pipeOutput = this.renderPipe(classNames);

        return (
            <Form
                name={constants.forms.info}
                title={'Пожарный гидрант'}
            >
                <div className={classNames.component}>
                    {pipeOutput}
                </div>
            </Form>
        );
    }

    renderPipe = (classNames) => {
        const { pipe } = this.state;
        let output;

        if (pipe) {
            const lockOutput = this.renderLock(classNames);
            const historyOutput = this.renderHistory(classNames);

            output = (
                <>
                    <Pipe pipe={pipe} />
                    {lockOutput}
                    {historyOutput}
                </>
            );
        }

        return output;
    };

    renderLock = (classNames) => {
        const { locking, pipe } = this.state;

        const disabled = !!pipe.busy;
        let iconOutput;

        if (locking) {
            iconOutput = (
                <Loader />
            );
        } else {
            let icon;

            if (pipe.busy) {
                icon = icons.lock;
            } else {
                icon = icons.unlock;
            }

            iconOutput = (
                <img className={classNames.lockIcon} src={icon} alt="" />
            );
        }

        return (
            <div className={classNames.lock}>
                <Button disabled={disabled} onClick={this.handleLockClick}>
                    {iconOutput}
                </Button>
            </div>
        );
    };

    renderHistory = (classNames) => {
        const { pipe } = this.state;
        let historyOutput;
        let title;

        if (Array.isArray(pipe.history) && pipe.history.length) {
            title = 'История';

            const historyItemsOutput = pipe.history.map((item, index) => {
                return (
                    <div className={classNames.historyItem} key={index}>
                        <div>
                            {item.date} - {item.action}
                        </div>
                        <div>
                            {item.userName}
                        </div>
                    </div>
                );
            });

            historyOutput = (
                <div className={classNames.historyItems}>
                    {historyItemsOutput}
                </div>
            );
        } else {
            title = 'История изменений отсутствует';
        }

        return (
            <div className={classNames.history}>
                <div>
                    {title}
                </div>

                {historyOutput}
            </div>
        );
    };

    handleLockClick = () => {
        const { pipe } = this.state;

        this.setState({
            locking: true
        });

        api.lockPipe(pipe.id)
            .then((response) => {
                this.setState({
                    locking: false,
                    pipe: response.data
                });
            })
            .catch((error) => {
                this.setState({
                    locking: false
                });
            });
    };
}

InfoForm.propTypes = {
    pipe: PropTypes.object
};

export default InfoForm;
