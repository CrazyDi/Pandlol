import React from 'react'
import clsx from 'clsx'

import IFocusable from '../IFocusable'
import useStyles from './styles'

interface Props extends IFocusable {
    className?: string
    disabled?: boolean
    children?: React.ReactNode
    onClick?: (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => void
}

const Button = (props: Props) => {
    const classes = useStyles({
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

    const handleClick = (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        if (props.onClick) {
            props.onClick(event)
        }
    }

    return (
        <button
            {...attributes}
            className={className}
            onFocus={handleFocus}
            onBlur={handleBlur}
            onClick={handleClick}
        >
            {props.children}
        </button>
    )
}

export default Button
