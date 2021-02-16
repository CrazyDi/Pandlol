import React, { useState, useEffect } from 'react'
import clsx from 'clsx'

import IFocusable from '../IFocusable'

import CheckBoxIcon from './icon'
import useStyles from './styles'

interface Props extends IFocusable {
    className?: string
    checked?: boolean
    disabled?: boolean
    children?: React.ReactNode
    onCheckedChanged?: (checked: boolean) => void
}

const CheckBox = (props: Props) => {
    const [checked, setChecked] = useState<boolean>(!!props.checked)

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
        setChecked(!checked)

        if (props.onCheckedChanged) {
            props.onCheckedChanged(!checked)
        }
    }

    useEffect(() => {
        setChecked(!!props.checked)
    }, [props.checked])

    return (
        <button
            {...attributes}
            className={className}
            onFocus={handleFocus}
            onBlur={handleBlur}
            onClick={handleClick}
        >
            <div className={classes.input}>
                <CheckBoxIcon className={classes.icon} />
            </div>
            <div className={classes.text}>
                {props.children}
            </div>
        </button>
    )
}

export default CheckBox
