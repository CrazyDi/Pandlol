import React from 'react';
import PropTypes from 'prop-types';

import icons from 'app/common/icons';
import utils from 'app/common/utils';

import './index.scss';

const baseClassName = 'list';

class List extends React.PureComponent {
    constructor(props) {
        super(props);

        this.inputRef = React.createRef();
        this.listRef = React.createRef();

        const state = {
            items: this.props.items || []
        };

        this.prepareState(state);

        this.state = {
            ...state,
            expanded: false
        };
    }

    componentDidUpdate(prevProps) {
        const selectedTextChanged = (prevProps.selectedText !== this.props.selectedText);
        const selectedValueChanged = (prevProps.selectedValue !== this.props.selectedValue);
        const itemsChanged = (prevProps.items !== this.props.items);

        const shouldUpdateSelectedText = selectedTextChanged && this.state.selectedText !== this.props.selectedText;
        const shouldUpdateSelectedValue = selectedValueChanged && this.state.selectedValue !== this.props.selectedValue;
        const shouldUpdateItems = itemsChanged && this.state.items !== this.props.items;

        if (shouldUpdateSelectedText || shouldUpdateSelectedValue || shouldUpdateItems) {
            const state = {
                items: this.props.items || []
            };

            this.prepareState(state);

            this.setState(state);
        }

        if (this.props.focused && prevProps.focused !== this.props.focused) {
            this.inputRef.current.focus();
        }
    }

    getClassNames = () => {
        const { expanded } = this.state;
        const { className, editable, disabled } = this.props;

        const componentClassName = utils.getClassName(
            baseClassName,
            className,
            [baseClassName + '--disabled', disabled],
            [baseClassName + '--expanded', expanded]
        );

        return {
            component: componentClassName,
            label: baseClassName + '__label',
            input: baseClassName + '__input',
            inputBackground: baseClassName + '__input-background',
            inputIcon: baseClassName + '__input-icon',
            items: baseClassName + '__items',
            item: baseClassName + '__item'
        };
    };

    render() {
        const classNames = this.getClassNames();
        const inputOutput = this.renderInput(classNames);
        const listOutput = this.renderList(classNames);

        return (
            <div className={classNames.component}>
                {inputOutput}
                {listOutput}
            </div>
        );
    }

    renderInput = (classNames) => {
        const { editable, renderInput } = this.props;
        const { selectedText, expanded } = this.state;
        let inputOutput;
        let icon;
        let backgroundOutput;
        let inputAttributes;

        if (expanded) {
            icon = icons.arrowDropUp;
        } else {
            icon = icons.arrowDropDown;
        }

        if (!editable) {
            inputAttributes = {
                readOnly: true
            };

            backgroundOutput = (
                <div className={classNames.inputBackground} />
            );
        }

        if (renderInput) {
            inputOutput = renderInput();
        }

        return (
            <label className={classNames.label}>
                {inputOutput}
                <input className={classNames.input}
                    {...inputAttributes}
                    ref={this.inputRef}
                    type="text"
                    value={selectedText}
                    onChange={this.handleInputChange}
                    onKeyDown={this.handleInputKeyDown}
                    onFocus={this.handleInputFocus}
                    onBlur={this.handleComponentBlur}
                    onMouseDown={this.handleInputFocus}
                />
                <img className={classNames.inputIcon} src={icon} alt="" />
                {backgroundOutput}
            </label>
        );
    };

    renderList = (classNames) => {
        const { items, selectedIndex } = this.state;
        const renderItem = this.props.renderItem || this.renderItem;
        let output;

        if (items.length) {
            const itemsOutput = items.map((item, index) => {
                const itemClassName = utils.getClassName(
                    classNames.item,
                    [classNames.item + '--selected', index === selectedIndex]
                );

                return (
                    <li className={itemClassName}
                        key={index}
                        data-value={item.value}
                        onMouseDown={this.handleListItemMouseDown(classNames)}
                    >
                        {renderItem(item)}
                    </li>
                );
            });

            output = (
                <ul className={classNames.items}
                    role="listbox"
                    tabIndex="0"
                    ref={this.listRef}
                    onFocus={this.handleListFocus}
                    onBlur={this.handleComponentBlur}
                    onKeyDown={this.handleListKeyDown}
                >
                    {itemsOutput}
                </ul>
            );
        }

        return output;
    };

    renderItem = (item) => {
        return (
            item.text
        );
    };

    handleInputChange = (event) => {
        const { onTextChanged } = this.props;

        const selectedText = event.target.value;

        this.setState({
            selectedText: selectedText
        });

        if (onTextChanged) {
            onTextChanged(selectedText);
        }
    };

