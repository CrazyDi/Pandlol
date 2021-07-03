import React from 'react'
import clsx from 'clsx'

import useStyles from './styles'

interface Props {
    className?: string
}

const RadioButtonIcon = (props: Props) => {
    const classes = useStyles()

    const className = clsx(classes.component, props.className)

    return (
        <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512' className={className}>
            <circle cx='256' cy='256' r='192' fill='#333' stroke='currentColor' strokeLinecap='round' strokeLinejoin='round' strokeWidth='32'/>
        </svg>
    )
}

export default RadioButtonIcon
