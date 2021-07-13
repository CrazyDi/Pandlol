import React from 'react'
import clsx from 'clsx'

import useStyles from './styles'

interface Props {
    className?: string
}

const MenuIcon = (props: Props) => {
    const classes = useStyles(props)

    const className = clsx(classes.component, props.className)

    return (
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" className={className}>
            <path d="M64 384h384v-42.666H64V384zm0-106.666h384v-42.667H64v42.667zM64 128v42.665h384V128H64z"/>
        </svg>
    )
}

export default MenuIcon