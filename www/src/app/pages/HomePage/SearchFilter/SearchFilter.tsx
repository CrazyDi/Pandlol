import React from 'react'
import Button from 'controls/Button'
import useStyles from './styles'

interface Props {
}

const HomePageSearchFilter = (props: Props) => {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <div>
                <Button>Expand</Button>
            </div>
            <div>
                <Button>Search</Button>
            </div>
        </div>
    )
}

export default HomePageSearchFilter
