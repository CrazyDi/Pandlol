import React from 'react'
import { Link as RouterLink, NavLink as RouterNavLink } from 'react-router-dom'
import clsx from 'clsx'

import useStyles from './styles'

export enum LinkType {
    Internal,
    Navigation,
    External
}

interface Props {
    className?: string
    type?: LinkType
    to: string
    target?: string
    disabled?: boolean
    children?: React.ReactNode
    onFocus?: () => void
    onLostFocus?: () => void
}

const Link = (props: Props) => {
    const classes = useStyles({
        disabled: props.disabled
    })

    const type = props.type || LinkType.Internal
    const className = clsx(classes.component, props.className)
    const attributes: { [index: string]: any } = {}

    if (props.disabled) {
        attributes['aria-disabled'] = true
        attributes.disabled = true
    }

    if (props.target) {
        attributes.target = props.target
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

    if (type === LinkType.External) {
        return (
            <a
                {...attributes}
                className={className}
                href={props.to}
                onFocus={handleFocus}
                onBlur={handleBlur}
            >
                {props.children}
            </a>
        )
    } else if (type === LinkType.Navigation) {
        return (
            <RouterNavLink
                {...attributes}
                className={className}
                to={props.to}
                onFocus={handleFocus}
                onBlur={handleBlur}
            >
                {props.children}
            </RouterNavLink>
        )
    } else {
        return (
            <RouterLink
                {...attributes}
                className={className}
                to={props.to}
                onFocus={handleFocus}
                onBlur={handleBlur}
            >
                {props.children}
            </RouterLink>
        )
    }
}

export default Link