    handleInputKeyDown = (event) => {
        const { expanded, items, selectedIndex } = this.state;
        let newSelectedIndex;

        switch (event.keyCode) {
            case 27: // Esc
                if (expanded) {
                    this.setState({
                        expanded: false
                    });
                    break;
                } else {
                    return;
                }

            case 38: // Up
                if (items.length) {
                    if (expanded) {
                        if (selectedIndex > 0) {
                            newSelectedIndex = selectedIndex - 1;
                        } else {
                            newSelectedIndex = items.length - 1;
                        }

                        this.setState({
                            selectedIndex: newSelectedIndex
                        });
                    }

                    this.listRef.current.focus();

                    this.setState({
                        expanded: true
                    });
                }
                break;

            case 40: // Down
                if (items.length) {
                    if (expanded) {
                        if (selectedIndex > -1 && selectedIndex < items.length - 1) {
                            newSelectedIndex = selectedIndex + 1;
                        } else {
                            newSelectedIndex = 0;
                        }

                        this.listRef.current.focus();

                        this.setState({
                            selectedIndex: newSelectedIndex
                        });
                    }

                    this.setState({
                        expanded: true
                    });
                }
                break;

            default:
                return;
        }

        event.preventDefault();
        event.stopPropagation();
    };

    handleInputFocus = () => {
        const { disabled } = this.props;
        const { items } = this.state;

        if (window.getSelection) {
            window.getSelection().removeAllRanges();
        }

        this.focused = true;

        if (!disabled && items.length) {
            this.setState({
                expanded: true
            });
        }
    };

    handleListFocus = () => {
        this.focused = true;
    };

    handleComponentBlur = () => {
        this.focused = false;

        setTimeout(() => {
            if (!this.focused) {
                this.setState({
                    expanded: false
                });
            }
        });
    };

    handleListKeyDown = (event) => {
        const { selectedIndex, items } = this.state;
        let newSelectedIndex;

        switch (event.keyCode) {
            case 27: // Esc
                this.inputRef.current.focus();

                this.setState({
                    expanded: false
                });
                break;

            case 13:
            case 32: // Space
                this.setSelectedItem(selectedIndex);

                this.inputRef.current.focus();

                this.setState({
                    expanded: false
                });
                break;

            case 38: // Up
                if (items.length) {
                    if (selectedIndex > 0) {
                        newSelectedIndex = selectedIndex - 1;
                    } else {
                        newSelectedIndex = items.length - 1;
                    }

                    this.setState({
                        selectedIndex: newSelectedIndex
                    });
                }
                break;

            case 40: // Down
                if (items.length) {
                    if (selectedIndex > -1 && selectedIndex < items.length - 1) {
                        newSelectedIndex = selectedIndex + 1;
                    } else {
                        newSelectedIndex = 0;
                    }

                    this.setState({
                        selectedIndex: newSelectedIndex
                    });
                }
                break;

            default:
                return;
        }

        event.preventDefault();
        event.stopPropagation();
    };

    handleListItemMouseDown = (classNames) => (event) => {
        if (event.button !== 0) {
            return;
        }

        const target = event.target.closest(`.${classNames.item}`);
        const itemValue = target.dataset.value;

        if (itemValue === undefined) {
            return;
        }

        const { items } = this.state;
        const { onSelectedItemChanged } = this.props;

        for (let i = 0; i < items.length; i++) {
            const item = items[i];

            if (String(item.value) === String(itemValue)) {
                this.setSelectedItem(i);

                this.setState({
                    expanded: false
                });

                if (onSelectedItemChanged) {
                    onSelectedItemChanged(item);
                }

                break;
            }
        }
    };

    prepareState = (state) => {
        const { selectedText, selectedValue, editable } = this.props;
        const { items } = state;

        state.selectedIndex = -1;

        if (selectedValue !== undefined) {
            for (let i = 0; i < items.length; i++) {
                const item = items[i];

                if (String(item.value) === String(selectedValue)) {
                    state.selectedText = item.text;
                    state.selectedValue = item.value;
                    state.selectedIndex = i;
                    break;
                }
            }
        }

        if (selectedText && (!state.selectedValue || editable)) {
            for (let i = 0; i < items.length; i++) {
                const item = items[i];

                if (item.text === selectedText) {
                    state.selectedText = item.text;
                    state.selectedValue = item.value;
                    state.selectedIndex = i;
                    break;
                }
            }
        }

        state.selectedText = state.selectedText || '';
        state.selectedValue = state.selectedValue || '';
    };

    setSelectedItem = (selectedIndex) => {
        const { items } = this.state;
        const item = items[selectedIndex];

        this.setState({
            selectedValue: item.value,
            selectedText: item.text,
            selectedIndex: selectedIndex
        });
    };
}

List.propTypes = {
    className: PropTypes.string,
    editable: PropTypes.bool,
    disabled: PropTypes.bool,
    focused: PropTypes.bool,
    items: PropTypes.arrayOf(PropTypes.shape({
        value: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.number
        ]).isRequired,
        text: PropTypes.string
    })),
    selectedValue: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.number
    ]),
    selectedText: PropTypes.string,
    renderInput: PropTypes.func,
    renderItem: PropTypes.func,
    onSelectedItemChanged: PropTypes.func,
    onTextChanged: PropTypes.func
};

export default List;
