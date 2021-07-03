import React, { useState, useEffect } from 'react'
import clsx from 'clsx'

import IFocusable from '../IFocusable'
import useStyles from './styles'

export enum InputType {
    Text,
    Password,
    MultiLine
}

interface Props extends IFocusable {
    className?: string
    disabled?: boolean
    type?: InputType
    placeholder?: string
    maxLength?: number
    autocomplete?: boolean
    value?: string
    onChange?: (value: string) => void
}

const Input = (props: Props) => {
    const classes = useStyles({
        disabled: props.disabled
    })

    const [value, setValue] = useState<string>(props.value || '')

    const className = clsx(classes.component, {
        [classes.input]: props.type === InputType.Text || props.type === InputType.Password,
        [classes.textarea]: props.type === InputType.MultiLine,
    }, props.className)

    const attributes: { [index: string]: any } = {}

    if (props.disabled) {
        attributes['aria-disabled'] = true
        attributes.disabled = true
    }

    if (props.maxLength) {
        attributes.maxLength = props.maxLength
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

    const handleChange = (event: React.ChangeEvent<HTMLInputElement|HTMLTextAreaElement>) => {
        const value = event.target.value

        setValue(value)

        if (props.onChange) {
            props.onChange(value)
        }
    }

    useEffect(() => {
        setValue(props.value || '')
    }, [props.value])

    if (props.type === InputType.MultiLine) {
        return (
            <textarea
                {...attributes}
                placeholder={props.placeholder}
                value={value}
                className={className}
                onFocus={handleFocus}
                onBlur={handleBlur}
                onChange={handleChange}
            />
        )
    } else {
        const type = props.type === InputType.Password ? 'password' : 'text'

        if (props.autocomplete !== undefined) {
            attributes.autocomplete = props.autocomplete ? 'on' : 'off'
        }

        return (
            <input
                {...attributes}
                type={type}
                placeholder={props.placeholder}
                value={value}
                className={className}
                onFocus={handleFocus}
                onBlur={handleBlur}
                onChange={handleChange}
            />
        )
    }
}

export default Input
