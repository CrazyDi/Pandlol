import React from 'react'
import MenuIcon from 'app/icons/MenuIcon'
import useStyles from './styles'

interface Props {
    children?: React.ReactNode
}

const MasterPage = (props: Props) => {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <div className={classes.header}>
                <MenuIcon/>
                Header
            </div>

            <div className={classes.page}>
                {props.children}
            </div>
        </div>
    )
}

export default MasterPage
