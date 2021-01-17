import React from 'react'
import clsx from 'clsx'

import useStyles from './styles'

interface Props {
    className?: string
    disabled?: boolean
    children?: React.ReactNode
}

const Label = (props: Props) => {
    const classes = useStyles({
        disabled: props.disabled
    })

    const className = clsx(classes.component, props.className)

    return (
        <div className={className}>
            {props.children}
        </div>
    )
}

export default Label
