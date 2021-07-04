import React from 'react'
import Label from 'controls/Label'
import IChampion from 'app/interfaces/IChampion'
import useStyles from './styles'

interface Props {
    item: IChampion
}

const HomePageSearchResultItem = (props: Props) => {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <div>
                <Label>Item</Label>
            </div>
        </div>
    )
}

export default HomePageSearchResultItem
