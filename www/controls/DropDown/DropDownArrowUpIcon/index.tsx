import React from 'react'
import clsx from 'clsx'

import useStyles from './styles'

interface Props {
    className?: string
}

const DropDownArrowUpIcon = (props: Props) => {
    const classes = useStyles()

    const className = clsx(classes.component, props.className)

    return (
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" className={className}>
            <path d="M128 320l128-128 128 128z"/>
        </svg>
    )
}

export default DropDownArrowUpIcon
