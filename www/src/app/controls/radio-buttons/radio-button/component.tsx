import React, { useContext, useState, useEffect } from 'react'
import clsx from 'clsx'

import IFocusable from '../../IFocusable'
import { RadioButtonsContext } from '../component'
import RadioButtonIcon from './icon'
import useStyles from './styles'

interface Props extends IFocusable {
    className?: string
    value: string
    checked?: boolean
    disabled?: boolean
    children?: React.ReactNode
    onCheckedChanged?: (checked: boolean) => void
}

const RadioButton = (props: Props) => {
    const context = useContext(RadioButtonsContext)
    const checkedValue = context.checkedValue

    const [value, setValue] = useState<string>(props.value)
    const [checked, setChecked] = useState<boolean>(checkedValue ? checkedValue === props.value : !!props.checked)

    const classes = useStyles({
        checked: checked,
        disabled: props.disabled
    })

    const className = clsx(classes.component, props.className)
    const attributes: { [index: string]: any } = {}

    if (props.disabled) {
        attributes['aria-disabled'] = true
        attributes.disabled = true
    }

    const handleFocus = () => {
        if (props.onFocus) {
            props.onFocus()
        }
    }

    const handleBlur = () => {
        if (props.onLostFocus) {
            props.onLostFocus()
        }
    }

    const handleClick = () => {
        if (!checked) {
            setChecked(true)

            context.onCheckedValueChanged(value)

            if (props.onCheckedChanged) {
                props.onCheckedChanged(!checked)
            }
        }
    }

    useEffect(() => {
        setValue(props.value)

        const newChecked = checkedValue ? checkedValue === props.value : !!props.checked

        if (newChecked !== checked) {
            setChecked(newChecked)

            if (newChecked) {
                context.onCheckedValueChanged(value)
            }

            if (props.onCheckedChanged) {
                props.onCheckedChanged(newChecked)
            }
        }
    }, [props.value, props.checked, checkedValue])

    return (
        <button
            {...attributes}
            className={className}
            onFocus={handleFocus}
            onBlur={handleBlur}
            onClick={handleClick}
        >
            <div className={classes.input}>
                <RadioButtonIcon className={classes.icon}/>
            </div>
            <div className={classes.text}>
                {props.children}
            </div>
        </button>
    )
}

export default RadioButton
