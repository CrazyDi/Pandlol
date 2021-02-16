import React, { useState, useEffect, useLayoutEffect, useRef } from 'react'
import clsx from 'clsx'

import IFocusable from '../IFocusable'

import ArrowDownIcon from './arrow-down'
import ArrowUpIcon from './arrow-up'
import useStyles from './styles'

export interface DropDownItem {
    value: string
    text: string,
    disabled?: boolean
}

interface ItemState {
    selectedIndex: number
    selectedValue: string
    selectedText: string
    inputText: string
}

interface Props extends IFocusable {
    className?: string
    editable?: boolean
    disabled?: boolean
    items: DropDownItem[]
    selectedIndex?: number
    selectedValue?: string
    selectedText?: string
    inputText?: string
    noItemsText?: string
    renderInput?: (output: React.ReactNode) => React.ReactNode
    renderInputArrow?: (output: React.ReactNode) => React.ReactNode
    renderItem?: (output: React.ReactNode, item: DropDownItem) => React.ReactNode
    onSelectedItemChanged?: (item: DropDownItem) => void
    onTextChanged?: (text: string) => void
}

const DropDown = (props: Props) => {
    const [items, setItems] = useState<DropDownItem[]>(props.items)
    const [focused, setFocused] = useState<boolean>(false)
    const [expanded, setExpanded] = useState<boolean>(false)
    const [selectedIndex, setSelectedIndex] = useState<number>(props.selectedIndex || -1)
    const [selectedValue, setSelectedValue] = useState<string>(props.selectedValue || '')
    const [selectedText, setSelectedText] = useState<string>(props.selectedText || '')
    const [inputText, setInputText] = useState<string>(props.inputText || '')
    const [inputFocused, setInputFocused] = useState<boolean>(false)
    const [inputButtonFocused, setInputButtonFocused] = useState<boolean>(false)

    const inputRef = useRef<HTMLInputElement>(null)
    const inputButtonRef = useRef<HTMLButtonElement>(null)

    const classes = useStyles({
        disabled: props.disabled,
        editable: props.editable
    })

    let focusing = false
    let touchable = false

    const className = clsx(classes.component, props.className)

    const setItemState = (itemState: ItemState) => {
        setSelectedIndex(itemState.selectedIndex)
        setSelectedValue(itemState.selectedValue)
        setSelectedText(itemState.selectedText)
        setInputText(itemState.inputText)
    }

    const selectItem = (item: DropDownItem) => {
        const index = props.items.findIndex((element) => {
            return element.value === item.value
        })

        setItemState({
            selectedIndex: index,
            selectedValue: item.value,
            selectedText: item.text,
            inputText: item.text
        })
    }

    const handleInputArrowFocus = () => {
        handleFocus()
    }

    const handleInputArrowBlur = () => {
        handleBlur()
    }

    const handleInputArrowClick = (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        if (touchable) {
            return
        }

        handleExpand()
    }

    const handleInputArrowTouchStart = (event: React.TouchEvent<HTMLButtonElement>) => {
        touchable = true

        handleExpand()
    }

    const handleInputButtonFocus = () => {
        handleFocus()
    }

    const handleInputButtonBlur = () => {
        handleBlur()
    }

    const handleInputButtonClick = (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        if (touchable) {
            return
        }

        handleExpand()
    }

    const handleInputButtonTouchStart = (event: React.TouchEvent<HTMLButtonElement>) => {
        touchable = true

        handleExpand()
    }

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setInputText(event.target.value)
    }

    const handleItemSelect = (item: DropDownItem) => {
        if (item.disabled) {
            return
        }

        selectItem(item)
        setExpanded(false)

        if (props.editable) {
            setInputFocused(true)
        } else {
            setInputButtonFocused(true)
        }
    }

    const handleExpand = () => {
        setExpanded(!expanded)
    }

    const handleBlur = () => {
        focusing = false

        setTimeout(() => {
            if (!focusing) {
                setFocused(false)
                setExpanded(false)

                if (props.onLostFocus) {
                    props.onLostFocus()
                }
            }
        })
    }

    const handleFocus = () => {
        focusing = true

        if (!focused) {
            setFocused(true)

            if (props.onFocus) {
                props.onFocus()
            }
        }
    }

    const handleInputFocus = () => {
        if (window.getSelection) {
            const selection = window.getSelection()

            if (selection) {
                selection.removeAllRanges()
            }
        }

        handleFocus()
    }

    const handleInputBlur = () => {
        handleBlur()
    }

    const handleListFocus = () => {
        handleFocus()
    }

    const handleListBlur = () => {
        handleBlur()
    }

    const handleListItemFocus = () => {
        handleFocus()
    }

    const handleListItemBlur = () => {
        handleBlur()
    }

    const handleListItemClick = (item: DropDownItem) => () => {
        if (touchable) {
            return
        }

        handleItemSelect(item)
    }

    const handleListItemTouch = (item: DropDownItem) => () => {
        touchable = true

        handleItemSelect(item)
    }

    useEffect(() => {
        const state = {
            selectedIndex: -1,
            selectedValue: '',
            selectedText: '',
            inputText: ''
        }

        if (props.selectedIndex !== undefined && props.selectedIndex !== selectedIndex) {
            if (props.items.length > props.selectedIndex) {
                const item = props.items[props.selectedIndex]

                state.selectedIndex = props.selectedIndex
                state.selectedValue = item.value
                state.selectedText = item.text
                state.inputText = item.text
            }
        } else if (props.selectedValue !== undefined && props.selectedValue !== selectedValue) {
            for (let i = 0; i < props.items.length; i++) {
                const item = props.items[i]

                if (item.value === props.selectedValue) {
                    state.selectedIndex = i
                    state.selectedValue = item.value
                    state.selectedText = item.text
                    state.inputText = item.text
                    break
                }
            }
        } else if (props.selectedText !== undefined && props.selectedText !== selectedText) {
            for (let i = 0; i < props.items.length; i++) {
                const item = props.items[i]

                if (item.text === props.selectedText) {
                    state.selectedIndex = i
                    state.selectedValue = item.value
                    state.selectedText = item.text
                    state.inputText = item.text
                    break
                }
            }
        } else if (props.inputText !== undefined && props.inputText !== inputText && props.editable) {
            for (let i = 0; i < props.items.length; i++) {
                const item = props.items[i]

                if (item.text === props.selectedText) {
                    state.selectedIndex = i
                    state.selectedValue = item.value
                    state.selectedText = item.text
                    state.inputText = item.text
                    break
                }
            }
        }

        setItems(props.items)
        setSelectedIndex(state.selectedIndex)
        setSelectedValue(state.selectedValue)
        setSelectedText(state.selectedText)
        setInputText(state.inputText)
    }, [props.items, props.selectedIndex, props.selectedValue, props.selectedText, props.inputText])

    useLayoutEffect(() => {
        if (!inputFocused) {
            return
        }

        if (inputRef && inputRef.current) {
            inputRef.current.focus()

            const activeElement = document.activeElement as HTMLInputElement

            if (activeElement) {
                const textLength = (activeElement.value || '').length

                activeElement.selectionStart = textLength
                activeElement.selectionEnd = textLength
            }
        }

        setInputFocused(false)
    }, [inputFocused])

    useLayoutEffect(() => {
        if (!inputButtonFocused) {
            return
        }

        if (inputButtonRef && inputButtonRef.current) {
            inputButtonRef.current.focus()
        }

        setInputButtonFocused(false)
    }, [inputButtonFocused])

    const renderInput = () => {
        const attributes: { [index: string]: any } = {}
        let className: string

        if (props.editable) {
            className = classes.input
        } else {
            className = clsx(classes.input, classes.input_Readonly)

            attributes['aria-readonly'] = true
            attributes.readOnly = true
            attributes.tabIndex = -1
        }

        const output = (
            <input
                {...attributes}
                className={className}
                ref={inputRef}
                type="text"
                value={inputText}
                onChange={handleInputChange}
                onFocus={handleInputFocus}
                onBlur={handleInputBlur}
            />
        )

        if (props.renderInput) {
            return props.renderInput(output)
        } else {
            return output
        }
    }

    const renderInputArrow = () => {
        let arrowOutput: React.ReactNode

        if (expanded) {
            arrowOutput = (
                <ArrowUpIcon />
            )
        } else {
            arrowOutput = (
                <ArrowDownIcon />
            )
        }

        const attributes: { [index: string]: any } = {}

        if (!props.editable) {
            attributes.tabIndex = -1
        }

        const output = (
            <button
                {...attributes}
                className={classes.inputArrow}
                onFocus={handleInputArrowFocus}
                onBlur={handleInputArrowBlur}
                onClick={handleInputArrowClick}
                onTouchStart={handleInputArrowTouchStart}
            >
                {arrowOutput}
            </button>
        )

        if (props.renderInputArrow) {
            return props.renderInputArrow(output)
        } else {
            return output
        }
    }

    const renderItem = (item: DropDownItem, index: number) => {
        const selected = index === selectedIndex
        const className = clsx(classes.listItem, {
            [classes.listItem_Selected]: selected,
            [classes.listItem_Disabled]: item.disabled
        })

        const output = (
            <button
                key={index}
                className={className}
                data-value={item.value}
                onFocus={handleListItemFocus}
                onBlur={handleListItemBlur}
                onClick={handleListItemClick(item)}
                onTouchStart={handleListItemTouch(item)}
            >
                {item.text}
            </button>
        )

        if (props.renderItem) {
            return props.renderItem(output, item)
        } else {
            return output
        }
    }

    const renderInputButton = () => {
        let output: React.ReactNode

        if (!props.editable) {
            output = (
                <button
                    className={classes.inputButton}
                    ref={inputButtonRef}
                    onFocus={handleInputButtonFocus}
                    onBlur={handleInputButtonBlur}
                    onClick={handleInputButtonClick}
                    onTouchStart={handleInputButtonTouchStart}
                />
            )
        }

        return output
    }

    const renderItems = () => {
        if (!expanded) {
            return null
        }

        let output: React.ReactNode

        if (items.length) {
            output = items.map((item, index) => {
                return renderItem(item, index)
            })
        } else {
            output = (
                <div className={classes.listItemsEmpty}>
                    {props.noItemsText || 'No items'}
                </div>
            )
        }

        return (
            <div
                className={classes.list}
                tabIndex={0}
                onFocus={handleListFocus}
                onBlur={handleListBlur}
            >
                {output}
            </div>
        )
    }

    return (
        <div className={className}>
            <div className={classes.content}>
                <div className={classes.inputContent}>
                    {renderInput()}
                    {renderInputArrow()}
                    {renderInputButton()}
                </div>
                {renderItems()}
            </div>
        </div>
    )
}

export default DropDown
