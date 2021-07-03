import React from 'react'
import Label from 'controls/Label'
import ISearchResultItem from 'app/interfaces/ISearchResultItem'
import useStyles from './styles'

interface Props {
    item: ISearchResultItem
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
