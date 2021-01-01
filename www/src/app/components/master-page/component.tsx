import React from 'react'

import MenuIcon from 'app/icons/menu'

import useStyles from './styles'

interface Props {
    children?: React.ReactNode
}

const MasterPage = (props: Props) => {
    const classes = useStyles(props)

    return (
        <div className={classes.component}>
            <MenuIcon />

            <div className={classes.page}>
                {props.children}
            </div>
        </div>
    )
}

export default MasterPage
