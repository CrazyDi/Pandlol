import React from 'react'
import clsx from 'clsx'

import './index.css'
import useStyles from './styles'

interface Props {
    className?: string
}

const Preloader = (props: Props) => {
    const classes = useStyles()

    const className = clsx(classes.component, props.className)

    return (
        <div className={className}>
            &nbsp;
            <div className={classes.content} />
        </div>
    )
}

export default Preloader
