import React from 'react'
import clsx from 'clsx'

import useStyles from './styles'

interface Props {
    className?: string
}

const CheckBoxIcon = (props: Props) => {
    const classes = useStyles(props)

    const className = clsx(classes.component, props.className)

    return (
        <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512' className={className}>
            <path fill='none' stroke='currentColor' strokeLinecap='round' strokeLinejoin='round' strokeWidth='32' d='M416 128L192 384l-96-96'/>
        </svg>
    )
}

export default CheckBoxIcon
